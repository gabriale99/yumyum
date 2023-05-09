import { defineStore } from 'pinia'

export const useRecipeStore = defineStore('recipe', {
  state: () => ({
    favorited: false,
    recipe : null,
  }),
  getters: {
    dailyRecipe: (state) => state.recipe,
    dailyFavorite: (state) => state.favorited,
  },
  actions: {
    setFavorited(f) {
      this.favorited = f;
    },
    setRecipe(r) {
      this.recipe = r;
    },
  }
})
