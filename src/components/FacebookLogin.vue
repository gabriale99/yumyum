<template>
  <div>
    <div
      class="fb-like"
      data-share="true"
      data-width="450"
      data-show-faces="true">
    </div>
    <fb:login-button 
      scope="public_profile,email"
      :onlogin="checkLoginState">
    </fb:login-button>
  </div>
</template>

<script>
  export default {
    methods: {
      checkLoginState(rep) {
        console.log(rep)
      }
    },
    mounted() {
      // FB.getLoginStatus(function(response) {
      //   statusChangeCallback(response);
      // });
    }
  }
</script>

<style></style>
