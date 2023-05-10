<template>
  <LoadingScreen v-if="loadingStore.isLoading" h="100vh" w="100vw"/>
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
import axios from 'axios';
import router from '../router';
import { mapStores, mapActions } from 'pinia';
import { useLoadingStore } from '../stores/loading';
import { useUserStore } from '../stores/user';
import { environment } from '../environments/environment'
import LoadingScreen from './LoadingScreen.vue'

export default {
  components: {
    LoadingScreen,
  },
  computed: {
    ...mapStores(useLoadingStore),
    ...mapStores(useUserStore),
  },
  methods: {
    checkLoginStatus() {
      let app = this;
      FB.getLoginStatus(function(response) {
        if (response.status === 'connected') {
          var uid = response.authResponse.userID;
          var accessToken = response.authResponse.accessToken;
          app.userStore.setupUser(uid, accessToken)
          FB.api('/me/picture', 'GET', {
            "redirect": false,
            "type": "large",
            "access_token": app.userStore.accessToken
          }, function(response) {
            app.userStore.storeProfilePic(response.data.url);
            router.push('/home');
          });
        }
      });
    },
    login() {
      let app = this;
      let api = environment.yumyumapi;
      this.loadingStore.changeLoadingStatus(true);
      FB.login(function(response) {
        if (response.authResponse) {
          app.userStore.setupUser(response.authResponse.userID, response.authResponse.accessToken)
          console.log('Welcome!  Fetching your information.... ');
          FB.api('/me', function(response) {
            // console.log(response)
            console.log('Good to see you, ' + response.name + '.');
          });
          
          FB.api('/me/picture', 'GET', {
            "redirect": false,
            "type": "large",
            "access_token": app.userStore.accessToken
          }, function(response) {
            // console.log(app.userStore.accessToken)
            app.userStore.storeProfilePic(response.data.url);
            // app.userStore.storeProfilePic(response)
            // console.log(app.userStore.profilePic)
          });

          axios.get(`${api}user?UserID=${app.userStore.userID}`)
          .then(resp => {
            if (resp.data['isFirstTime']) {
              router.push('/user')
            } else {
              router.push('/home')
            }
          });

        } else {
          console.log('User cancelled login or did not fully authorize.');
        }
        app.loadingStore.changeLoadingStatus(false);
      });
    },
  },
  mounted() {
    this.checkLoginStatus();
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
