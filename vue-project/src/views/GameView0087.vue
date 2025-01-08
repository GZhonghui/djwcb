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
"2023-01-28": "https://v.douyu.com/show/8pa9v5PmNyqWVrqA",
"2023-01-30": "https://v.douyu.com/show/XqeO74AR02nMxywG",
"2023-02-01": "https://v.douyu.com/show/jwzOvpGDoxDWZVRm",
"2023-02-03": "https://v.douyu.com/show/aRbBv3PyA6m76PYV",
"2023-02-04": "https://v.douyu.com/show/X3JzMaOAzDGvPQro",
"2023-02-05": "https://v.douyu.com/show/3rob7jOAeZbMgkZl",
"2023-02-07": "https://v.douyu.com/show/DrwnvzZVKYovPNaX",
"2023-02-08": "https://v.douyu.com/show/6Aw87OOXb0j7YGkg",
"2023-02-09": "https://v.douyu.com/show/2Bj8vGEYPnQMObnd",
"2023-02-12": "https://v.douyu.com/show/X3JzMaOp65LvPQro",
"2023-03-02": "https://v.douyu.com/show/yVmjvBbybpdvqkNb",
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
