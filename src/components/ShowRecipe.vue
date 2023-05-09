<template>
  <FeedbackPopup
    :recipeID="recipe.ID"
  />

  <LoadingScreen v-if="loadingStore.isLoading" h="85vh" w="100vw"/>
  <div class="d-flex flex-column recipe-overlay">
    <v-row>
      <v-col cols="12">
        <div class="d-flex flex-row justify-center align-center">
          <v-btn
            v-show="!!recipeToShow"
            class="ma-2 return-icon"
            color="blue"
            icon="mdi-arrow-u-left-top"
            @click="selectRecipe(null)"
          ></v-btn>
          <div class="d-flex justify-center text-h2">{{ recipe.Name }}</div>
          <div class="right-icons">
            <v-btn
              v-show="!recipeToShow"
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
import { mapStores, mapState, mapActions } from 'pinia';
import { useFeedbackStore } from '../stores/feedback';
import { useLoadingStore } from '../stores/loading';
import { useRecipeStore } from '../stores/recipe';
import { useTabStore } from '../stores/tabs';
import { useUserStore } from '../stores/user';
import { environment } from '../environments/environment'
import FeedbackPopup from './FeedbackPopup.vue'
import LoadingScreen from './LoadingScreen.vue'

export default {
  components: {
    FeedbackPopup,
    LoadingScreen,
  },
  computed: {
    ...mapStores(useFeedbackStore),
    ...mapStores(useLoadingStore),
    ...mapStores(useRecipeStore),
    ...mapState(useTabStore, ['recipeToShow']),
    ...mapState(useUserStore, ['userID']),
  },
  data() {
    return {
      favorited: false,
      isLoading: false,
      recipe: {}
    }
  },
  methods: {
    ...mapActions(useTabStore, ['selectRecipe']),
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
        this.recipeStore.setFavorited(true);
      }
    },
    async getRecipe() {
      if (!!this.recipeStore.recipe && !this.recipeToShow) {
        this.recipe = this.recipeStore.dailyRecipe
        this.favorited = this.recipeStore.dailyFavorite
        return;
      }
      this.loadingStore.changeLoadingStatus(true);

      let api = environment.yumyumapi;
      api = `${api}recipe?UserID=${this.userID}`
      if (this.recipeToShow) {
        api = `${api}&RecipeID=${this.recipeToShow}`
      }

      let resp = await axios.get(api);
      // console.log(resp);
      
      if (resp.status === 200) {
        this.recipe = resp.data['recipe'];
        this.favorited = resp.data['favorited'];
        if (!this.recipeToShow) {
          this.recipeStore.setRecipe(this.recipe);
          this.recipeStore.setFavorited(this.favorited);
        }
      }

      this.loadingStore.changeLoadingStatus(false);
    }
  },
  async mounted() {
    await this.getRecipe();
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
