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
"2024-11-29[月末放羊]": "https://v.douyu.com/show/4xq3WDzEaER7LGNz",
"2024-11-30": "https://v.douyu.com/show/a2JEMJJOQoZMNxml",
"2024-12-01": "https://v.douyu.com/show/worZv0YXxNp7JBk3",
"2024-12-03": "https://v.douyu.com/show/NVm0WK49wrQvJeBP",
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
