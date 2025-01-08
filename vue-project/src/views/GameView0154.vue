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
"2024-05-14": "https://v.douyu.com/show/8pa9v5N8lj17VrqA",
"2024-05-15": "https://v.douyu.com/show/8pa9v5N8JR17VrqA",
"2024-05-17": "https://v.douyu.com/show/NVm0WKNEOjbMJeBP",
"2024-05-18": "https://v.douyu.com/show/85BAvq8ay81WG4Lm",
"2024-05-19": "https://v.douyu.com/show/JmbBMkgLpDQM40XA",
"2024-05-21": "https://v.douyu.com/show/a4Jj7lBPPG4WDk01",
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
