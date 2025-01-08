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
"2020-06-06": "https://v.douyu.com/show/85BAvqxzXPBWG4Lm",
"2020-06-07": "https://v.douyu.com/show/XqeO74eJEJrMxywG",
"2020-06-14": "https://v.douyu.com/show/Qyz171mkERJ7BJj9",
"2020-06-06[又摆好久]": "",
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
