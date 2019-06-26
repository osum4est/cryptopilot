<template>
  <currency-line-chart v-if="chartData" :data="chartData"></currency-line-chart>
</template>

<script lang="ts">
    import Vue from "vue";
    import Component from "vue-class-component";
    import {Prop} from "vue-property-decorator";
    import CurrencyLineChart from "@/charts/CurrencyLineChart";
    import axios from "axios";

    @Component({
        components: {CurrencyLineChart}
    })
    export default class CurrencyGraph extends Vue {
        chartData: any = null;

        @Prop()
        currencyData!: CurrencyData;

        async mounted() {
            this.chartData = (await axios.get("/api/price_history", {
                params: {
                    currency_id: this.currencyData.currency_id, // TODO: Update models to use camelCase
                    length: "2week",
                },
            })).data;
        }
    }
</script>
