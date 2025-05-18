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
"2025-01-20": "https://v.douyu.com/show/DrwnvzDBZoOMPNaX",
"2025-01-21": "https://v.douyu.com/show/ERALvEqJXmZv1Vw0",
"2025-01-22": "https://v.douyu.com/show/LDBbMAKVE2yvyJRP",
"2025-01-24": "https://v.douyu.com/show/Kp1QM8Yokw6Wk4bj",
"2025-01-25": "https://v.douyu.com/show/Kg1VWRQNDjNMGbNA",
"2025-01-26": "https://v.douyu.com/show/qJgOWx5BLmlvkVzL",
"2025-01-29": "https://v.douyu.com/show/kDe0W2gJ6aRvA4Bz",
"2025-01-30": "https://v.douyu.com/show/a4Jj7lB4Y36WDk01",
"2025-01-31": "https://v.douyu.com/show/DO84vrRmXkYvedGr",
"2025-02-01": "https://v.douyu.com/show/Kg1VWRQNkPQMGbNA",
"2025-02-02": "https://v.douyu.com/show/yVY8WwDQx68vLOz9",
"2025-02-04": "https://v.douyu.com/show/XqeO74N9bknWxywG",
"2025-02-05": "https://v.douyu.com/show/EO0XvNwa5Ej7DrBd",
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
