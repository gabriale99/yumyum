<script>
import ShowRecipe from '../components/ShowRecipe.vue'

export default {
  components: {
    ShowRecipe,
  },
  data() {
    return {
      recipes: [
        {
          ID: 1,
          Name: "Scramble Eggs with Tomato",
          Region: 'Chinese',
          TypeOfMeal: 'Dish',
          Thumbnail: "https://images.food52.com/H9ApwoVc35v_4WzAHX1WYwC286k=/2016x1344/filters:format(webp)/b9564bf8-cf23-484b-82de-f26dffea55a5--2002-6.jpg",
          Serving: '4 people',
          CookingTime: '15 minutes',
          credit: "Gabriel Chung",
        },
        {
          ID: 2,
          Name: "Scramble Eggs with Seared Spam",
          Region: 'Chinese',
          TypeOfMeal: 'Dish',
          Thumbnail: "https://lh3.googleusercontent.com/6Gigya3mJmGG0GF5HTRXtwbGQ1MQf78Auox8So0Nxc2o5eLjaWrBzUI-PKTiuU7uoftBw3u6wbyoABvFMWSytw=w1280-h1280-c-rj-v1-e365",
          Serving: '4 people',
          CookingTime: '15 minutes',
          credit: "Gabriel Chung",
        },
        {
          ID: 3,
          Name: "Scramble Eggs x",
          Region: 'Chinese',
          TypeOfMeal: 'Dish',
          Thumbnail: "https://lh3.googleusercontent.com/6Gigya3mJmGG0GF5HTRXtwbGQ1MQf78Auox8So0Nxc2o5eLjaWrBzUI-PKTiuU7uoftBw3u6wbyoABvFMWSytw=w1280-h1280-c-rj-v1-e365",
          Serving: '4 people',
          CookingTime: '15 minutes',
          credit: "Gabriel Chung",
        },
        {
          ID: 3,
          Name: "Scramble Eggs x",
          Region: 'Chinese',
          TypeOfMeal: 'Dish',
          Thumbnail: "https://lh3.googleusercontent.com/6Gigya3mJmGG0GF5HTRXtwbGQ1MQf78Auox8So0Nxc2o5eLjaWrBzUI-PKTiuU7uoftBw3u6wbyoABvFMWSytw=w1280-h1280-c-rj-v1-e365",
          Serving: '4 people',
          CookingTime: '15 minutes',
          credit: "Gabriel Chung",
        },
        {
          ID: 3,
          Name: "Scramble Eggs x",
          Region: 'Chinese',
          TypeOfMeal: 'Dish',
          Thumbnail: "https://lh3.googleusercontent.com/6Gigya3mJmGG0GF5HTRXtwbGQ1MQf78Auox8So0Nxc2o5eLjaWrBzUI-PKTiuU7uoftBw3u6wbyoABvFMWSytw=w1280-h1280-c-rj-v1-e365",
          Serving: '4 people',
          CookingTime: '15 minutes',
          credit: "Gabriel Chung",
        },
        {
          ID: 3,
          Name: "Scramble Eggs x",
          Region: 'Chinese',
          TypeOfMeal: 'Dish',
          Thumbnail: "https://lh3.googleusercontent.com/6Gigya3mJmGG0GF5HTRXtwbGQ1MQf78Auox8So0Nxc2o5eLjaWrBzUI-PKTiuU7uoftBw3u6wbyoABvFMWSytw=w1280-h1280-c-rj-v1-e365",
          Serving: '4 people',
          CookingTime: '15 minutes',
          credit: "Gabriel Chung",
        },
        {
          ID: 3,
          Name: "Scramble Eggs x",
          Region: 'Chinese',
          TypeOfMeal: 'Dish',
          Thumbnail: "https://lh3.googleusercontent.com/6Gigya3mJmGG0GF5HTRXtwbGQ1MQf78Auox8So0Nxc2o5eLjaWrBzUI-PKTiuU7uoftBw3u6wbyoABvFMWSytw=w1280-h1280-c-rj-v1-e365",
          Serving: '4 people',
          CookingTime: '15 minutes',
          credit: "Gabriel Chung",
        }
      ],
      selectedRecipe: null,
    }
  },
  methods: {
    selectRecipe(id) {
      this.selectedRecipe = id;
    }
  },
}
</script>

<template>
  <v-row class="recipes-container" v-if="!selectedRecipe">
    <v-col class="d-flex flex-row justify-center flex-wrap recipes">
      <v-card
        v-for="r in recipes"
        :key="r.ID"
        class="recipe-2"
        @click="selectRecipe(r.ID)"
      >
        <v-img
          v-if="!!r.Thumbnail"
          :src="r.Thumbnail"
          height="250px"
          cover
        ></v-img>

        <v-card-title>
          {{ r.Name }}
        </v-card-title>

        <v-card-subtitle>
          {{ r.Region }} | {{ r.Serving }} | {{ r.CookingTime }}
        </v-card-subtitle>
      </v-card>
    </v-col>
  </v-row>
  <ShowRecipe :recipeID="selectedRecipe" @returnToList="selectedRecipe=null" v-else />
</template>

<style scoped>
.recipes-container {
  padding: 5px;
  height: inherit;
}

.recipes{
  height: inherit;
  overflow: auto;
}

.recipe-2 {
  margin: 10px;
  background-color:burlywood;
  min-width: 30%;
  max-width: 50%;
}
</style>
