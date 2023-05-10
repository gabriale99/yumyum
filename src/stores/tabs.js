import { defineStore } from 'pinia'

export const useTabStore = defineStore('tab', {
  state: () => ({
    tab: 0,
    defaultTabs : ['Daily Refresh', 'Favorites', 'Analytics'],
    selectedRecipe: null,
  }),
  getters: {
    recipeToShow: (state) => state.selectedRecipe,
    currentTab: (state) => state.tab,
    tabs: (state) => state.defaultTabs,
  },
  actions: {
    changeTab(t) {
      if (t === 'DailyRefresh') {
        this.selectedRecipe = null;
      }
      this.tab = t;
    },
    selectRecipe(r) {
      this.selectedRecipe = r;
    },
  }
})
