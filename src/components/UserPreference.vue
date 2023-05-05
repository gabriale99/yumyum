<template>
  <v-container class="d-flex justify-center align-center flex-column main-background">
    <span class="text-h2 pref-title">Yum Yum</span>
    <div class="pref-container">
      <v-row class="cuisine">
        <v-col>
          <!-- Cuisine Preference -->
          <v-row>
            <v-col>
              <span class="cuisine-title text-h5">Cuisine Prefences</span>
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
                <v-radio label="True" :value="true"></v-radio>
                <v-radio label="False" :value="false"></v-radio>
              </v-radio-group>
            </v-col>
          </v-row>
  
          <!-- Ingredients and Allergic food -->
          <v-row>
            <v-col cols="6">
              <!-- Text input -->
              <v-row>
                <v-col>
                  <v-text-field
                    placeholder="Insert ingredient"
                    density="compact"
                    v-model="ingredient"
                    @keypress.enter="addIngredient"
                    :bg-color="inputColor">
                  </v-text-field>
                </v-col>
              </v-row>
              <!-- Chips -->
              <v-row class="ingredients-adder">
                <v-col>
                  <v-chip
                    v-for="ingr in ingredients"
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
import colors from 'vuetify/lib/util/colors'
import { mapState } from 'pinia';
import { useUserStore } from '../stores/user';
import router from '../router';

export default {
  data() {
    return {
      allergy: null,
      allergies: [],
      chipColor: colors.black,
      inputColor: colors.grey.lighten4,
      cuisines: [],
      ingredient: null,
      ingredients: [],
      selectedCuisines: [],
      vegetarian: false,
    }
  },
  computed: {
    ...mapState(useUserStore, ['userID']),
  },
  methods: {
    addAllergic() {
      if (!this.allergy) {
        return;
      }

      this.allergies.push(this.allergy);
      this.allergy = null;
    },
    addIngredient() {
      if (!this.ingredient) {
        return;
      }

      this.ingredients.push(this.ingredient);
      this.ingredient = null;
    },
    submitPreferences() {
      if (!this.selectedCuisines.length) {
        // warning
        return;
      }

      // let api = '';

      let params = {
        UserID: this.userID,
        Ingredients: this.ingredients,
        Preferences: this.selectedCuisines,
        Vegetarian: this.vegetarian,
        Allergy: this.allergies,
      }

      console.log(params);

      router.push('/')
    }
  },
  mounted() {
    let cuisines = [
      'British', 'Malaysian', 'Indian', 'American', 'Mexican', 'Russian', 'French',
      'Canadian', 'Jamaican', 'Chinese', 'Italian', 'Dutch', 'Vietnamese', 'Polish',
      'Irish', 'Croatian', 'Japanese', 'Moroccan', 'Tunisian', 'Turkish',
      'Greek', 'Egyptian', 'Portuguese', 'Kenyan', 'Thai', 'Spanish',
    ]

    // https://stackoverflow.com/questions/8495687/split-array-into-chunks
    let transformedCuisines = [];
    let chunkSize = 4;
    for (let i = 0; i < cuisines.length; i += chunkSize) {
      let chunk = cuisines.slice(i, i + chunkSize);
      transformedCuisines.push(chunk)
    }
    this.cuisines = transformedCuisines;
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

  .cuisine-title {
    padding-left: 10px;
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