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
"2020-05-16[搞笑视频 + KTV]": "https://v.douyu.com/show/mPyq7o65ZwYv1gLY",
"2023-08-06": "https://v.douyu.com/show/6Aw87O8gr8xMYGkg",
"2023-08-13": "https://v.douyu.com/show/EO0XvNb6kDjvDrBd",
"2023-09-19": "https://v.douyu.com/show/jNBdvn8xRrNME2yw",
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
