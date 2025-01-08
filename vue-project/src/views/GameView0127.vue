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
"2023-12-14": "https://v.douyu.com/show/Qyz171DY6RJvBJj9",
"2023-12-16": "https://v.douyu.com/show/a2JEMJn8RDkMNxml",
"2023-12-24": "https://v.douyu.com/show/yVY8WwdeKwVvLOz9",
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
