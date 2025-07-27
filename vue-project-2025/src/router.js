// 这个文件是 Vue Router 的配置文件

import { createWebHistory, createRouter } from "vue-router";

// 导入视图组件
import GameFlow from "./views/GameFlow.vue";
import RecordFlow from "./views/RecordFlow.vue";

// 定义路由规则
const routes = [
  // 普通路由
  { path: '/', component: GameFlow },
  // 动态路由，匹配游戏 ID
  // 比如：/game/123
  {
    path: '/game/:id(\\d+)', // 使用正则表达式匹配数字 ID
    component: RecordFlow, // 组件加载时会传入路由参数
    props: route => ({ id: Number(route.params.id) }) // 将路由参数转换为数字
  },
]

// 导出路由实例
export const router = createRouter({
  history: createWebHistory(), // 使用 HTML5 的 history 模式
  routes, // 路由规则
})