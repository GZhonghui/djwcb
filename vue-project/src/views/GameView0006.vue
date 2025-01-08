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
"2019-08-30": "https://v.douyu.com/show/DO84vr63p5wvedGr",
"2022-10-07": "https://v.douyu.com/show/LDBbMA8gP5g7yJRP",
"2022-10-08": "https://v.douyu.com/show/6Aw87OZxpwdvYGkg",
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
