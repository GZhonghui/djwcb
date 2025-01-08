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
"2023-12-05": "https://v.douyu.com/show/jwzOvpx85GqvZVRm",
"2023-12-06": "https://v.douyu.com/show/6Aw87O8edOjMYGkg",
"2023-12-08": "https://v.douyu.com/show/Kg1VWR8d5Xo7GbNA",
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
