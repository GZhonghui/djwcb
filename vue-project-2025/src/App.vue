<script setup>

import { ref, onMounted } from 'vue';
import Header from './components/Header.vue';

</script>

<template>
  <div class="page">
    <Header />
    <RouterView />
  </div>
</template>

<style scoped>
.page {
  font-family: sans-serif;
  margin: 0;
}
</style>