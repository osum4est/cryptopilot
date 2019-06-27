import Vue from 'vue';
import Router from 'vue-router';
import Dashboard from '@/views/Dashboard.vue';
import AutoTraders from '@/views/AutoTraders.vue';
import CandleData from '@/views/CandleData.vue';
import PageNotFound from '@/views/PageNotFound.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      redirect: '/dashboard',
    },
    {
      path: '/dashboard',
      name: 'dashboard',
      component: Dashboard,
    },
    {
      path: '/auto_traders',
      name: 'auto_traders',
      component: AutoTraders,
    },
    {
      path: '/candle_data',
      name: 'candle_data',
      component: CandleData,
    },
    {
      path: '*',
      name: 'page_not_found',
      component: PageNotFound,
    },
  ],
});
