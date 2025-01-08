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
"2023-12-09": "https://v.douyu.com/show/mPyq7o8q9mpM1gLY",
"2023-12-10": "https://v.douyu.com/show/NbwE7Z8nYPRWn5Zz",
"2023-12-15": "https://v.douyu.com/show/aRbBv3AjnNYM6PYV",
"2023-12-17": "https://v.douyu.com/show/a2JEMJn3jPnMNxml",
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
