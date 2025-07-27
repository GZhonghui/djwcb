<script setup>

import { ref, onMounted } from 'vue';
import Header from './components/Header.vue';

</script>

<template>
  <!-- App.vue 主页面 -->
  <div class="page">
    <!-- 自己定义的头部组件 -->
    <Header />
    <!-- （在router中）url绑定的组件会显示（更新）在这里 -->
    <RouterView />
  </div>
</template>

<style scoped>
.page {
  font-family: sans-serif;
  margin: 0;
}
</style>