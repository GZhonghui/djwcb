<script setup>

// @在导入路径中表示：src目录
import RecordCard from '@/components/RecordCard.vue'
import { storeToRefs } from 'pinia'
import { useStaticDataStore } from '@/logic' // js文件直接省略了js后缀
import { onMounted, ref, watch, computed } from 'vue'
import { NFlex } from 'naive-ui'

// 从动态路由中获取参数
const props = defineProps({
  id: Number
})

// 获取静态数据存储
const store = useStaticDataStore()
// 从store中获取数据和状态
const { data, isReady, loading, error } = storeToRefs(store)

// 转换为可用的数据字典
const recordsDict = computed(() => (data.value ? data.value.records : {}))

const gameName = ref("")
const records = ref([])

function fetchGame(id) {
  gameName.value = `game_${id}`
  let recordList = recordsDict.value[id]
  records.value = recordList
}

onMounted(() => fetchGame(props.id))

// 监听props.id的变化，重新获取数据
// 当 id 变化的时候，这个 view 可能不会重新加载，所以不能用 onMounted
// 需要手动监听 id 的变化
watch(() => props.id, (newId) => {
  fetchGame(newId)
})
</script>

<template>
  <div id="root">
    <!-- naive-ui提供的布局组件 -->
    <n-flex justify="center" wrap>
      <!-- 使用 vue 的for循环动态渲染记录卡片 -->
      <!-- :key 是必须的，用于标识每个组件的唯一性 -->
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