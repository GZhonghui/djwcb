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
"2024-08-16": "https://v.douyu.com/show/a2JEMJJGrQ0MNxml",
"2024-08-17": "https://v.douyu.com/show/4xq3WDzwqwN7LGNz",
"2024-08-18": "https://v.douyu.com/show/DO84vrRrggGvedGr",
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
