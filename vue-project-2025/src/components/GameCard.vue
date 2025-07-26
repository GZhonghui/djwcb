<script setup>

import { NCard } from 'naive-ui';
import { useRouter } from 'vue-router';

const props = defineProps({
  id: { type: Number, required: true },
  title: { type: String, required: true },
  time: { type: String, required: true },
  days: { type: Number, required: true },
})

const router = useRouter();

function onClick() {
  router.push(`/game/${props.id}`)
}

</script>

<template>
  <n-card
    :title="props.title"
    hoverable
    style="width: 192px; height: 128px; cursor: pointer;"
    @click="onClick"
  >
    {{ props.time }} ({{ props.days }})
  </n-card>
</template>