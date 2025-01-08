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
"2023-04-04": "https://v.douyu.com/show/NbwE7ZJmj0k7n5Zz",
"2023-04-11": "https://v.douyu.com/show/8pa9v5PGROaWVrqA",
"2023-04-18": "https://v.douyu.com/show/DrwnvzZnJAVvPNaX",
"2023-05-02": "https://v.douyu.com/show/XqeO74A5LPPMxywG",
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
