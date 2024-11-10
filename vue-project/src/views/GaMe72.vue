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
"回到首页": "/",
"2024-03-29": "https://v.douyu.com/show/worZv0ZDR3pMJBk3",
"2024-04-01": "https://v.douyu.com/show/Kg1VWR8rgJm7GbNA",
"2024-04-02": "https://v.douyu.com/show/aRbBv3Ama5XM6PYV",
"2024-04-03": "https://v.douyu.com/show/qJgOWxgpoVeMkVzL",
"2024-04-05": "https://v.douyu.com/show/JmbBMkgElO0M40XA",
"2024-04-06": "https://v.douyu.com/show/a2JEMJnNJ12MNxml",
"2024-04-07": "https://v.douyu.com/show/ZB5Kv9YaEJ9va93x",
"2024-04-09": "https://v.douyu.com/show/85BAvq8AdjXWG4Lm",
"2024-04-10": "https://v.douyu.com/show/aRbBv3A91yyM6PYV",
"2024-04-12": "https://v.douyu.com/show/85BAvq8AyDXWG4Lm",
      }
    };
  },
  methods: {
    go(link) {
      if (link.startsWith('/')) {
        this.$router.push(link);
      } else {
        window.open(link, '_blank'); // window.location.href = link;
      }
    }
  }
};
</script>

<style scoped>
/* Transparent container backgrounds */
.app-container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background-color: transparent; /* Ensure no background color */
}

/* Button container styles */
.buttons-container {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  padding: 50px;
  background-color: transparent; /* Ensure no background color */
}

/* Button styles */
.button {
  padding: 15px 25px;
  font-size: 18px;
  cursor: pointer;
  background-color: #ffffff; /* Solid white background */
  color: #333;
  border: 1px solid #ddd;
  border-radius: 12px;
  text-transform: uppercase;
  box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
  transition: background-color 0.3s, transform 0.2s;
}

/* Hover effect for buttons */
.button:hover {
  background-color: #f0f0f0;
  transform: scale(1.03);
}
</style>
