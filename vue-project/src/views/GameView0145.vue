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
"2024-03-19": "https://v.douyu.com/show/JmbBMkgpeKYM40XA",
"2024-03-20": "https://v.douyu.com/show/ZB5Kv9YGqXmva93x",
"2024-03-21": "https://v.douyu.com/show/aRbBv3AGne4M6PYV",
"2024-03-23": "https://v.douyu.com/show/3rob7jQXDb3vgkZl",
"2024-03-24": "https://v.douyu.com/show/Kp1QM8AE4ywWk4bj",
"2024-03-26": "https://v.douyu.com/show/8KxjMdG0wbO7VLwb",
"2024-03-27": "https://v.douyu.com/show/DO84vr8qaLlMedGr",
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
