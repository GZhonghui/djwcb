<script setup>

import { ref } from 'vue';
import { useRouter } from 'vue-router';
import {
  NButton,
} from 'naive-ui';

</script>

<template>
  <header class="header-bar">
    <h1 class="title">戴大哥 老年人回放</h1>
    <div class="actions">
      <n-button type="primary">直播间</n-button>
    </div>
  </header>
</template>

<style scoped>
.header-bar {
  width: 100%;
  height: 64px;
  margin-bottom: 16px;
  background: #000000;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 24px;
  box-sizing: border-box;
  color: #fff;
}

.title {
  margin: 0;
  font-size: 24px;
}

.actions {
  display: flex;
  align-items: center;
  gap: 12px;
}
</style>