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
"2018-09-20": "https://v.douyu.com/show/DrwnvzyLZnOWPNaX",
"2019-07-25": "https://v.douyu.com/show/Aox276g6nE2MVz8Z",
"2019-07-27": "https://v.douyu.com/show/1LDR7QDk406vJzx8",
"2019-09-17": "https://v.douyu.com/show/LDBbMAxjxYq7yJRP",
"2019-10-05": "https://v.douyu.com/show/2Bj8vG5DZLyMObnd",
"2019-12-31": "https://v.douyu.com/show/Aox276kqx5KMVz8Z",
"2020-02-15": "https://v.douyu.com/show/Kg1VWRP3L8N7GbNA",
"2020-06-08": "https://v.douyu.com/show/n8GzMXlVAKDM6qyP",
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
