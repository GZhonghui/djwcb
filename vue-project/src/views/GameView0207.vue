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
"2025-04-06": "https://v.douyu.com/show/mPyq7obA5zdv1gLY",
"2025-04-08": "https://v.douyu.com/show/Aox276Yn1Y8vVz8Z",
"2025-04-09": "https://v.douyu.com/show/0Q8mMY5XaPjM49Ad",
"2025-04-10": "https://v.douyu.com/show/1LDR7QRXNkBMJzx8",
"2025-04-11": "https://v.douyu.com/show/6Aw87OQXl3dWYGkg",
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
