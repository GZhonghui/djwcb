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
"2023-10-27": "https://v.douyu.com/show/ERALvE80GAjW1Vw0",
"2023-10-28": "https://v.douyu.com/show/X3JzMaQAKDNMPQro",
"2023-10-29": "https://v.douyu.com/show/Kg1VWR8DO8x7GbNA",
"2023-11-01": "https://v.douyu.com/show/brN0Mmx6wkr7pyxA",
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
