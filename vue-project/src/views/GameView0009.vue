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
"2020-01-26": "https://v.douyu.com/show/85BAvqx5kPyWG4Lm",
"2020-02-01": "https://v.douyu.com/show/3rob7j2r9Zp7gkZl",
"2020-03-09": "https://v.douyu.com/show/brN0MmO6akbvpyxA",
"2020-01-25[第一次]": "",
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
