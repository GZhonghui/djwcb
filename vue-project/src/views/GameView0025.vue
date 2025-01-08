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
"2020-03-15[就玩了一天]": "",
"2020-12-02[又是一天]": "",
"2024-04-24": "https://v.douyu.com/show/2V0JMVG9gDDWRY5k",
"2024-04-26": "https://v.douyu.com/show/DO84vr8xx90MedGr",
"2024-04-27": "https://v.douyu.com/show/2V0JMVGEKBkWRY5k",
"2024-04-28": "https://v.douyu.com/show/3rob7jQ6Kb1vgkZl",
"2024-04-30[月末放羊]": "https://v.douyu.com/show/n8GzMX8Y161M6qyP",
"2024-05-04": "https://v.douyu.com/show/6Aw87O8PBgxMYGkg",
"2024-05-05": "https://v.douyu.com/show/worZv0ZjJOpMJBk3",
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
