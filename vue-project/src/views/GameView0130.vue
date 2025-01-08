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
"2024-01-10": "https://v.douyu.com/show/X3JzMaQPa6VMPQro",
"2024-01-12": "https://v.douyu.com/show/8KxjMdGmjOg7VLwb",
"2024-01-13": "https://v.douyu.com/show/LDBbMAN6K0EWyJRP",
"2024-01-14": "https://v.douyu.com/show/JmbBMkg3kXNM40XA",
"2024-01-16": "https://v.douyu.com/show/DrwnvzgQLPn7PNaX",
"2024-01-17[结局]": "https://v.douyu.com/show/DrwnvzgQrAO7PNaX",
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
