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
"2023-01-11": "https://v.douyu.com/show/DrwnvzZYLjQvPNaX",
"2023-01-12": "https://v.douyu.com/show/brN0Mm4E8E37pyxA",
"2023-01-13": "https://v.douyu.com/show/EO0XvN325587DrBd",
"2023-01-17": "https://v.douyu.com/show/a2JEMJbadlmMNxml",
"2023-01-24": "https://v.douyu.com/show/Qyz171Z2zpbMBJj9",
"2023-02-05": "https://v.douyu.com/show/3rob7jOAeZbMgkZl",
"2023-02-14": "https://v.douyu.com/show/Kg1VWR468BP7GbNA",
"2023-02-15": "https://v.douyu.com/show/1LDR7QJ6XAVMJzx8",
"2023-02-22": "https://v.douyu.com/show/1LDR7QJALoBMJzx8",
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
