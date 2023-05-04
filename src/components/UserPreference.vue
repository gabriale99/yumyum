<template>
  <div class="preference-container">
    <v-container>
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
            <v-col cols="6">
              <!-- Text input -->
              <v-row>
                <v-col>
                  <v-text-field
                    placeholder="Insert allergic food"
                    density="compact"
                    v-model="allergy"
                    @keypress.enter="addAllergic"
                    :bg-color="inputColor"></v-text-field>
                </v-col>
              </v-row>
              <!-- Chips -->
              <v-row>
                <v-col class="ingredients-adder">
                  <v-chip
                    v-for="al in allergies"
                    class="ma-2"
                    closable
                    :color="chipColor"
                  >
                    {{ al }}
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
    </v-container>
  </div>
</template>

<script>
import colors from 'vuetify/lib/util/colors'

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
        UserID: '',
        Ingredients: this.ingredients,
        Preferences: this.selectedCuisines,
        Vegetarian: this.vegetarian,
        Allergy: this.allergies,
      }

      console.log(params);
    }
  },
  mounted() {
    let cuisines = [
      'British', 'Malaysian', 'Indian', 'American', 'Mexican', 'Russian', 'French',
      'Canadian', 'Jamaican', 'Chinese', 'Italian', 'Dutch', 'Vietnamese', 'Polish',
      'Irish', 'Croatian', 'Unknown', 'Japanese', 'Moroccan', 'Tunisian', 'Turkish',
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
    background-color: rgba(253, 224, 181, 0.9);
    border-radius: 10px;
    height: 80%;
  }

  .cuisine-title {
    padding-left: 10px;
  }

  .ingredients-adder {
    height: 250px;
    max-height: 250px;
    overflow: auto;
  }

  .preference-container {
    z-index: 100;
    background-color: rgba(245, 233, 212, 0.7);
    padding: 10px;
    height: inherit;
  }
</style>