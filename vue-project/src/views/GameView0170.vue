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
"2024-09-01": "https://v.douyu.com/show/NVm0WK4ZYObvJeBP",
"2024-09-03": "https://v.douyu.com/show/85BAvqQK1nwvG4Lm",
"2024-09-04": "https://v.douyu.com/show/NVm0WK4zgAPvJeBP",
"2024-09-06": "https://v.douyu.com/show/XqeO74NAa1NWxywG",
"2024-09-07": "https://v.douyu.com/show/Aox276Y2O2NvVz8Z",
"2024-09-08": "https://v.douyu.com/show/NVm0WK4zoy0vJeBP",
"2024-09-10": "https://v.douyu.com/show/DrwnvzDZL6jMPNaX",
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
