<script setup>
// Header.vue 头部组件
import { ref, computed } from 'vue';
import { useStaticDataStore } from '@/logic';
import { useRouter, useRoute } from 'vue-router';
import {
  NButton,
  NInput
} from 'naive-ui';

const router = useRouter();
const route = useRoute();

// 使用 router.path 来判断当前的路由
const isHome = computed(() => route.path === '/')
const showSearchInput = ref(false)
const isInputFocused = ref(false)
const searchQuery = ref('')
const store = useStaticDataStore()

function onClickTitle() {
  // 清空搜索关键字
  store.updateSearchStr('')

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

function onSearch() {
  store.updateSearchStr(searchQuery.value);
  searchQuery.value = '';
}
</script>

<template>
  <header 
    class="header-bar"
    @mouseenter="showSearchInput = true"
    @mouseleave="isInputFocused || (showSearchInput = false)"
  >
    <h1 class="title" @click="onClickTitle">戴大哥 老年人活动汇总</h1>
    <div class="actions">
      <!-- 搜索区域 -->
      <div class="search-container">
        <transition name="fade">
          <n-input
            v-if="showSearchInput"
            v-model:value="searchQuery"
            class="search-input"
            placeholder="请输入搜索内容"
            clearable
            @keyup.enter="onSearch"
            @focus="isInputFocused = true"
            @blur="showSearchInput = isInputFocused = false"
          />
        </transition>
        <n-button type="primary" @click="onSearch">搜索</n-button>
      </div>
      
      <n-button type="primary" @click="onClickLive">直播间</n-button>
    </div>
  </header>
</template>

<style scoped>
/* scoped表示样式只作用于当前组件 */
.header-bar {
  width: 100%;
  height: auto;
  margin-bottom: 16px;
  background: #000000;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  padding: 12px 24px;
  box-sizing: border-box;
  color: #fff;
  position: relative;
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

.search-container {
  display: flex;
  align-items: center;
  position: relative;
}

.search-input {
  width: 200px;
  margin-right: 8px;
  transition: all 0.3s ease;
}

/* 过渡动画效果 */
.fade-enter-active, .fade-leave-active {
  transition: opacity 0.3s, transform 0.3s;
}
.fade-enter-from, .fade-leave-to {
  opacity: 0;
  transform: translateX(-10px);
}
.fade-enter-to, .fade-leave-from {
  opacity: 1;
  transform: translateX(0);
}
</style>