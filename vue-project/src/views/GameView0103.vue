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
"2023-06-18": "https://v.douyu.com/show/EO0XvNbz0OjvDrBd",
"2023-06-20": "https://v.douyu.com/show/GnzXvbQOwdwW462l",
"2023-06-21": "https://v.douyu.com/show/2V0JMVGbGwEWRY5k",
"2023-06-23": "https://v.douyu.com/show/aRbBv3ARQxbM6PYV",
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
