<template>
  <v-container grid-list-xl>
    <v-layout row wrap>
      <v-flex xs3 grow v-for="currency_data in currency_datas">
        <currency-data v-bind:currency_data="currency_data"></currency-data>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script lang="ts">
    import Vue from "vue";
    import Component from "vue-class-component";
    import CurrencyData from "@/components/CurrencyData.vue";
    import axios from "axios";

    @Component({
        components: {
            CurrencyData,
        }
    })
    export default class CandleData extends Vue {
        currency_datas!: Any[] = [];

        mounted() {
            axios.get("/api/candle_overviews")
                .then(res => {
                    for (let i = 0; i < res.data.results.length; i++) {
                        let result = res.data.results[i];
                        axios.get("/api/currencies/" + result.currency_id)
                            .then(res => {
                                result.currency = res.data;
                                this.currency_datas.push(result);
                            });
                    }
                });
        }
    };
</script>
