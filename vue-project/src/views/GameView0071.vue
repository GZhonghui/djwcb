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
"2022-10-01": "https://v.douyu.com/show/wLjGvLZ3bNxMmO90",
"2022-10-04": "https://v.douyu.com/show/ZB5Kv9o1Xa2Ma93x",
"2022-10-06": "https://v.douyu.com/show/NbwE7Z2bXDk7n5Zz",
"2022-10-09": "https://v.douyu.com/show/LDBbMA8RN9g7yJRP",
"2022-10-10": "https://v.douyu.com/show/JmbBMklEw6yW40XA",
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
