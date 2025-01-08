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
"2024-11-12": "https://v.douyu.com/show/EO0XvNwgleX7DrBd",
"2024-11-13": "https://v.douyu.com/show/2V0JMVQAw157RY5k",
"2024-11-15": "https://v.douyu.com/show/3rob7joGnmbMgkZl",
"2024-11-16[全解锁存档]": "https://v.douyu.com/show/Bjq4MexaQyq75Ea8",
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
