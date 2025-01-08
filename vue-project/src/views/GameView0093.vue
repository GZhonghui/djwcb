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
"2023-03-27": "https://v.douyu.com/show/Bjq4MerqAXxW5Ea8",
"2023-03-28": "https://v.douyu.com/show/JmbBMk943kQv40XA",
"2023-03-30": "https://v.douyu.com/show/qJgOWxZV2ol7kVzL",
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
