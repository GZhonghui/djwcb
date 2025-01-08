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
"2023-12-20": "https://v.douyu.com/show/4xq3WDB09Zb7LGNz",
"2023-12-22": "https://v.douyu.com/show/85BAvq8e0VXWG4Lm",
"2023-12-23": "https://v.douyu.com/show/LDBbMANYd4LWyJRP",
"2023-12-26": "https://v.douyu.com/show/yVY8WwdVwaVvLOz9",
"2023-12-27": "https://v.douyu.com/show/X3JzMaQwZRGMPQro",
"2023-12-29": "https://v.douyu.com/show/aRbBv3ABy9EM6PYV",
"2023-12-30": "https://v.douyu.com/show/X3JzMaQw0OLMPQro",
"2023-12-31": "https://v.douyu.com/show/yVY8WwdVzrzvLOz9",
"2024-01-02": "https://v.douyu.com/show/Yo4evyg4jodM8L62",
"2024-01-03": "https://v.douyu.com/show/Bjq4MelQjmx75Ea8",
"2024-01-04": "https://v.douyu.com/show/EO0XvNbyxBjvDrBd",
"2024-01-05": "https://v.douyu.com/show/8pa9v5NyXKK7VrqA",
"2024-01-06": "https://v.douyu.com/show/mPyq7o8NpADM1gLY",
"2024-01-07": "https://v.douyu.com/show/NbwE7Z84p6JWn5Zz",
"2024-01-09": "https://v.douyu.com/show/0zZVvPoyL4qWO4E2",
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
