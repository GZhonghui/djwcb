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
"2023-05-28": "https://v.douyu.com/show/yVY8WwdAkGzvLOz9",
"2023-05-30": "https://v.douyu.com/show/yVmjvBpZq6RMqkNb",
"2023-05-31": "https://v.douyu.com/show/1LDR7QZN3aZMJzx8",
"2023-06-02": "https://v.douyu.com/show/0Q8mMYYkwD2M49Ad",
"2023-06-03": "https://v.douyu.com/show/8KxjMdGJOeV7VLwb",
"2023-06-04": "https://v.douyu.com/show/aRbBv3AoB9mM6PYV",
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
