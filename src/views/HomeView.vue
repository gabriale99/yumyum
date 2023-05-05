<script setup>
import { ref } from 'vue'
import { storeToRefs } from 'pinia';
import { useUserStore } from '../stores/user';
import { useRouter } from 'vue-router';
import ShowRecipe from '../components/ShowRecipe.vue'
import ListRecipes from '../components/ListRecipes.vue'

const user = useUserStore();

const { userID } = storeToRefs(user);

const showRecipe = ref(true);

const router = useRouter();

if (!userID.value) {
  router.push('/landing');
}
</script>

<template>
  <main>
    <div class="d-flex align-center text-h1 flex-column banner">
      <span>Yum Yum</span>
    </div>
    <v-tabs
      fixed-tabs
      bg-color="amber-darken-1"
      class="tabs"
    >
      <v-tab @click="showRecipe = true">
        Daily Refresh
      </v-tab>
      <v-tab @click="showRecipe = false">
        Favorites
      </v-tab>
    </v-tabs>
    <div class="d-flex main-background justify-center">
      <ShowRecipe v-if="showRecipe" />
      <ListRecipes v-else />
    </div>
  </main>
</template>

<style scoped>
.banner{
  background-image: url('../assets/images/banner.png');
  background-size: contain;
  background-repeat: repeat;
}

.banner span {
  z-index: 100;
  background-color:rgb(255, 179, 0);
  color: black;
  padding: 0px 5px;
}

.tabs {
  z-index: 200;
}
</style>