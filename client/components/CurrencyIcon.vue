<template>
  <v-img :src="getIconPath" :height="height" :width="width" contain></v-img>
</template>

<script lang="ts">
    import {Prop} from "vue-property-decorator";
    import Component from "vue-class-component";
    import Vue from "vue";

    @Component
    export default class CurrencyIcon extends Vue {
        @Prop()
        currency!: Any;
        @Prop()
        height!: string;
        @Prop()
        width!: string;

        get getIconPath() {
            return require('cryptocurrency-icons/svg/color/' + this.currency.base_currency.toLowerCase() + '.svg')
        }
    }
</script>
