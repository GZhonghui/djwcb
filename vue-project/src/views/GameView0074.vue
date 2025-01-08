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
"2022-11-02": "https://v.douyu.com/show/Yo4evyxmlX6W8L62",
"2022-11-05": "https://v.douyu.com/show/qJgOWxZAAnX7kVzL",
"2022-11-06": "https://v.douyu.com/show/0zZVvP9m1xq7O4E2",
"2022-11-07": "https://v.douyu.com/show/wLjGvLqp4P27mO90",
"2022-11-08": "https://v.douyu.com/show/0Q8mMY90O1LM49Ad",
"2022-11-11": "https://v.douyu.com/show/Bjq4Mer4VyzW5Ea8",
"2022-11-12": "https://v.douyu.com/show/0zZVvP9RB327O4E2",
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
