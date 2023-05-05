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
          <span v-if="recipe.Credit">&nbsp;|<a :href="recipe.Credit">&nbsp;Credit</a>&nbsp;|&nbsp;</span>
          <a v-if="recipe.VideoLink" :href="recipe.VideoLink">Video Tutotial</a>
        </div>
      </v-col>
    </v-row>
    <v-row>
      <v-col lg="3" ms="3" sm="12">
        <div class="d-flex flex-column i-container">
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
import { mapStores } from 'pinia';
import { useFeedbackStore } from '../stores/feedback';
import FeedbackPopup from '../components/FeedbackPopup.vue'

export default {
  components: {
    FeedbackPopup,
  },
  props: {
    recipeID: Number,
  },
  computed: {
    ...mapStores(useFeedbackStore),
  },
  data() {
    return {
      favorited: false,
      recipe: {
        ID: 1,
        Name: "Beef Stew",
        Region: "Chinese",
        TypeOfMeal: "Main dish",
        Thumbnail: null,
        Serving: "3 people",
        CookingTime: "30 minutes",
        Ingredients: [
          {
            Name: "Beef",
            Portion: "4 pounds"
          },
          {
            Name: "Carrot",
            Portion: "3"
          },
          {
            Name: "Carrot",
            Portion: "3"
          },
          {
            Name: "Carrot",
            Portion: "3"
          },
          {
            Name: "Carrot",
            Portion: "3"
          },
          {
            Name: "Carrot",
            Portion: "3"
          },
          {
            Name: "Carrot",
            Portion: "3"
          },
          {
            Name: "Carrot",
            Portion: "3"
          },
          {
            Name: "Carrot",
            Portion: "3"
          },
          {
            Name: "Carrot",
            Portion: "3"
          },
          {
            Name: "Carrot",
            Portion: "3"
          },
          {
            Name: "Carrot",
            Portion: "3"
          },
          {
            Name: "Carrot",
            Portion: "3"
          },
          {
            Name: "Carrot",
            Portion: "3"
          },
        ],
        Instructions: [
          "This is the first step",
          "This is the second step",
          "Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodi, ratione debitis quis est labore voluptatibus! Eaque cupiditate minima, at placeat totam, magni doloremque veniam neque porro libero rerum unde voluptatem!",
          "This is the second step",
          "This is the final step",
          "This is the final step",
          "This is the final step",
          "This is the final step",
          "This is the final step",
          "This is the final step",
          "This is the final step",
          "This is the final step",
        ],
        Credit: "Gabriel Chung",
        VideoLink: "https://www.youtube.com"
      }
    }
  },
  methods: {
    favoriteRecipe() {
      if (!this.favorited)
        this.favorited = true;
    },
  },
  mounted() {
    if (this.recipeID) {
      this.recipe = {
        ID: 1,
        Name: "Beef Stew 2",
        Region: "Chinese",
        TypeOfMeal: "Main dish",
        Thumbnail: null,
        Serving: "4 people",
        CookingTime: "20 minutes",
        Ingredients: [
          {
            Name: "Beef",
            Portion: "4 pounds"
          },
          {
            Name: "Carrot",
            Portion: "3"
          },
        ],
        Instructions: [
          "This is the first step",
          "This is the second step",
          "This is the second step",
          "This is the second step",
          "This is the second step",
          "This is the second step",
          "This is the second step",
          "Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodi, ratione debitis quis est labore voluptatibus! Eaque cupiditate minima, at placeat totam, magni doloremque veniam neque porro libero rerum unde voluptatem!",
          "This is the final step",
          "This is the final step",
          "This is the final step",
        ],
        Credit: "Gabriel Chung",
        VideoLink: "www.abcdef.com"
      }
    }
  },
}
</script>

<style scoped>
  .i-container {
    border-left: 2px solid rgb(7, 29, 100);
    padding-left: 12px;
    color: black;
    max-height: 65vh;
  }

  .i-title {
    margin: 5px 0px;
  }

  .instructions {
    overflow-y: auto;

    height: 40%;
  }

  .recipe-overlay {
    z-index: 100;
    background-color:rgba(245, 233, 212, 0.795);
    color: black;
    padding: 10px;
    height: inherit;
  }

  .return-icon {
    margin-left: 10px;
    position: absolute;
    left: 0;
  }

  .right-icons {
    margin-left: 10px;
    position: absolute;
    right: 0;
  }
</style>
