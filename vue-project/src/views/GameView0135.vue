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
"2024-02-04": "https://v.douyu.com/show/yVY8WwdzNyVvLOz9",
"2024-03-22": "https://v.douyu.com/show/8pa9v5NGDpp7VrqA",
"2024-03-25": "https://v.douyu.com/show/a2JEMJnzb8oMNxml",
"2024-03-27": "https://v.douyu.com/show/DO84vr8qaLlMedGr",
"2024-04-01": "https://v.douyu.com/show/Kg1VWR8rgJm7GbNA",
"2024-04-02": "https://v.douyu.com/show/aRbBv3Ama5XM6PYV",
"2024-04-03": "https://v.douyu.com/show/qJgOWxgpoVeMkVzL",
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
