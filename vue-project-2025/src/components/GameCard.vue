<script setup>

import { NCard } from 'naive-ui';

const props = defineProps({
  title: { type: String, required: true },
  time: { type: String, required: true },
  days: { type: Number, required: true },
})

</script>

<template>
  <n-card :title="props.title" hoverable style="width: 256px; height: 128px;">
    {{ props.time }} ({{ props.days }})
  </n-card>
</template>