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
"2024-12-13": "https://v.douyu.com/show/r90XWgo9nPgWgk25",
"2024-12-14": "https://v.douyu.com/show/XqeO74NVyweWxywG",
"2024-12-15": "https://v.douyu.com/show/0Q8mMY5ROe5M49Ad",
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
