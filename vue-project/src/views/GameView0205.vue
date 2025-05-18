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
"2025-03-24": "https://v.douyu.com/show/DrwnvzD4jRKMPNaX",
"2025-03-25": "https://v.douyu.com/show/ERALvEqzN1xv1Vw0",
"2025-03-26": "https://v.douyu.com/show/Bjq4MexGZJG75Ea8",
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
