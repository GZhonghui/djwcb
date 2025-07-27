<script setup>
// Header.vue 头部组件
import { ref, computed } from 'vue';
import { useRouter, useRoute } from 'vue-router';
import {
  NButton,
} from 'naive-ui';

const router = useRouter();
const route = useRoute();

// 使用 router.path 来判断当前的路由
const isHome = computed(() => route.path === '/')

function onClickTitle() {
  if (isHome.value) {
    // window.scrollTo({ top: 0, behavior: 'smooth' })
    // 在路由之间跳转
    router.push('/')
    return
  }

  // 如果可以返回上一页，则返回上一页
  // window.history.length 是浏览器历史记录的长度（当前页面的历史）
  if (window.history.length > 1) {
    // window.scrollTo({ top: 0, behavior: 'smooth' })
    router.back()
  } else {
    router.push('/')
  }
}

function onClickLive() {
  window.open("https://douyu.com/93589", '_blank')
}

</script>

<template>
  <header class="header-bar">
    <h1 class="title" @click="onClickTitle">戴大哥 老年人活动汇总</h1>
    <div class="actions">
      <n-button type="primary" @click="onClickLive">直播间</n-button>
    </div>
  </header>
</template>

<style scoped>
/* scoped表示样式只作用于当前组件 */
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
  cursor: pointer; /* 鼠标悬停时显示手型光标 */
}

.actions {
  display: flex;
  align-items: center;
  gap: 12px;
}
</style>