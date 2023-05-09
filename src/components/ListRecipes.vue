<template>
  <LoadingScreen v-if="loadingStore.isLoading" h="85vh" w="100vw"/>
  <v-row
    v-if="!tabStore.recipeToShow"
    class="recipes-container"
  >
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
  <ShowRecipe
    v-else
  />
</template>

<script>
import axios from 'axios'
import { mapState, mapStores } from 'pinia';
import { useLoadingStore } from '../stores/loading';
import { useTabStore } from '../stores/tabs';
import { useUserStore } from '../stores/user';
import { environment } from '../environments/environment'
import LoadingScreen from './LoadingScreen.vue'
import ShowRecipe from './ShowRecipe.vue'

export default {
  components: {
    ShowRecipe,
    LoadingScreen,
  },  
  computed: {
    ...mapStores(useLoadingStore),
    ...mapStores(useTabStore),
    ...mapState(useUserStore, ['userID']),
  },  
  data() {
    return {
      recipes: [],
    }  
  },  
  methods: {
    selectRecipe(id) {
      this.tabStore.selectRecipe(id);
    },
    async getFavoriteRecipes() {
      this.loadingStore.changeLoadingStatus(true);
      let api = environment.yumyumapi;
      api = `${api}favorite?UserID=${this.userID}`

      let resp = await axios.get(api);
      // console.log(resp);
      
      this.recipes = resp.data;
      this.loadingStore.changeLoadingStatus(false);
    },
  },  
  async mounted() {
    await this.getFavoriteRecipes();
  },    
}
</script>

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
