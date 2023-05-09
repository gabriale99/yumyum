<script setup>
import { ref } from 'vue';
import { storeToRefs } from 'pinia';
import { useTabStore } from '../stores/tabs';
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

const tabStore = useTabStore();
const { tabs, currentTab } = storeToRefs(tabStore);
const tab = currentTab.value? ref(currentTab.value) : ref(0)
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
      v-model="tab"
    >
      <v-tab v-for="t, i in tabs" @click="tabStore.changeTab(i)">
        {{ t }}
      </v-tab>
    </v-tabs>
    <div class="d-flex main-background justify-center">
      <ShowRecipe v-if="tab === 0" />
      <ListRecipes v-else-if="tab === 1" />
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