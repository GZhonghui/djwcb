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
"2025-04-12": "https://v.douyu.com/show/ERALvEqEbrDv1Vw0",
"2025-04-13": "https://v.douyu.com/show/mPyq7ob2YY2v1gLY",
"2025-04-15": "https://v.douyu.com/show/DrwnvzDVYAOMPNaX",
"2025-04-16": "https://v.douyu.com/show/6Aw87OQXoExWYGkg",
"2025-04-18": "https://v.douyu.com/show/X3JzMalqp0V7PQro",
"2025-04-19": "https://v.douyu.com/show/yVmjvBgQojz7qkNb",
"2025-04-20": "https://v.douyu.com/show/85BAvqQZgQwvG4Lm",
"2025-04-22": "https://v.douyu.com/show/XqeO74NOdyrWxywG",
"2025-04-23": "https://v.douyu.com/show/a4Jj7lBop85WDk01",
"2025-04-25": "https://v.douyu.com/show/r90XWgomxxgWgk25",
"2025-04-27": "https://v.douyu.com/show/n8GzMXQp0QgW6qyP",
"2025-04-29": "https://v.douyu.com/show/6Aw87OQRQjZWYGkg",
"2025-04-30": "https://v.douyu.com/show/4xq3WDzrJ9l7LGNz",
"2025-05-01": "https://v.douyu.com/show/NbwE7ZYp59yvn5Zz",
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
