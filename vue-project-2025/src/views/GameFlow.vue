<script setup>

import { NFlex, NPagination } from 'naive-ui';

import GameCard from '@/components/GameCard.vue';
import { ref, computed, watch } from 'vue';
import { storeToRefs } from 'pinia';
import { useStaticDataStore } from '@/logic';
import { useRoute, useRouter } from 'vue-router'

const route = useRoute()
const router = useRouter()

// 引入 pinia 的全局数据
const store = useStaticDataStore()
const { data, isReady, loading, error } = storeToRefs(store)

// 确保数据已准备好
// data 是一个 ref，所以需要用 data.value 来访问实际数据
const games = computed(() => (data.value ? data.value.games : []))

// || 表示：前者有则用前者，否则用后者
// route.query是路由的查询参数（?后面的参数）
// 例如：/game?page=2&pageSize=48
// 这里的page和pageSize是可选的，如果没有则使用默认值
// AI：从 URL query 里恢复
const page = ref(Number(route.query.page) || 1)
const pageSize = ref(Number(route.query.pageSize) || 48)

// computed 是 Vue 的响应式计算属性
const pageCount = computed(() =>
  Math.ceil(games.value.length / pageSize.value || 1)
)

const pagedGames = computed(() => {
  const start = (page.value - 1) * pageSize.value
  return games.value.slice(start, start + pageSize.value)
})

function onPageSizeChange(size) {
  pageSize.value = size
  page.value = 1
}

// 监听 page 和 pageSize 的变化，更新路由的查询参数
// page 和 pageSize 来自url的查询参数
// AI：当页码/每页条数改变时，写回 URL（用 replace，避免污染历史栈）
watch([page, pageSize], ([p, ps]) => {
  router.replace({
    query: {
      ...route.query,
      page: String(p),
      pageSize: String(ps)
    }
  })
})

// 不理解这是在干啥
// AI：当路由变化（回退/前进）时，同步回本地状态
watch(
  () => route.query,
  (q) => {
    const p = Number(q.page) || 1
    const ps = Number(q.pageSize) || 48
    if (p !== page.value) page.value = p
    if (ps !== pageSize.value) pageSize.value = ps
  }
)
</script>

<template>
  <div id="root">
    <n-flex justify="center" wrap>
      <GameCard
        v-for="g in pagedGames"
        :key="g.id"
        :id="g.id"
        :title="g.title"
        :time="g.time"
        :days="g.days"
      />
    </n-flex>

    <!-- 分页组件 -->
    <n-flex justify="center" style="margin:32px;">
      <n-pagination
        v-model:page="page"
        :page-size="pageSize"
        :page-count="pageCount"
        show-size-picker
        :page-sizes="[48, 96]"
        @update:page-size="onPageSizeChange"
      />
    </n-flex>
  </div>
</template>

<style scoped>
#root {
  padding: 8px;
}
</style>