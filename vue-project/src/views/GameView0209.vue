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
"2025-05-03": "https://v.douyu.com/show/brN0MmQpoNZMpyxA",
"2025-05-04": "https://v.douyu.com/show/85BAvqQpZwbvG4Lm",
"2025-05-05": "https://v.douyu.com/show/3rob7jopLJZMgkZl",
"2025-05-06": "https://v.douyu.com/show/8pa9v5eKanlvVrqA",
"2025-05-07": "https://v.douyu.com/show/ZB5Kv9gK6emMa93x",
"2025-05-09": "https://v.douyu.com/show/X3JzMalpr9L7PQro",
"2025-05-10": "https://v.douyu.com/show/XqeO74NKJNXWxywG",
"2025-05-11": "https://v.douyu.com/show/GnzXvbPpB8eM462l",
"2025-05-13": "https://v.douyu.com/show/qJgOWx5L2VKvkVzL",
"2025-05-14": "https://v.douyu.com/show/NVm0WK48jlBvJeBP",
"2025-05-16": "https://v.douyu.com/show/3rob7joLo0jMgkZl",
"2025-05-17": "https://v.douyu.com/show/brN0MmQLgV0MpyxA",
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
