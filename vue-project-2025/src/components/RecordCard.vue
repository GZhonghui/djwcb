<script setup>

import { NCard } from 'naive-ui';
import { useRouter } from 'vue-router';

// 从父组件接收属性
const props = defineProps({
  id: { type: Number, required: true },
  title: { type: String, required: true },
  comment: { type: String, required: true },
  url: { type: String, required: true },
})

function onClick() {
  if (!props.url) return

  // if (props.url.startsWith('/')) {
  //   router.push(props.url)
  // } else {
  //   window.open(props.url, '_blank')
  // }
  window.open(props.url, '_blank')
}

</script>

<template>
  <!-- 使用这些属性 -->
  <!-- :hoverable 根据 props.url 的存在与否来决定 -->
  <n-card
    :title="props.title"
    :hoverable="Boolean(props.url)"
    style="width: 192px; height: 128px; cursor: pointer;"
    @click="onClick"
  >
    {{ props.comment }}
  </n-card>
</template>