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
"2024-02-23": "https://v.douyu.com/show/XqeO74DdNNQ7xywG",
"2024-02-24": "https://v.douyu.com/show/n8GzMX8JA5DM6qyP",
"2024-02-25": "https://v.douyu.com/show/Aox276Dd8ELWVz8Z",
"2024-02-27": "https://v.douyu.com/show/aRbBv3AdkGoM6PYV",
"2024-02-28": "https://v.douyu.com/show/a4Jj7l80Y5D7Dk01",
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
