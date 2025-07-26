<script setup>

import RecordCard from '@/components/RecordCard.vue'
import { storeToRefs } from 'pinia'
import { useStaticDataStore } from '@/logic'
import { onMounted, ref, watch, computed } from 'vue'
import { NFlex } from 'naive-ui'

const props = defineProps({
  id: Number
})

const store = useStaticDataStore()
const { data, isReady, loading, error } = storeToRefs(store)

const recordsDict = computed(() => (data.value ? data.value.records : {}))

const gameName = ref("")
const records = ref([])

function fetchGame(id) {
  gameName.value = `game_${id}`
  let recordList = recordsDict.value[id]
  records.value = recordList
}

onMounted(() => fetchGame(props.id))

watch(() => props.id, (newId) => {
  fetchGame(newId)
})
</script>

<template>
  <div id="root">
    <n-flex justify="center" wrap>
      <RecordCard
        v-for="g in records"
        :key="g.id"
        :id="g.id"
        :title="g.title"
        :comment="g.comment"
        :url="g.url"
      />
    </n-flex>
  </div>
</template>

<style scoped>
#root {
  padding: 8px;
}
</style>