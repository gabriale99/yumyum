// import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useUserStore = defineStore("user", {
  state: () => ({
    accessToken: null,
    profilePic: null,
    userID: null,
  }),
  actions: {
    setupUser(userID, accessToken) {
      this.userID = userID;
      this.accessToken = accessToken;
    },
    storeProfilePic(pic) {
      this.profilePic = pic;
    },
  }
});
