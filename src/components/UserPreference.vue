<template>
  <v-container class="d-flex justify-center align-center flex-column main-background">
    <span class="text-h2 pref-title">Yum Yum</span>
    <div class="pref-container">
      <v-row class="cuisine">
        <v-col>
          <!-- Cuisine Preference -->
          <v-row>
            <v-col>
              <span class="text-h5">Cuisine Prefences</span>
            </v-col>
          </v-row>
          <v-row>
            <v-col v-for="cu1 in cuisines">
              <v-checkbox
                v-for="cu2 in cu1"
                v-model="selectedCuisines"
                :label="cu2"
                :value="cu2"
                color="indigo"
                multiple
                hide-details></v-checkbox>
            </v-col>
          </v-row>
  
          <!-- Vegetarian -->
          <v-row>
            <v-col class="d-flex flex-row align-center">
              <span class="text-h6">Vegetarian?</span>
              <v-radio-group v-model="vegetarian" inline color="green" hide-details>
                <v-radio label="Yes" :value="true"></v-radio>
                <v-radio label="No" :value="false"></v-radio>
              </v-radio-group>
            </v-col>
          </v-row>
  
          <!-- Ingredients and Allergic food -->
          <v-row>
            <v-col cols="8">
              <!-- Text input -->
              <v-row>
                <v-col>
                  <v-autocomplete
                    placeholder="Insert ingredient"
                    density="compact"
                    v-model="ingredient"
                    :items="ingredients"
                    :bg-color="inputColor"
                  ></v-autocomplete>
                </v-col>
                <v-col>
                  <v-btn @click="addIngredient" color="rgb(250, 207, 142)">
                    add ingredient
                  </v-btn>
                </v-col>
              </v-row>
              <!-- Chips -->
              <v-row class="ingredients-adder">
                <v-col>
                  <v-chip
                    v-for="ingr in insertedIngredients"
                    class="ma-2"
                    closable
                    :color="chipColor"
                  >
                    {{ ingr }}
                  </v-chip>
                </v-col>
              </v-row>
            </v-col>
          </v-row>

          <v-row>
            <v-col>
              <v-btn color="rgb(250, 207, 142)" @click="submitPreferences">
                Submit Information
              </v-btn>
            </v-col>
          </v-row>
        </v-col>
      </v-row>
    </div>
  </v-container>
</template>

<script>
import axios from 'axios';
import colors from 'vuetify/lib/util/colors'
import { mapState } from 'pinia';
import { useUserStore } from '../stores/user';
import router from '../router';
import { environment } from '../environments/environment'

export default {
  data() {
    return {
      chipColor: colors.black,
      inputColor: colors.grey.lighten4,
      cuisines: [],
      ingredient: null,
      ingredients: [],
      insertedIngredients: [],
      selectedCuisines: [],
      vegetarian: false,
    }
  },
  computed: {
    ...mapState(useUserStore, ['userID']),
  },
  methods: {
    addIngredient() {
      if (!this.ingredient) {
        return;
      }

      this.insertedIngredients.push(this.ingredient);
      this.ingredient = null;
    },
    async getCuisines() {
      let cuisines = await this.getResource('region');

      // https://stackoverflow.com/questions/8495687/split-array-into-chunks
      let transformedCuisines = [];
      let chunkSize = 4;
      for (let i = 0; i < cuisines.length; i += chunkSize) {
        let chunk = cuisines.slice(i, i + chunkSize);
        transformedCuisines.push(chunk)
      }
      this.cuisines = transformedCuisines;
    },
    async getIngredients() {
      this.ingredients = await this.getResource('ingredient');
    },
    async getResource(table) {
      let api = environment.yumyumapi;

      let resp = await axios.get(`${api}resource?table=${table}`);

      if (resp.status === 200) {
        return resp['data']['output'];
      }
    },
    async getUserData() {
      let api = environment.yumyumapi;

      let resp = await axios.get(`${api}user?UserID=${this.userID}`);

      if (resp.status === 200 && !resp['data']['isFirstTime']) {
        let data = resp['data'];
        if (!data['isFirstTime']) {
          this.insertedIngredients = data['Ingredients'];
          this.selectedCuisines = data['Preferences'];
          this.vegetarian = data['Vegetarian'];
        }
      }
    },
    async submitPreferences() {
      if (!this.selectedCuisines.length) {
        // warning
        return;
      }

      let api = environment.yumyumapi;
      // console.log(api)

      let params = {
        UserID: this.userID,
        Ingredients: this.insertedIngredients,
        Preferences: this.selectedCuisines,
        Vegetarian: this.vegetarian,
      }

      // console.log(params);

      let resp = await axios.put(`${api}user`, params);

      if (resp.status === 200) {
        // console.log(resp.data['message']);
        router.push('/')
      }

    }
  },
  async mounted() {
    if (!this.userID) {
      router.push('/landing')
    }
    await this.getCuisines();
    await this.getIngredients();
    await this.getUserData();
  },
}
</script>

<style scoped>

  .cuisine {
    background-color: rgba(248, 196, 118, 2);
    border-radius: 10px;
    width: 80vw;
    margin: 5px;
  }

  .ingredients-adder {
    height: 20vh;
    max-height: 20vh;
    overflow: auto;
  }

  .pref-container {
    z-index: 100;
    padding: 10px;
  }

  .pref-title {
    background-color: rgba(248, 196, 118, 2);
    padding: 20px;
    border-radius: 25px;
  }

  .v-container {
    height: 100vh;
    width: 100vw;
    max-width: none;
  }
</style>