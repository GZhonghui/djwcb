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
"2024-09-27": "https://v.douyu.com/show/Yo4evyDgeDRW8L62",
"2024-09-28": "https://v.douyu.com/show/2V0JMVQGzqb7RY5k",
"2024-09-29": "https://v.douyu.com/show/0Q8mMY55krmM49Ad",
"2024-10-01": "https://v.douyu.com/show/kDe0W2ggDrPvA4Bz",
"2024-10-02": "https://v.douyu.com/show/kDe0W2ggy8ovA4Bz",
"2024-10-04": "https://v.douyu.com/show/a2JEMJJJ4w2MNxml",
"2024-10-05": "https://v.douyu.com/show/ZB5Kv9ggnemMa93x",
"2024-10-06": "https://v.douyu.com/show/0Q8mMY556x8M49Ad",
"2024-10-07": "https://v.douyu.com/show/85BAvqQQeXwvG4Lm",
"2024-10-09": "https://v.douyu.com/show/Yo4evyDD30NW8L62",
"2024-10-10": "https://v.douyu.com/show/jNBdvnbbnyPvE2yw",
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
