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
"2025-04-01": "https://v.douyu.com/show/Aox276Ynnr2vVz8Z",
"2025-04-02": "https://v.douyu.com/show/DrwnvzD4LoQMPNaX",
"2025-04-04": "https://v.douyu.com/show/DO84vrRgzLYvedGr",
"2025-04-05": "https://v.douyu.com/show/yVmjvBgn2mR7qkNb",
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
