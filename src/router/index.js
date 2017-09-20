import Vue from 'vue';
import Router from 'vue-router';
import Psalm from '@/components/Psalm';
import Psalms from '@/components/Psalms';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Psalms',
      component: Psalms,
    },
    {
      path: '/psalm/:id',
      name: 'Psalm',
      component: Psalm,
    },
  ],
});
