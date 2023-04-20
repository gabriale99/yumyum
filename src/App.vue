<script setup>
import { RouterLink, RouterView } from 'vue-router'
import HelloWorld from './components/HelloWorld.vue'
</script>

<template>
  <div class="d-flex align-center text-h2 flex-column banner">
    <span>Yum Yum</span>
  </div>
  <v-tabs
    fixed-tabs
    bg-color="amber-darken-1"
  >
    <v-tab to="/">
      Option
    </v-tab>
    <v-tab to="/about">
      Another Option
    </v-tab>
  </v-tabs>
  <v-row align-content="center" justify="center" class="main-content">
    <v-col cols="6">
      <RouterView />
    </v-col>
  </v-row>
</template>

<style scoped>
.banner{
  background-image: url('./assets/images/banner.png');
  background-size: contain;
  background-repeat: repeat;
}

.banner span {
  /* left: 0; */
  z-index: 100;
  background-color:rgba(251, 231, 183, 0.7);
  color: black;
}

.main-content {
  background-image: url('./assets/images/cooking_icon.png');
  background-size: contain;
  background-repeat: repeat;
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}

@media (min-width: 1024px) {
  .banner{
    background-image: url('./assets/images/banner.png');
    background-size: contain;
    background-repeat: repeat;
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }

  nav {
    text-align: left;
    margin-left: -1rem;
    font-size: 1rem;

    padding: 1rem 0;
    margin-top: 1rem;
  }
}
</style>
