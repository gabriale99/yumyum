<script>
// import { ref } from 'vue';

export default {
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
        }
      ],
    }
  },
}
</script>

<template>
  <v-row class="recipes-container">
    <v-col>
      <v-card
        v-for="r in recipes"
        :key="r.ID"
        variant="outlined"
        class="recipe"
      >
      <v-img
        :src="r.Thumbnail"
        height="200px"
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
</template>

<style scoped>
.recipes-container {
  padding: 5px;
}
.recipe {
  margin: 5px 0px;
  background-color: aliceblue;
}
</style>
