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
"2023-06-06": "https://v.douyu.com/show/Aox276Dk14NWVz8Z",
"2023-06-07": "https://v.douyu.com/show/6Aw87O8mqGgMYGkg",
"2023-06-09": "https://v.douyu.com/show/4xq3WDBKqOo7LGNz",
"2023-06-10": "https://v.douyu.com/show/X3JzMaQm60GMPQro",
"2023-06-11": "https://v.douyu.com/show/Drwnvzgm68n7PNaX",
"2023-06-13": "https://v.douyu.com/show/2V0JMVGlJBAWRY5k",
"2023-06-14": "https://v.douyu.com/show/85BAvq8RKkyWG4Lm",
"2023-06-16": "https://v.douyu.com/show/r90XWgjdOQ2Mgk25",
"2023-06-17": "https://v.douyu.com/show/LDBbMAN5YNBWyJRP",
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
