<script setup>

import { ref, computed } from 'vue';
import { useRouter, useRoute } from 'vue-router';
import {
  NButton,
} from 'naive-ui';

const router = useRouter();
const route = useRoute();

const isHome = computed(() => route.path === '/')

function onClickTitle() {
  if (isHome.value) {
    // window.scrollTo({ top: 0, behavior: 'smooth' })
    router.push('/')
    return
  }

  if (window.history.length > 1) {
    // window.scrollTo({ top: 0, behavior: 'smooth' })
    router.back()
  } else {
    router.push('/')
  }
}

</script>

<template>
  <header class="header-bar">
    <h1 class="title" @click="onClickTitle">戴大哥 老年人回放（点我返回）</h1>
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
  cursor: pointer;
}

.actions {
  display: flex;
  align-items: center;
  gap: 12px;
}
</style>