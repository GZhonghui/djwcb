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
"2024-01-27": "https://v.douyu.com/show/r90XWgjyERNMgk25",
"2024-01-28": "https://v.douyu.com/show/85BAvq8yAmKWG4Lm",
"2024-01-29": "https://v.douyu.com/show/0Q8mMYYOPL5M49Ad",
"2024-01-30": "https://v.douyu.com/show/a2JEMJnYjzZMNxml",
"2024-01-31": "https://v.douyu.com/show/Bjq4Melb0gA75Ea8",
"2024-02-02": "https://v.douyu.com/show/mPyq7o80rPQM1gLY",
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
