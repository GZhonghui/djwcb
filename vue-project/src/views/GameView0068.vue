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
"2022-07-21": "https://v.douyu.com/show/0Q8mMYGXEzqv49Ad",
"2022-07-22": "https://v.douyu.com/show/2Bj8vGNY083WObnd",
"2022-07-23": "https://v.douyu.com/show/X3JzMakqwglvPQro",
"2022-07-24": "https://v.douyu.com/show/ERALvElEGbnW1Vw0",
"2023-01-23[关服 + COS]": "https://v.douyu.com/show/1LDR7QJPz1mMJzx8",
"2023-03-23[24小时竞技场]": "https://v.douyu.com/show/kDe0W2mxek8MA4Bz",
"2023-03-24[24小时竞技场]": "https://v.douyu.com/show/XqeO74A1xGZMxywG",
"2023-03-25[24小时竞技场]": "https://v.douyu.com/show/jwzOvpGo3pjWZVRm",
"2023-03-26[24小时竞技场]": "https://v.douyu.com/show/0Q8mMY9LRAjM49Ad",
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
