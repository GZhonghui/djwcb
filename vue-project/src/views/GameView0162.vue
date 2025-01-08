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
"2024-07-09": "https://v.douyu.com/show/2Bj8vG3XmeVvObnd",
"2024-07-10": "https://v.douyu.com/show/wLjGvLr5qxRMmO90",
"2024-07-12": "https://v.douyu.com/show/mPyq7obQD5Qv1gLY",
"2024-07-13": "https://v.douyu.com/show/85BAvqQ9noXvG4Lm",
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
