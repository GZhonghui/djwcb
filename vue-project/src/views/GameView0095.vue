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
"2023-04-14": "https://v.douyu.com/show/jwzOvpGK3nQWZVRm",
"2023-04-15": "https://v.douyu.com/show/3rob7jOX3ykMgkZl",
"2023-04-21": "https://v.douyu.com/show/Kg1VWR4nwxL7GbNA",
"2023-04-23": "https://v.douyu.com/show/2V0JMVV9r6bMRY5k",
"2023-04-27": "https://v.douyu.com/show/yVmjvBb00PAvqkNb",
"2023-05-03": "https://v.douyu.com/show/worZv0bjDz9MJBk3",
"2023-05-05": "https://v.douyu.com/show/ZB5Kv9eNo5eva93x",
"2023-05-06[铲车人团建]": "https://v.douyu.com/show/wLjGvLqYm107mO90",
"2023-05-07": "https://v.douyu.com/show/ERALvEbk0Qx71Vw0",
"2023-05-10": "https://v.douyu.com/show/JmbBMk9LzXZv40XA",
"2023-05-12": "https://v.douyu.com/show/yVY8WwdaD0BvLOz9",
"2023-05-13": "https://v.douyu.com/show/GnzXvbQG1GlW462l",
"2023-05-25": "https://v.douyu.com/show/Aox276Dg5pKWVz8Z",
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
