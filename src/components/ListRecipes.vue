<script>
import axios from 'axios'
import { mapState } from 'pinia';
import { useUserStore } from '../stores/user';
import ShowRecipe from '../components/ShowRecipe.vue'
import { environment } from '../environments/environment'

export default {
  components: {
    ShowRecipe,
  },
  computed: {
    ...mapState(useUserStore, ['userID']),
  },
  data() {
    return {
      recipes: [],
      selectedRecipe: null,
    }
  },
  methods: {
    selectRecipe(id) {
      this.selectedRecipe = id;
    },
    async getFavoriteRecipes() {
      let api = environment.yumyumapi;
      api = `${api}favorite?UserID=${this.userID}`

      let resp = await axios.get(api);
      // console.log(resp);
      
      this.recipes = resp.data;
    },
  },
  async mounted() {
    await this.getFavoriteRecipes();
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
  height: 85vh;
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
  height: 42%;
}
</style>
