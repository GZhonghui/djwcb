<script setup>

import { NFlex } from 'naive-ui';

import GameCard from '@/components/GameCard.vue';
import { ref } from 'vue';

const games = ref([
  {
    id: 1,
    title: "动物迷城",
    time: "2025/07",
    days: 10,
  },
])

</script>

<template>
  <div id="root">
    <n-flex justify="center">
      <GameCard
        v-for="g in games"
        :key="g.id"
        :title="g.title"
        :time="g.time"
        :days="g.days"
      />
    </n-flex>
  </div>
</template>

<style scoped>
#root {
  padding: 8px;
}
</style>