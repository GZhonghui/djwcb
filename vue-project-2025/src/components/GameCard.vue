<script setup>

import { NCard } from 'naive-ui';
import { useRouter } from 'vue-router';

// 从父组件接收属性
const props = defineProps({
  id: { type: Number, required: true },
  title: { type: String, required: true },
  time: { type: String, required: true },
  days: { type: Number, required: true },
})

const router = useRouter();

function onClick() {
  // 跳转动态路由
  router.push(`/game/${props.id}`)
}

</script>

<template>
  <!-- 使用这些属性 -->
  <!-- width, height 设定固定尺寸 -->
  <n-card
    :title="props.title"
    hoverable
    style="width: 192px; height: 128px; cursor: pointer;"
    @click="onClick"
  >
    {{ props.time }} ({{ props.days }})
  </n-card>
</template>