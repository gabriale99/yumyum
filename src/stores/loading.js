import { defineStore } from 'pinia'

export const useLoadingStore = defineStore('loading', {
  state: () => ({
    isLoading : false,
  }),
  actions: {
    changeLoadingStatus(l) {
      this.isLoading = l;
    }
  }
})
