<template>
  <v-container class="main-background">
    <div class="d-flex justify-center align-center flex-column login-overlay">
      <v-row class="d-flex justify-center align-center">
        <v-col cols="12">
          <v-row class="justify-center text-h1">
            Welcome to Yum Yum
          </v-row>
          <v-row class="justify-center text-h5">
            your daily recipe surprise that alleviates you from the stress of finding new recipes.
          </v-row>
        </v-col>
      </v-row>
      <v-row class="justify-center">
        <!-- <div
          class="fb-login-button"
          data-max-rows="1"
          data-size="large"
          data-button-type="continue_with"
          data-use-continue-as="true"
          @login="checkLoginStatus"
          ></div> -->
        <v-btn @click="login" size="x-large" color="amber-darken-1">Login</v-btn>
      </v-row>
    </div>
  </v-container>
</template>

<script>
import { mapStores } from 'pinia';
import { useUserStore } from '../stores/user';
import router from '../router';

export default {
  computed: {
    ...mapStores(useUserStore),
  },
  methods: {
    login() {
      let app = this;
      FB.login(function(response) {
        if (response.authResponse) {
          app.userStore.setupUser(response.authResponse.userID, response.authResponse.access)
          console.log('Welcome!  Fetching your information.... ');
          FB.api('/me', function(response) {
            console.log('Good to see you, ' + response.name + '.');
          });
          console.log(app.userStore.userID)
        } else {
          console.log('User cancelled login or did not fully authorize.');
        }
      });

      if (false) {
        router.push('/')
      } else {
        router.push('/user')
      }
    },
    // checkLoginStatus() {
    //   FB.getLoginStatus(function(response) {
    //     console.log(response.userID)
    //   });
    // }
  },
  mounted() {
    if (this.userID) {
      router.push('/')
    }
  },
}
</script>

<style>
  .login-overlay {
    z-index: 100;
    background-color:rgba(255, 255, 255, 0.795);
    height: inherit;
    width: inherit;
  }

  .v-container {
    height: 100vh;
    width: 100vw;
    max-width: none;
  }
</style>
