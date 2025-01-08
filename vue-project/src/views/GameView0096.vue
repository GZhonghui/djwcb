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
"2023-04-18": "https://v.douyu.com/show/DrwnvzZnJAVvPNaX",
"2023-04-19": "https://v.douyu.com/show/n8GzMXmVA5rW6qyP",
"2023-08-09": "https://v.douyu.com/show/a4Jj7l8dZ6j7Dk01",
"2023-08-11": "https://v.douyu.com/show/X3JzMaQZxpeMPQro",
"2023-08-12": "https://v.douyu.com/show/ERALvE8jr4aW1Vw0",
"2023-08-15": "https://v.douyu.com/show/ERALvE8jdRnW1Vw0",
"2023-08-16": "https://v.douyu.com/show/wLjGvLxKnVavmO90",
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
