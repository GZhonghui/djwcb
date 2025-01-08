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
"2023-11-21": "https://v.douyu.com/show/2V0JMVG6BO4WRY5k",
"2023-11-22": "https://v.douyu.com/show/ERALvE8P95xW1Vw0",
"2023-11-26": "https://v.douyu.com/show/4xq3WDBDedj7LGNz",
"2023-11-27": "https://v.douyu.com/show/a2JEMJnmQeZMNxml",
"2023-11-28": "https://v.douyu.com/show/Yo4evygLrKXM8L62",
"2023-11-29": "https://v.douyu.com/show/brN0MmxZPQ07pyxA",
"2023-12-02": "https://v.douyu.com/show/kDe0W2DojXX7A4Bz",
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
