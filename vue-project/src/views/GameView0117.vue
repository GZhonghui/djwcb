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
"2023-09-01": "https://v.douyu.com/show/XqeO74DVbpX7xywG",
"2023-09-02": "https://v.douyu.com/show/8pa9v5N35mR7VrqA",
"2023-09-03": "https://v.douyu.com/show/yVY8WwdldrBvLOz9",
"2023-09-05": "https://v.douyu.com/show/ERALvE831ZDW1Vw0",
"2023-09-06": "https://v.douyu.com/show/JmbBMkgk2KyM40XA",
"2023-09-08": "https://v.douyu.com/show/DO84vr8l3wOMedGr",
"2023-09-09": "https://v.douyu.com/show/85BAvq8wj3pWG4Lm",
"2023-09-10": "https://v.douyu.com/show/DO84vr8aoqGMedGr",
"2023-09-17": "https://v.douyu.com/show/8pa9v5NwpOL7VrqA",
"2023-09-26": "https://v.douyu.com/show/DO84vr8mrOGMedGr",
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
