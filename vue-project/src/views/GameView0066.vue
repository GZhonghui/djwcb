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
"2022-11-21": "",
"2022-11-13": "https://v.douyu.com/show/2Bj8vGEXg6yMObnd",
"2022-11-14": "https://v.douyu.com/show/Kg1VWR4AEGm7GbNA",
"2022-11-15": "https://v.douyu.com/show/worZv0bNz4lMJBk3",
"2022-11-16": "https://v.douyu.com/show/Aox27629B007Vz8Z",
"2022-11-22": "https://v.douyu.com/show/kDe0W2mQ48RMA4Bz",
"2022-11-24": "https://v.douyu.com/show/0zZVvP9Gnmq7O4E2",
"2022-11-25": "https://v.douyu.com/show/n8GzMXmzE2rW6qyP",
"2022-11-26": "https://v.douyu.com/show/Aox2762QJ5x7Vz8Z",
"2022-11-27": "https://v.douyu.com/show/yVmjvBbDPyRvqkNb",
"2022-11-28": "https://v.douyu.com/show/brN0Mm4z2yQ7pyxA",
"2022-11-29": "https://v.douyu.com/show/8pa9v5PoNapWVrqA",
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
