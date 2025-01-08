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
"2024-03-02": "https://v.douyu.com/show/0Q8mMYYz11LM49Ad",
"2024-03-03": "https://v.douyu.com/show/6Aw87O8AZLZMYGkg",
"2024-03-05": "https://v.douyu.com/show/NbwE7Z8q5jpWn5Zz",
"2024-03-06[大结局]": "https://v.douyu.com/show/mPyq7o81paqM1gLY",
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
