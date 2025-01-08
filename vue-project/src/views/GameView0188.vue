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
"2024-11-29[硬核模式]": "https://v.douyu.com/show/4xq3WDzEaER7LGNz",
"2024-12-04[硬核模式]": "https://v.douyu.com/show/8pa9v5e3p25vVrqA",
"2024-12-08[硬核模式]": "https://v.douyu.com/show/brN0MmQag9QMpyxA",
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
