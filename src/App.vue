<script>
import { RouterView } from 'vue-router'
</script>

<template>
  <div class="d-flex align-center text-h1 flex-column banner">
    <span>Yum Yum</span>
  </div>
  <v-tabs
    fixed-tabs
    bg-color="amber-darken-1"
    class="tabs"
  >
    <v-tab to="/">
      Daily Refresh
    </v-tab>
    <v-tab to="/about">
      Favorites
    </v-tab>
  </v-tabs>
    
  <div class="d-flex main-content justify-center">
    <RouterView />
  </div>
</template>

<style scoped>
.banner{
  background-image: url('./assets/images/banner.png');
  background-size: contain;
  background-repeat: repeat;
}

.banner span {
  z-index: 100;
  background-color:rgb(255, 179, 0);
  color: black;
  padding: 0px 5px;
}

.main-content {
  background-image: url('./assets/images/cooking_icon.png');
  background-repeat: repeat;
  background-position: center;
  background-size: contain;
  height: 85vh;
}

.tabs {
  z-index: 200;
}
</style>
