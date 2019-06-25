<template>
  <v-app :dark="dark">

    <v-navigation-drawer
        clipped
        fixed
        v-model="drawer"
        app>
      <v-list>
        <v-list-tile to="dashboard">
          <v-list-tile-action>
            <v-icon>mdi-view-dashboard</v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-list-tile-title>Dashboard</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
        <v-list-tile to="auto_traders">
          <v-list-tile-action>
            <v-icon>mdi-robot</v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-list-tile-title>Auto Traders</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
        <v-list-tile to="candle_data">
          <v-list-tile-action>
            <v-icon>mdi-database</v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-list-tile-title>Candle Data</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
      </v-list>
    </v-navigation-drawer>

    <v-toolbar app fixed clipped-left>
      <v-toolbar-side-icon @click.stop="drawer = !drawer"></v-toolbar-side-icon>
      <v-toolbar-title class="headline">
        <span>Crypto</span>
        <span class="font-weight-light">Pilot</span>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-toolbar-items>
        <v-btn icon>
          <v-icon @click="dark = !dark">mdi-brightness-2</v-icon>
        </v-btn>
      </v-toolbar-items>
    </v-toolbar>

    <v-content>
      <v-container fluid>
        <router-view></router-view>
      </v-container>
    </v-content>

    <v-footer app fixed>
      <span>&copy; Forrest Jones 2019</span>
    </v-footer>

  </v-app>
</template>

<script lang="ts">
    import Vue from "vue";
    import Component from "vue-class-component";
    import {Watch} from 'vue-property-decorator';

    @Component
    export default class App extends Vue {
        drawer = true;
        dark: boolean = localStorage.dark === "true";

        @Watch('dark')
        onPropertyChanged(val: string) {
            localStorage.dark = val;
        }
    };
</script>
