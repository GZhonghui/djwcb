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
"2024-06-21[放羊]": "https://v.douyu.com/show/0Q8mMY506wjM49Ad",
"2024-06-22": "https://v.douyu.com/show/8KxjMdl8DYQMVLwb",
"2024-06-23": "https://v.douyu.com/show/yVY8WwDAzXPvLOz9",
"2024-06-25": "https://v.douyu.com/show/jwzOvp1Z91X7ZVRm",
"2024-06-26[放羊]": "https://v.douyu.com/show/qJgOWx52KbNvkVzL",
"2024-06-28": "https://v.douyu.com/show/0zZVvPQR9Vb7O4E2",
"2024-06-29": "https://v.douyu.com/show/wLjGvLrQKPpMmO90",
"2024-07-01": "https://v.douyu.com/show/LDBbMAKJQ0yvyJRP",
"2024-07-02": "https://v.douyu.com/show/brN0MmQODwOMpyxA",
"2024-07-04[老头环战老头]": "https://v.douyu.com/show/EO0XvNwNyDj7DrBd",
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
