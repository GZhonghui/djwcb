// 程序入口

import { createApp } from 'vue' // vue
import { createPinia } from 'pinia' // pinia 状态管理
import { router } from './router.js' // 这个文件是自己定义的路由配置
import App from './App.vue' // App.vue 是主页面组件
import { useStaticDataStore } from './logic.js' // 处理数据

async function bootstrap() {
  // 创建 Vue 应用实例
  const app = createApp(App)

  // 使用 Pinia 状态管理
  // 也要创建 Pinia 实例并注册到 Vue 应用中
  const pinia = createPinia()
  app.use(pinia)
  // 使用自定义路由
  app.use(router)

  // 先挂载页面，再异步加载数据，确保首次进入可见 loading 状态
  app.mount('#app')

  // 异步初始化数据
  const store = useStaticDataStore(pinia)
  await store.init()
}

bootstrap()