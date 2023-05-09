// import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useUserStore = defineStore("user", {
  state: () => ({
    accessToken: null,
    profilePic: null,
    userID: '10219328332312730',
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
