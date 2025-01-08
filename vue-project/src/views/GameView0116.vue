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
"2023-08-19": "https://v.douyu.com/show/brN0MmxXXLO7pyxA",
"2023-08-20": "https://v.douyu.com/show/Kp1QM8AB15RWk4bj",
"2023-08-22": "https://v.douyu.com/show/2Bj8vGpky6V7Obnd",
"2023-08-23": "https://v.douyu.com/show/a4Jj7l8XRB67Dk01",
"2023-08-25": "https://v.douyu.com/show/worZv0ZXkpGMJBk3",
"2023-08-26": "https://v.douyu.com/show/yVY8Wwd5dmBvLOz9",
"2023-08-27": "https://v.douyu.com/show/ERALvE8B39aW1Vw0",
"2023-08-29": "https://v.douyu.com/show/a2JEMJnOeV2MNxml",
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
