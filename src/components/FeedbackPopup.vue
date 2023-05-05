<script>
import { mapState, mapStores } from 'pinia';
import { useFeedbackStore } from '../stores/feedback';
import { useUserStore } from '../stores/user';

export default {
  props: {
    recipeID: Number,
  },
  computed: {
    ...mapStores(useFeedbackStore),
    ...mapState(useUserStore, ['userID']),
  },
  data() {
    return {
      feedback: "",
      type: "Recipe",
    }
  },
  methods: {
    async submitFeedback() {
      if (!this.feedback) {
        return;
      }

      // let api = '';

      let params = {
        UserID: this.userID,
        Feedback: this.feedback,
        Category: this.type,
      }

      console.log(params);
      this.feedback = "";
      this.type = "Recipe";
      // let response = await fetch(api, params);
      // let json = await response.json();
      // if (response.ok) {
      // } else {
      // }

      this.feedbackStore.openClose();
    }
  },
}
</script>

<template>
  <v-dialog
    v-model="feedbackStore.dialog"
    width="500px"
  >

    <v-card>
      <v-form>
        <v-container>
          <v-row>
            <v-col class="category-title">
              Category
            </v-col>
            <v-col cols="8">
              <v-radio-group v-model="type" inline color="blue">
                <v-radio label="Recipe" value="Recipe"></v-radio>
                <v-radio label="Overall" value="Overall"></v-radio>
              </v-radio-group>
            </v-col>
          </v-row>
          <v-textarea label="Feedback" v-model="feedback"></v-textarea>
        </v-container>
      </v-form>
      <v-card-actions>
        <v-btn color="primary" block @click="submitFeedback">Submit feedback</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<style scoped>
  .category-title {
    margin: 10px;
  }
</style>
