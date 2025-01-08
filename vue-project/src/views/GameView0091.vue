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
"2023-02-24": "https://v.douyu.com/show/NVm0WKzOoV8MJeBP",
"2023-02-25": "https://v.douyu.com/show/2V0JMVV2g2DMRY5k",
"2023-03-03": "https://v.douyu.com/show/r90XWgq8zkK7gk25",
"2023-03-04": "https://v.douyu.com/show/aRbBv3Pg3jD76PYV",
"2023-03-07": "https://v.douyu.com/show/r90XWgqlXOw7gk25",
"2023-03-14": "https://v.douyu.com/show/Kg1VWR40Q0L7GbNA",
"2023-03-15": "https://v.douyu.com/show/2Bj8vGE2rdLMObnd",
"2023-03-16": "https://v.douyu.com/show/DO84vrKyLAl7edGr",
"2023-03-18": "https://v.douyu.com/show/Aox2762LPA27Vz8Z",
"2023-03-21": "https://v.douyu.com/show/85BAvqKNb3BMG4Lm",
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
