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
"2023-07-07": "https://v.douyu.com/show/NVm0WKNZ1QQMJeBP",
"2023-07-08": "https://v.douyu.com/show/X3JzMaQknqGMPQro",
"2023-07-09": "https://v.douyu.com/show/6Aw87O8ZYO4MYGkg",
"2023-07-13": "https://v.douyu.com/show/2V0JMVGVjeaWRY5k",
"2023-07-15": "https://v.douyu.com/show/DO84vr8K1zkMedGr",
"2023-07-19": "https://v.douyu.com/show/wLjGvLxxq2EvmO90",
"2023-07-20": "https://v.douyu.com/show/r90XWgjjGrDMgk25",
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
