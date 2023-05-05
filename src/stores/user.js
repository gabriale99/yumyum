// import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useUserStore = defineStore("user", {
  state: () => ({
    accessToken: null,
    userID: null,
  }),
  actions: {
    setupUser(userID, accessToken) {
      this.userID = userID;
      this.accessToken = accessToken;
    },
  }
});
