<template>
  <v-container grid-list-xs>
    <v-layout row wrap>

      <v-flex xs12 md4 pa-1>
        <v-card>
          <currency-card :currency-data="currencyData"></currency-card>
        </v-card>
      </v-flex>

      <v-flex xs12 md8 pa-1>
        <v-card style="height: 100%; min-height: 265px">
          <v-container style="height: 100%; width: 100%">
            <div class="div-fill-sizer">
              <currency-graph :currency-data="currencyData"></currency-graph>
            </div>
          </v-container>
        </v-card>
      </v-flex>

    </v-layout>
  </v-container>
</template>

<script lang="ts">
    import Vue from "vue";
    import Component from "vue-class-component";
    import CurrencyGraph from "@/components/CurrencyGraph.vue";
    import CurrencyCard from "@/components/CurrencyCard.vue";
    import {Prop} from "vue-property-decorator";

    @Component({
        components: {CurrencyGraph, CurrencyCard}
    })
    export default class CurrencyOverview extends Vue {
        @Prop()
        currencyData!: CurrencyData;
    }
</script>
