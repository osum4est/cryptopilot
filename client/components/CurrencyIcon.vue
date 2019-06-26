<template>
  <v-img :src="getIconPath" :height="height" :width="width" :position="position" contain></v-img>
</template>

<script lang="ts">
    import {Prop} from "vue-property-decorator";
    import Component from "vue-class-component";
    import Vue from "vue";
    import {Currency} from "@/models";

    @Component
    export default class CurrencyIcon extends Vue {
        @Prop()
        currency!: Currency;
        @Prop()
        height!: string;
        @Prop()
        width!: string;
        @Prop()
        position!: string;

        get getIconPath() {
            return require('cryptocurrency-icons/svg/color/' + this.currency.baseCurrency.toLowerCase() + '.svg')
        }
    }
</script>
