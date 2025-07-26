<script setup>

import { NFlex, NPagination } from 'naive-ui';

import GameCard from '@/components/GameCard.vue';
import { ref, computed, watch } from 'vue';
import { storeToRefs } from 'pinia';
import { useStaticDataStore } from '@/logic';
import { useRoute, useRouter } from 'vue-router'

const route = useRoute()
const router = useRouter()

const store = useStaticDataStore()
const { data, isReady, loading, error } = storeToRefs(store)

const games = computed(() => (data.value ? data.value.games : []))

const page = ref(Number(route.query.page) || 1)
const pageSize = ref(Number(route.query.pageSize) || 48)

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

watch([page, pageSize], ([p, ps]) => {
  router.replace({
    query: {
      ...route.query,
      page: String(p),
      pageSize: String(ps)
    }
  })
})

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