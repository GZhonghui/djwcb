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
"2024-02-03": "https://v.douyu.com/show/worZv0ZlPJ2MJBk3",
"2024-02-04": "https://v.douyu.com/show/yVY8WwdzNyVvLOz9",
"2024-02-06": "https://v.douyu.com/show/8pa9v5NVLQP7VrqA",
"2024-02-07": "https://v.douyu.com/show/85BAvq8NBgyWG4Lm",
"2024-02-11": "https://v.douyu.com/show/X3JzMaQL3GVMPQro",
"2024-02-12": "https://v.douyu.com/show/ERALvE8LlGaW1Vw0",
"2024-02-13": "https://v.douyu.com/show/X3JzMaQLl0YMPQro",
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
