<script>
export default {
  props: {
    recipeID: Number,
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
        credit: "Gabriel Chung",
        videoLink: "www.abcdef.com"
      }
    }
  },
  methods: {
    favoriteRecipe() {
      console.log(this.recipe.ID)
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
        credit: "Gabriel Chung",
        videoLink: "www.abcdef.com"
      }
    }
  },
}
</script>

<template>
  <div class="recipe">
    <v-row>
      <v-col class="d-flex flex-row justify-center align-center">
        <v-btn
          v-show="!!recipeID"
          class="ma-2 return-icon"
          color="blue"
          icon="mdi-arrow-u-left-top"
          @click="$emit('returnToList')"
        ></v-btn>
        <div class="d-flex justify-center text-h2">{{ recipe.Name }}</div>
        <v-btn
          v-show="!recipeID"
          class="ma-2 favorite-icon"
          :color="!favorited? 'indigo' : 'red'"
          icon="mdi-heart-circle"
          @click="favoriteRecipe"
          :disabled="favorited"
        ></v-btn>
      </v-col>
    </v-row>
    <v-row class="level-2-row">
      <v-col cols="4">
        <div class="text-h3">Ingredients</div>
        <v-table density="compact" class="ingredients">
          <thead>
            <tr>
              <th class="text-left">
                <b>Name</b>
              </th>
              <th class="text-left">
                <b>Portion</b>
              </th>
            </tr>
          </thead>
          <tbody>
            <tr
              v-for="ing in recipe.Ingredients"
              :key="ing.Name"
            >
              <td>{{ ing.Name }}</td>
              <td>{{ ing.Portion }}</td>
            </tr>
          </tbody>
        </v-table>
      </v-col>
      <v-col class="level-2-col">
        <div class="instruction-container">
          <div class="d-flex text-h3 justify-center">Instructions</div>
          <div class="instructions">
            <div v-for="ins in recipe.Instructions">
              <div class="text-h5">
                {{ ins }}
              </div>
              <br />
            </div>
          </div>
        </div>
      </v-col>
    </v-row>

  </div>
</template>

<style scoped>

  .favorite-icon {
    margin-right: 10px;
    position: absolute;
    right: 0;
  }

  .ingredients {
    margin: 5px 0px;
    max-height: 70%;
    overflow-y: auto;
  }

  .instruction-container {
    border-left: 1px solid black;
    padding-left: 12px;
    height: 80%;
    color: black;
  }

  .instructions {
    overflow-y: auto;
    max-height: 90%;
  }

  .level-2-row {
    height: inherit;
  }

  .level-2-col {
    height: inherit;
  }

  .recipe {
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
</style>
