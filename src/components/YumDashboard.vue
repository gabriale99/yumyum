<template>
  <div class="d-flex align-center overlay">
    <Bar
      v-if="showChart"
      :options="chartOptions"
      :data="chartData"
      ref="bar"
    />
  </div>
</template>

<script>
import axios from 'axios';
// import { mapState } from 'pinia';
import { Bar } from 'vue-chartjs'
import { environment } from '../environments/environment'

import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

export default {
  components: { Bar },
  // computed: {
  //   ...mapState(useUserStore, ['userID']),
  // },
  data() {
    return {
      chartData: null,
      chartOptions: {
        plugins: {
            title: {
                display: true,
                text: 'Top 10 Cuisines preferred by users'
            },
        },
        scales: {
          y: {
            min: 0,
            max: 5,
            ticks: {
              // forces step size to be 50 units
              stepSize: 1
            }
          }
        }
      },
      showChart: false,
    }
  },
  methods: {
    async getAnalytic(resource) {
      this.showChart = false;
      let api = environment.yumyumapi;

      let resp = await axios.get(`${api}analytic/${resource}`);

      if (resp.status === 200) {
        // console.log(resp);
        this.chartData = {
          'labels': Object.keys(resp['data']),
          'datasets': [{
            label: '',
            data: Object.values(resp['data']),
            backgroundColor: [
              'rgba(255, 99, 132)',
            ],
            'xAxisID': 'Cuisine'
          }]
        }
        // this.chartData['labels'] = Object.keys(resp['data']);
        // this.chartData['datasets'] = [ { data: Object.values(resp['data']) } ];
        // console.log(this.chartData['labels'])
        // console.log(this.chartData['datasets'][0])
        this.showChart = true;
      }
    }
  },
  async mounted() {
    await this.getAnalytic('cuisine');
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
