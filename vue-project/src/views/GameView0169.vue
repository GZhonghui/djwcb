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
"2024-08-20[发售日放羊]": "https://v.douyu.com/show/yVmjvBgDkgz7qkNb",
"2024-08-21[放羊]": "https://v.douyu.com/show/6Aw87OQ6NdxWYGkg",
"2024-08-22": "https://v.douyu.com/show/X3JzMalVaXA7PQro",
"2024-08-23": "https://v.douyu.com/show/DrwnvzDKyaKMPNaX",
"2024-08-24": "https://v.douyu.com/show/6Aw87OQZl1jWYGkg",
"2024-08-25": "https://v.douyu.com/show/8KxjMdlkGyYMVLwb",
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
