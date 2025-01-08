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
"2020-08-27[断了一截，9-16续上，和怪猎一起]": "",
"2022-07-01": "https://v.douyu.com/show/Kg1VWRB2njQWGbNA",
"2022-07-08": "https://v.douyu.com/show/DrwnvzKq8wQ7PNaX",
"2022-07-09": "https://v.douyu.com/show/ZB5Kv9o0O38Ma93x",
"2022-07-10": "https://v.douyu.com/show/0Q8mMYGogoNv49Ad",
"2022-07-12": "https://v.douyu.com/show/DO84vr92PrQWedGr",
"2022-07-13": "https://v.douyu.com/show/qJgOWxmEjZRvkVzL",
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
