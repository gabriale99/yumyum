<template>
  <v-container class="login-overlay">
    <v-row class="d-flex justify-center">
      <v-col cols="8">
        <v-row class="justify-center text-h1">
          Welcome to Yumyum
        </v-row>
        <v-row class="justify-center text-h5">
          your daily recipe surprise that alleviates from the stress of finding new recipes.
        </v-row>
      </v-col>
    </v-row>
    <v-row class="justify-center">
      <div class="fb-login-button" data-width="" data-size="large" data-button-type="rounded" data-layout="" data-auto-logout-link="false" data-use-continue-as="true"></div>
    </v-row>
  </v-container>
</template>

<script>
  export default {
    methods: {
      checkLoginState() {
        FB.getLoginStatus(function(response) {
          // console.log(response)
          // statusChangeCallback(response);
        });
      }
    },
    mounted() {}
  }
</script>

<style>
  .login-overlay {
    z-index: 100;
    background-color:rgba(255, 255, 255, 0.795);
    height: inherit;
    width: 100vw !important;
  }
</style>
