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
"2023-09-20": "https://v.douyu.com/show/JmbBMkgdOKKM40XA",
"2023-09-21": "https://v.douyu.com/show/8KxjMdGEKkm7VLwb",
"2023-09-23": "https://v.douyu.com/show/jNBdvn8xjaoME2yw",
"2023-09-24": "https://v.douyu.com/show/Bjq4MelE2aJ75Ea8",
"2023-09-26": "https://v.douyu.com/show/DO84vr8mrOGMedGr",
"2023-09-27": "https://v.douyu.com/show/brN0MmxrRVb7pyxA",
"2023-09-28": "https://v.douyu.com/show/ZB5Kv9YDP2Kva93x",
"2023-09-29": "https://v.douyu.com/show/DO84vr8mQ4OMedGr",
"2023-09-30": "https://v.douyu.com/show/Yo4evygBO56M8L62",
"2023-10-01": "https://v.douyu.com/show/LDBbMANVPXVWyJRP",
"2023-10-03[大结局]": "https://v.douyu.com/show/8KxjMdGgYbO7VLwb",
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
