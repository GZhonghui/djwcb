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
"2023-01-24": "https://v.douyu.com/show/Qyz171Z2zpbMBJj9",
"2023-01-27": "https://v.douyu.com/show/yVY8Ww6n2AoMLOz9",
"2023-05-21": "https://v.douyu.com/show/Qyz171Dwqp1vBJj9",
"2023-05-23": "https://v.douyu.com/show/8KxjMdGBARO7VLwb",
"2023-05-24": "https://v.douyu.com/show/6Aw87O8p21ZMYGkg",
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
