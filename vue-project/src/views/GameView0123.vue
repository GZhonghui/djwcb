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
"2023-11-03": "https://v.douyu.com/show/Kp1QM8An9lNWk4bj",
"2023-11-04": "https://v.douyu.com/show/0zZVvPoaJabWO4E2",
"2023-11-06": "https://v.douyu.com/show/DO84vr8QBjwMedGr",
"2023-11-07": "https://v.douyu.com/show/jwzOvpxbzbAvZVRm",
"2023-11-08": "https://v.douyu.com/show/a2JEMJnXDk0MNxml",
"2023-11-10": "https://v.douyu.com/show/2V0JMVGX5RGWRY5k",
"2023-11-11": "https://v.douyu.com/show/DrwnvzgVOmn7PNaX",
"2023-11-14": "https://v.douyu.com/show/8pa9v5NKrqL7VrqA",
"2023-11-15": "https://v.douyu.com/show/2V0JMVGyYbGWRY5k",
"2023-11-17": "https://v.douyu.com/show/EO0XvNbQkJJvDrBd",
"2023-11-18": "https://v.douyu.com/show/jNBdvn8GekBME2yw",
"2023-11-19[大结局]": "https://v.douyu.com/show/yVmjvBpJ256MqkNb",
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
