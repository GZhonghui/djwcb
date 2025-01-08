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
"2022-10-14": "",
"2022-10-15": "https://v.douyu.com/show/NbwE7Z2kpxP7n5Zz",
"2022-10-16": "https://v.douyu.com/show/Kg1VWRBqleLWGbNA",
"2022-10-18": "https://v.douyu.com/show/2V0JMVxEGEEvRY5k",
"2022-10-19": "https://v.douyu.com/show/GnzXvblxqzwM462l",
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
