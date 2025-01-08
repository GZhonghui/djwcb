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
"2022-06-12": "",
"2022-07-02": "https://v.douyu.com/show/8KxjMdk3JAn7VLwb",
"2022-07-03": "https://v.douyu.com/show/GnzXvblqP1oM462l",
"2022-07-05": "https://v.douyu.com/show/NbwE7Z2PRXR7n5Zz",
"2022-07-06": "https://v.douyu.com/show/LDBbMA81LNg7yJRP",
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
