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
"2023-01-25": "https://v.douyu.com/show/4xq3WDpYAZRWLGNz",
"2023-01-26[传奇！雨中种植物]": "https://v.douyu.com/show/0Q8mMY9DDgkM49Ad",
"2023-01-27": "https://v.douyu.com/show/yVY8Ww6n2AoMLOz9",
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
