// vue-project/src/router/index.js

import { createRouter, createWebHistory } from 'vue-router';
import AllGames from '../views/AllGames.vue';

const routes = [
  {
    path: '/',
    name: 'AllGames',
    component: AllGames,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
});

export default router;