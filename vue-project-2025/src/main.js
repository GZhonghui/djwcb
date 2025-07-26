import { createApp } from 'vue'
import { createPinia } from 'pinia'
import { router } from './router.js'
import App from './App.vue'
import { useStaticDataStore } from './logic.js'

async function bootstrap() {
  const app = createApp(App)

  const pinia = createPinia()
  app.use(pinia)
  app.use(router)

  const store = useStaticDataStore(pinia)
  await store.init()

  app.mount('#app')
}

bootstrap()