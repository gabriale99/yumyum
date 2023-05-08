<script setup>
import { ref } from 'vue'
import { storeToRefs } from 'pinia';
import { useUserStore } from '../stores/user';
import { useRouter } from 'vue-router';
import ShowRecipe from '../components/ShowRecipe.vue'
import ListRecipes from '../components/ListRecipes.vue'
import YumDashboard from '../components/YumDashboard.vue'

const user = useUserStore();

const { userID, profilePic } = storeToRefs(user);

const router = useRouter();

if (!userID.value) {
  router.push('/');
}

function toUserPreference() {
  router.push('/user');
}

const tab = ref('Daily Refresh');
const tabs = ['Daily Refresh', 'Favorites', 'Analytics']

function changeTab(t) {
  tab.value = t;
}
</script>

<template>
  <main>
    <div class="d-flex justify-center align-center text-h1 flex-row banner">
      <span>Yum Yum</span>
      <v-avatar
        class="right-icons profile-pic"
        size="90px"
        @click="toUserPreference"
      >
        <v-img
          v-if="profilePic"
          alt="Avatar"
          :src="profilePic"
        ></v-img>
        <v-icon
          v-else
          icon="mdi-account-circle"
          color="amber-darken-1"
        ></v-icon>
      </v-avatar>
    </div>
    <v-tabs
      fixed-tabs
      bg-color="amber-darken-1"
      class="tabs"
    >
      <v-tab v-for="t in tabs" @click="changeTab(t)">
        {{ t }}
      </v-tab>
    </v-tabs>
    <div class="d-flex main-background justify-center">
      <ShowRecipe v-if="tab === 'Daily Refresh'" />
      <ListRecipes v-else-if="tab === 'Favorites'" />
      <YumDashboard v-else />
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

.profile-pic {
  margin-right: 20px;
  background-color: black;
}
</style>