<script setup>
import { storeToRefs } from 'pinia';
// import UserPreference from '../components/UserPreference.vue'
import FacebookLogin from '../components/FacebookLogin.vue'
import ShowRecipe from '../components/ShowRecipe.vue'
import { useUserStore } from '../stores/user';

const user = useUserStore();

const { isFirstTime } = storeToRefs(user);

</script>

<template>
  <main>
    <FacebookLogin v-if="isFirstTime"/>
    <ShowRecipe v-else/>
  </main>
</template>
