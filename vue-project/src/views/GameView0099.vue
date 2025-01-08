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
"2023-05-25[伏笔换俯卧撑]": "https://v.douyu.com/show/Aox276Dg5pKWVz8Z",
"2023-05-26[伏笔换俯卧撑]": "https://v.douyu.com/show/8pa9v5NOx9D7VrqA",
"2023-05-27": "https://v.douyu.com/show/yVmjvBpZ1KdMqkNb",
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
