import { createWebHistory, createRouter } from "vue-router";

import GameFlow from "./views/GameFlow.vue";
import RecordFlow from "./views/RecordFlow.vue";

const routes = [
  { path: '/', component: GameFlow },
  { path: '/game', component: RecordFlow },
]

export const router = createRouter({
  history: createWebHistory(),
  routes,
})