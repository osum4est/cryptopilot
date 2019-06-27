<template>
  <v-container fill-height>
    <v-layout justify-center align-center column>
      <v-flex>
        <h1>Congratulations!</h1>
      </v-flex>
      <v-flex>
        <h3>You found the super secret non existent page!</h3>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script lang="ts">
    import Vue from "vue";
    import Component from 'vue-class-component';

    @Component
    export default class PageNotFound extends Vue {

    }
</script>
