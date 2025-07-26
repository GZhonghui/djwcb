<script setup>

import { NCard } from 'naive-ui';
import { useRouter } from 'vue-router';

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
  <n-card
    :title="props.title"
    :hoverable="Boolean(props.url)"
    style="width: 192px; height: 128px; cursor: pointer;"
    @click="onClick"
  >
    {{ props.comment }}
  </n-card>
</template>