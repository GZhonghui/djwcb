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
"2023-01-16": "https://v.douyu.com/show/yVmjvBbmy4zvqkNb",
"2023-01-20": "https://v.douyu.com/show/qJgOWxZ0BVn7kVzL",
"2023-02-21[水友活动]": "https://v.douyu.com/show/XqeO74A09ayMxywG",
"2023-05-09[团建]": "https://v.douyu.com/show/8KxjMd4NzAmMVLwb",
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
