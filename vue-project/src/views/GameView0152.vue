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
"2024-05-07": "https://v.douyu.com/show/8pa9v5NgdA17VrqA",
"2024-05-08": "https://v.douyu.com/show/Kg1VWR8ZrwN7GbNA",
"2024-05-12": "https://v.douyu.com/show/2V0JMVGzV35WRY5k",
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
