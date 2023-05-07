<template>
  <FeedbackPopup
    :recipeID="recipe.ID"
  />

  <div class="d-flex flex-column recipe-overlay">
    <v-row>
      <v-col cols="12">
        <div class="d-flex flex-row justify-center align-center">
          <v-btn
            v-show="!!recipeID"
            class="ma-2 return-icon"
            color="blue"
            icon="mdi-arrow-u-left-top"
            @click="$emit('returnToList')"
          ></v-btn>
          <div class="d-flex justify-center text-h2">{{ recipe.Name }}</div>
          <div class="right-icons">
            <v-btn
              v-show="!recipeID"
              class="ma-2"
              :color="!favorited? 'indigo' : 'red'"
              icon="mdi-heart-circle"
              @click="favoriteRecipe"
              :disabled="favorited"
            ></v-btn>
            <v-btn
              class="ma-2"
              icon="mdi-comment"
              @click="feedbackStore.openClose"
            ></v-btn>
          </div>
        </div>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <div class="d-flex flex-row justify-center text-h5">
          {{ recipe.Region }} | {{ recipe.TypeOfMeal }} | {{ recipe.Serving }}
          <span v-if="recipe.Credit">&nbsp;|<a :href="recipe.Credit" target="_blank">&nbsp;Credit</a>&nbsp;|&nbsp;</span>
          <a v-if="recipe.VideoLink" :href="recipe.VideoLink" target="_blank">Video Tutotial</a>
        </div>
      </v-col>
    </v-row>
    <v-row>
      <v-col lg="4" ms="4" sm="12">
        <div class="d-flex flex-column i-container">
          <v-img
            v-if="!!recipe.Thumbnail"
            :src="recipe.Thumbnail"
            height="300px"
            cover
          ></v-img>
          <div class="d-flex text-h3 justify-center i-title">Ingredients</div>
            <v-table density="compact" class="instructions ">
              <tbody>
                <tr
                  v-for="ing in recipe.Ingredients"
                  :key="ing.Name"
                >
                  <td class="text-center">{{ ing.Name }}</td>
                  <td class="text-center">{{ ing.Portion }}</td>
                </tr>
              </tbody>
            </v-table>
        </div>
      </v-col>
      <v-col>
        <div class="d-flex flex-column i-container">
          <div class="d-flex text-h3 justify-center i-title">Instructions</div>
          <div class="instructions">
            <div v-for="(ins, idx) in recipe.Instructions">
              <div class="text-h5">
                <div class="text-brown-darken-4">
                  <b>Step {{ idx + 1 }}</b>
                </div>
                <div>
                  {{ ins }}
                </div>
              </div>
              <v-divider></v-divider>
            </div>
          </div>
        </div>
      </v-col>
    </v-row>
  </div>
</template>

<script>
import axios from 'axios'
import { mapStores, mapState } from 'pinia';
import { useFeedbackStore } from '../stores/feedback';
import { useUserStore } from '../stores/user';
import FeedbackPopup from '../components/FeedbackPopup.vue'
import { environment } from '../environments/environment'

export default {
  components: {
    FeedbackPopup,
  },
  props: {
    recipeID: Number,
  },
  computed: {
    ...mapStores(useFeedbackStore),
    ...mapState(useUserStore, ['userID']),
  },
  data() {
    return {
      favorited: false,
      recipe: {}
    }
  },
  methods: {
    async favoriteRecipe() {
      if (this.favorited) {
        return;
      }
        
      let api = environment.yumyumapi;

      let params = {
        UserID: this.userID,
        ID: this.recipe.ID
      };

      let resp = await axios.put(`${api}favorite`, params);
      
      if (resp.status === 200) {
        // console.log(resp.data);
        this.favorited = true;
      }
    },
    async getRecipe(recipeID) {
      let api = environment.yumyumapi;
      api = `${api}recipe?UserID=${this.userID}`
      if (recipeID) {
        api = `${api}&RecipeID=${recipeID}`
      }

      let resp = await axios.get(api);
      // console.log(resp);
      
      if (resp.status === 200) {
        this.recipe = resp.data['recipe'];
        this.favorited = resp.data['favorited'];
      }
    }
  },
  async mounted() {
    await this.getRecipe(this.recipeID);
  },
}
</script>

<style scoped>
  .i-container {
    border-left: 2px solid rgb(7, 29, 100);
    padding-left: 12px;
    color: black;
    max-height: 68vh;
  }

  .i-title {
    margin: 5px 0px;
  }

  .instructions {
    overflow-y: auto;
  }

  .recipe-overlay {
    z-index: 100;
    background-color:rgba(252, 230, 194, 0.9);
    color: black;
    padding: 10px;
  }

  .return-icon {
    margin-left: 10px;
    position: absolute;
    left: 0;
  }
</style>
