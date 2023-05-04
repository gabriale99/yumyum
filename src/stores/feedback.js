import { defineStore } from 'pinia'

export const useFeedbackStore = defineStore({
  id: 'feedback',
  state: () => ({
    dialog : false,
  }),
  actions: {
    openClose() {
      this.dialog = !this.dialog;
    }
  }
})
