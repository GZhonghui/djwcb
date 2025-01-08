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
"2024-04-20": "https://v.douyu.com/show/Aox276DPwDmWVz8Z",
"2024-04-21": "https://v.douyu.com/show/wLjGvLxn0VRvmO90",
"2024-04-23": "https://v.douyu.com/show/85BAvq8X0rKWG4Lm",
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
