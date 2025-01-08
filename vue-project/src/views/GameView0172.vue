<template>
  <div class="app-container">
    <div class="buttons-container">
      <button
        v-for="(link, text) in links"
        :key="text"
        @click="go(link)"
        class="button"
      >
        {{ text }}
      </button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      links: {
"2024-09-11": "https://v.douyu.com/show/0Q8mMY59VkJM49Ad",
"2024-09-13": "https://v.douyu.com/show/GnzXvbP9bZwM462l",
"2024-09-15": "https://v.douyu.com/show/NbwE7ZYJrRpvn5Zz",
"2024-09-16": "https://v.douyu.com/show/worZv0YZpEG7JBk3",
"2024-09-18": "https://v.douyu.com/show/NVm0WK4NznQvJeBP",
"2024-09-19": "https://v.douyu.com/show/JmbBMkogRZZM40XA",
"2024-09-20": "https://v.douyu.com/show/LDBbMAKNEnnvyJRP",
"2024-09-21": "https://v.douyu.com/show/mPyq7ob8Ezjv1gLY",
"2024-09-22": "https://v.douyu.com/show/8pa9v5eNmXKvVrqA",
"2024-09-24": "https://v.douyu.com/show/n8GzMXQ8ZaxW6qyP",
"2024-09-25": "https://v.douyu.com/show/85BAvqQ8k3KvG4Lm",
      }
    };
  },
  methods: {
    go(link) {
      if (link) if (link.startsWith('/')) {
        this.$router.push(link);
      } else {
        window.open(link, '_blank'); // window.location.href = link;
      }
    }
  }
};
</script>

<style scoped>
@import "@/styles/common.css";
</style>
