<template>
  <LoadingScreen v-if="loadingStore.isLoading" h="85vh" w="100vw"/>
  <div class="d-flex flex-column align-center overlay">
    <div class="d-flex flex-row justify-space-around align-center" style="width: 50vw; max-height: 5vh;">
      <v-radio-group inline v-model="resource" hide-details>
        <v-radio label="Cuisine Preferenec" value="cuisine"></v-radio>
        <v-radio label="Favorite Recipe" value="favorite"></v-radio>
      </v-radio-group>
      <v-select
        density="compact"
        hide-details
        v-if="resource === 'favorite'"
        v-model="category"
        :items="categories"
      ></v-select>
    </div>
    <Bar
      :options="chartOptions"
      :data="chartData"
      ref="bar"
    />
  </div>
</template>

<script>
import axios from 'axios';
import { mapStores } from 'pinia';
import { Bar } from 'vue-chartjs'
import { useLoadingStore } from '../stores/loading';
import { environment } from '../environments/environment'
import LoadingScreen from './LoadingScreen.vue'

import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

export default {
  components: {
    Bar,
    LoadingScreen,
  },
  computed: {
    ...mapStores(useLoadingStore),
  },
  watch: {
    resource: async function(newVal, oldVal) {
      if (newVal !== oldVal) {
        await this.getAnalytic();
      }
    },
    category: function(newVal, oldVal) {
      if (newVal !== oldVal) {
        this.transformTop10FavoriteRecipe();
      }
    },
  },
  data() {
    return {
      categories: ['CookingTime', 'Serving', 'Region', 'TypeOfMeal'],
      category: 'CookingTime',
      chartData: {
        'label': [],
        'datasets': [
          {
            data: [],
          }
        ]
      },
      chartOptions: {
        plugins: {
            title: {
                display: true,
                text: ''
            },
        },
        scales: {
          y: {
            ticks: {
              stepSize: 1
            }
          }
        }
      },
      favoriteRecipeData: null,
      resource: 'cuisine',
    }
  },
  methods: {
    async getAnalytic() {
      this.loadingStore.changeLoadingStatus(true);
      let api = environment.yumyumapi;
      let resp = await axios.get(`${api}analytic/${this.resource}`);

      if (resp.status === 200) {
        let respData = resp['data']
        if (this.resource === 'cuisine') {
          this.transformTop10Cuisine(respData);
        } else {
          this.favoriteRecipeData = respData;
          this.transformTop10FavoriteRecipe();
        }
      }
      this.loadingStore.changeLoadingStatus(false);
    },
    transformTop10Cuisine(resp) {
      this.chartData = {
        'labels': Object.keys(resp),
        'datasets': [{
          label: '',
          data: Object.values(resp),
          backgroundColor: [
            'rgba(99, 132, 255)',
          ],
        }]
      }

      this.chartOptions['plugins']['title']['text'] = 'Top 10 Cuisines preferred by users';
    },
    transformTop10FavoriteRecipe() {
      let orders = {};
      let cat = this.category;
      for (let r of this.favoriteRecipeData) {
        if (!orders[r[cat]]) {
          orders[r[cat]] = r['Count']
        } else {
          orders[r[cat]] += r['Count']
        }
      }

      orders = Object.keys(orders).map(x => {
        return {'label': x, 'value': orders[x]}
      });
      orders.sort((x, y) => y['value']- x['value']);

      orders.slice(10);
      let labels = orders.map(x => x['label']);
      let data = orders.map(x => x['value']);

      this.chartData = {
        'labels': labels,
        'datasets': [{
          label: '',
          data: data,
          backgroundColor: [
            'rgba(99, 132, 255)',
          ],
        }]
      }

      this.chartOptions['plugins']['title']['text'] = `Top ${this.category} by favorite recipes`;
    },
  },
  async mounted() {
    await this.getAnalytic();
  }
}
</script>

<style scoped>
  
  .overlay {
    z-index: 100;
    background-color:rgba(252, 230, 194, 1);
    color: black;
    padding: 10px;
    height: 85vh;
    width: 80vw;
  }
</style>
