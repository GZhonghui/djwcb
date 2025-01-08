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
"2023-06-27": "https://v.douyu.com/show/X3JzMaQVGx9MPQro",
"2023-06-28": "https://v.douyu.com/show/ERALvE8wbw5W1Vw0",
"2023-06-30": "https://v.douyu.com/show/ERALvE8w1dDW1Vw0",
"2023-07-01": "https://v.douyu.com/show/X3JzMaQVn5AMPQro",
"2023-07-02": "https://v.douyu.com/show/qJgOWxgOqQKMkVzL",
"2023-07-03": "https://v.douyu.com/show/NbwE7Z8VrlBWn5Zz",
"2023-07-04": "https://v.douyu.com/show/brN0MmxzOme7pyxA",
"2023-07-05": "https://v.douyu.com/show/NVm0WKNZzNwMJeBP",
"2023-07-06": "https://v.douyu.com/show/1LDR7QZla86MJzx8",
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
