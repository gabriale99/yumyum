<template>
  <div class="loading-overlay d-flex justify-center align-center" :style="`height: ${h}; width: ${w}`">
    <v-progress-circular indeterminate :size="128" :width="12"></v-progress-circular>
  </div>
</template>

<script>
export default {
  props: {
    h: String,
    w: String,
  },
}
</script>

<style scoped>
  .loading-overlay {
    position: absolute;
    top: 0;
    left: 0;
    z-index: 400;
    background-color:rgba(252, 230, 194);
  }
</style>