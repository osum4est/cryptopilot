<template>
  <v-container grid-list-xl>
    <v-layout row wrap>
      <v-flex xs12 grow v-for="currencyData in currencyDataItems">
        <currency-overview v-bind:currency-data="currencyData"></currency-overview>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script lang="ts">
    import Vue from "vue";
    import Component from "vue-class-component";
    import axios from "axios";
    import CurrencyOverview from "@/components/CurrencyOverview.vue";

    @Component({
        components: {
            CurrencyOverview
        }
    })
    export default class CandleData extends Vue {
        currencyDataItems: CurrencyData[] = [];

        async mounted() {
            let currencyDataItemsJson = (await axios.get("/api/candle_overviews")).data.results;
            for (let i = 0; i < currencyDataItemsJson.length; i++) {
                let currencyDataJson = currencyDataItemsJson[i];
                currencyDataJson.currency =
                    <Currency> ((await axios.get("/api/currencies/" + currencyDataJson.currency_id)).data);
                this.currencyDataItems.push(<CurrencyData> currencyDataJson);
            }
        }
    };
</script>
