import { createWebHistory, createRouter } from "vue-router";

import GameFlow from "./views/GameFlow.vue";
import RecordFlow from "./views/RecordFlow.vue";

const routes = [
  { path: '/', component: GameFlow },
  {
    path: '/game/:id(\\d+)',
    component: RecordFlow,
    props: route => ({ id: Number(route.params.id) })
  },
]

export const router = createRouter({
  history: createWebHistory(),
  routes,
})