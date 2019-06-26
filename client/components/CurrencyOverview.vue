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
              <price-history-line-chart v-if="chartData" :data="chartData"></price-history-line-chart>
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
    import CurrencyCard from "@/components/CurrencyCard.vue";
    import {Prop} from "vue-property-decorator";
    import axios from "axios";
    import PriceHistoryLineChart from '@/charts/PriceHistoryLineChart';
    import {CurrencyData} from "@/models";

    @Component({
        components: {CurrencyCard, PriceHistoryLineChart}
    })
    export default class CurrencyOverview extends Vue {
        chartData: any = null;

        @Prop()
        currencyData!: CurrencyData;

          async mounted() {
            this.chartData = (await axios.get("/api/price_history", {
              params: {
                currency_id: this.currencyData.currencyId,
                length: "2week",
              },
            })).data;
          }
    }
</script>
