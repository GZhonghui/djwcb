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
"2024-08-09": "https://v.douyu.com/show/85BAvqQmNpRvG4Lm",
"2024-08-10": "https://v.douyu.com/show/ERALvEq9GXbv1Vw0",
"2024-08-11": "https://v.douyu.com/show/Qyz171l5kpQvBJj9",
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
