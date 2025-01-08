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
"2023-01-12": "https://v.douyu.com/show/brN0Mm4E8E37pyxA",
"2023-01-15": "https://v.douyu.com/show/0Q8mMY9NgxjM49Ad",
"2023-01-17": "https://v.douyu.com/show/a2JEMJbadlmMNxml",
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
