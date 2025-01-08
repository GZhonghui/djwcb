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
"2024-03-09": "https://v.douyu.com/show/DrwnvzgxQ6l7PNaX",
"2024-03-10": "https://v.douyu.com/show/a2JEMJn1dVYMNxml",
"2024-03-12": "https://v.douyu.com/show/1LDR7QZrpZgMJzx8",
"2024-03-13": "https://v.douyu.com/show/jNBdvn8yVXJME2yw",
"2024-03-15": "https://v.douyu.com/show/a2JEMJnqKmkMNxml",
"2024-03-16": "https://v.douyu.com/show/n8GzMX82dKAM6qyP",
"2024-03-17": "https://v.douyu.com/show/4xq3WDBGYwN7LGNz",
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
