<template>
  <v-container>
    <v-layout row wrap>

      <v-flex xs12>
        <v-layout row align-space-between justify-space-between>

          <v-flex grow>
            <v-layout column align-space-between justify-space-between>

              <v-flex shrink>
                <v-layout row align-space-between>

                  <v-flex mr-0 pr-0 shrink>
                    <span class="display-2">{{ currencyData.currency.name }}</span>
                    <br/>
                    <span class="subheading font-weight-light">{{ currencyData.currency.currency_id }}</span>
                  </v-flex>

                  <v-flex ml-0 pl-0 grow>
                    <div class="div-fill-sizer">
                      <!-- Sometimes right side of icon gets slightly cut off, so width/height need to be 99% -->
                      <currency-icon id="currency_icon" :currency="currencyData.currency" position="right"
                                     width="99%" height="99%"></currency-icon>
                    </div>
                  </v-flex>

                </v-layout>
              </v-flex>

              <v-flex>
                <v-layout row>

                  <v-flex shrink>
                    <v-layout column>

                      <v-flex shrink>
                        <v-layout row>
                          <v-flex pb-0 pr-0>
                            <span class="caption font-weight-light text-uppercase">Current</span>
                          </v-flex>
                          <v-flex pb-0 pl-0 text-xs-right style="color: lawngreen">
                            <span class="caption font-weight-thin">▲</span>
                            <span class="body-1">15%</span>
                          </v-flex>
                        </v-layout>
                      </v-flex>

                      <v-flex pt-1 shrink>
                        <span class="display-1">$1920.92</span>
                      </v-flex>

                    </v-layout>
                  </v-flex>

                </v-layout>
              </v-flex>

            </v-layout>
          </v-flex>

        </v-layout>
      </v-flex>

      <v-flex xs4 pb-0>
        <span class="caption font-weight-light text-uppercase">1st Rec. Price</span>
      </v-flex>

      <v-flex xs4 pb-0>
        <span class="caption font-weight-light text-uppercase">Min</span>
      </v-flex>

      <v-flex xs4 pb-0>
        <span class="caption font-weight-light text-uppercase">Max</span>
      </v-flex>

      <v-flex xs4 pt-1>
        <span class="title">6/14/19</span>
      </v-flex>

      <v-flex xs4 pt-1>
        <span class="title">$740.29</span>
      </v-flex>

      <v-flex xs4 pt-1>
        <span class="title">$1740.29</span>
      </v-flex>

    </v-layout>
  </v-container>
</template>

<script lang="ts">
    import Vue from "vue";
    import Component from "vue-class-component";
    import {Prop} from "vue-property-decorator";
    import CurrencyIcon from "@/components/CurrencyIcon.vue";

    @Component({
        components: {CurrencyIcon}
    })
    export default class CurrencyCard extends Vue {
        @Prop()
        currencyData!: CurrencyData;
    }
</script>
