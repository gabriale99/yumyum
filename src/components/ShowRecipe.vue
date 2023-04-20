<script setup>
import { ref } from 'vue'
  // defineProps({
  // msg: {
  //     type: String,
  //     required: true
  // }
  // })

  // const recipe = ref({
  //   ID: [idMeal],
  //   Name: [strMeal],
  //   Region: [strRegion],
  //   TypeOfMeal: [strTags],
  //   Thumbnail: [strMealThumb],
  //   Serving: <str>,
  //   CookingTime: <str>,
  //   Ingredients: [
  //     {
  //       Name: [strIngredientX],
  //       Portion: [strMeasureX]
  //     }
  //   ],
  //   Instructions: [
  //     ""
  //   ],
  //   credit: [strSource],
  //   videoLink: [strYouTube]
  // })

  const recipe = ref({
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
      }
    ],
    Instructions: [
      "This is the first step",
      "This is the second step",
      "This is the final step",
    ],
    credit: "Gabriel Chung",
    videoLink: "www.abcdef.com"
  })
</script>

<template>
  <div>
    <v-row>
      <v-col>
        <div class="d-flex justify-center text-h2 green">{{ recipe.Name }}</div>
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="4">
        <div class="text-h3">Ingredients</div>
        <v-table density="compact">
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
      <v-col>
        <div class="d-flex text-h3 justify-center">Instructions</div>
        <div v-for="ins in recipe.Instructions">
          <div class="text-h5">
            {{ ins }}
          </div>
          <br />
        </div>
      </v-col>
    </v-row>

  </div>
</template>

<style scoped>
h1 {
  font-weight: 500;
  font-size: 2.6rem;
  top: -10px;
}

h3 {
  font-size: 1.2rem;
}

.greetings h1,
.greetings h3 {
  text-align: center;
}

@media (min-width: 1024px) {
  .greetings h1,
  .greetings h3 {
    text-align: left;
  }
}
</style>
