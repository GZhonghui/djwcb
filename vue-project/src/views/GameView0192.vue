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
"2024-12-17": "https://v.douyu.com/show/2V0JMVQ8mja7RY5k",
"2024-12-18": "https://v.douyu.com/show/85BAvqQ2amyvG4Lm",
"2024-12-20": "https://v.douyu.com/show/Qyz171ljgy0vBJj9",
"2024-12-21": "https://v.douyu.com/show/1LDR7QRYlOOMJzx8",
"2024-12-22": "https://v.douyu.com/show/yVY8WwDbDOPvLOz9",
"2024-12-24[放羊]": "https://v.douyu.com/show/0zZVvPQgg0Y7O4E2",
"2024-12-25": "https://v.douyu.com/show/EO0XvNwlaLB7DrBd",
"2024-12-27": "https://v.douyu.com/show/aRbBv3Yx1EgM6PYV",
"2024-12-28": "https://v.douyu.com/show/aRbBv3YxkaXM6PYV",
"2024-12-29": "https://v.douyu.com/show/a2JEMJJ6VpnMNxml",
"2024-12-31": "https://v.douyu.com/show/n8GzMXQdPKJW6qyP",
"2025-01-01": "https://v.douyu.com/show/NVm0WK4lwpwvJeBP",
"2025-01-03": "https://v.douyu.com/show/Kp1QM8YDpg3Wk4bj",
"2025-01-04": "https://v.douyu.com/show/Bjq4MexEJEG75Ea8",
"2025-01-05": "https://v.douyu.com/show/brN0MmQEx6OMpyxA",
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
