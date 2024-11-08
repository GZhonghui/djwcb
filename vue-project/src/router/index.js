import { createRouter, createWebHistory } from 'vue-router';
import AllGames from '../views/AllGames.vue';
import GaMe1 from '../views/GaMe1.vue';
import GaMe2 from '../views/GaMe2.vue';
import GaMe3 from '../views/GaMe3.vue';
import GaMe4 from '../views/GaMe4.vue';
import GaMe5 from '../views/GaMe5.vue';
import GaMe6 from '../views/GaMe6.vue';
import GaMe7 from '../views/GaMe7.vue';
import GaMe8 from '../views/GaMe8.vue';
import GaMe9 from '../views/GaMe9.vue';
import GaMe10 from '../views/GaMe10.vue';
import GaMe11 from '../views/GaMe11.vue';
import GaMe12 from '../views/GaMe12.vue';
import GaMe13 from '../views/GaMe13.vue';
import GaMe14 from '../views/GaMe14.vue';
import GaMe15 from '../views/GaMe15.vue';
import GaMe16 from '../views/GaMe16.vue';
import GaMe17 from '../views/GaMe17.vue';
import GaMe18 from '../views/GaMe18.vue';
import GaMe19 from '../views/GaMe19.vue';
import GaMe20 from '../views/GaMe20.vue';
import GaMe21 from '../views/GaMe21.vue';
import GaMe22 from '../views/GaMe22.vue';
import GaMe23 from '../views/GaMe23.vue';
import GaMe24 from '../views/GaMe24.vue';
import GaMe25 from '../views/GaMe25.vue';
import GaMe26 from '../views/GaMe26.vue';
import GaMe27 from '../views/GaMe27.vue';
import GaMe28 from '../views/GaMe28.vue';
const routes = [
  {
    path: '/',
    name: 'AllGames',
    component: AllGames,
  },
{path: '/game1', name: 'GaMe1', component: GaMe1},
{path: '/game2', name: 'GaMe2', component: GaMe2},
{path: '/game3', name: 'GaMe3', component: GaMe3},
{path: '/game4', name: 'GaMe4', component: GaMe4},
{path: '/game5', name: 'GaMe5', component: GaMe5},
{path: '/game6', name: 'GaMe6', component: GaMe6},
{path: '/game7', name: 'GaMe7', component: GaMe7},
{path: '/game8', name: 'GaMe8', component: GaMe8},
{path: '/game9', name: 'GaMe9', component: GaMe9},
{path: '/game10', name: 'GaMe10', component: GaMe10},
{path: '/game11', name: 'GaMe11', component: GaMe11},
{path: '/game12', name: 'GaMe12', component: GaMe12},
{path: '/game13', name: 'GaMe13', component: GaMe13},
{path: '/game14', name: 'GaMe14', component: GaMe14},
{path: '/game15', name: 'GaMe15', component: GaMe15},
{path: '/game16', name: 'GaMe16', component: GaMe16},
{path: '/game17', name: 'GaMe17', component: GaMe17},
{path: '/game18', name: 'GaMe18', component: GaMe18},
{path: '/game19', name: 'GaMe19', component: GaMe19},
{path: '/game20', name: 'GaMe20', component: GaMe20},
{path: '/game21', name: 'GaMe21', component: GaMe21},
{path: '/game22', name: 'GaMe22', component: GaMe22},
{path: '/game23', name: 'GaMe23', component: GaMe23},
{path: '/game24', name: 'GaMe24', component: GaMe24},
{path: '/game25', name: 'GaMe25', component: GaMe25},
{path: '/game26', name: 'GaMe26', component: GaMe26},
{path: '/game27', name: 'GaMe27', component: GaMe27},
{path: '/game28', name: 'GaMe28', component: GaMe28},
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
});

export default router;
