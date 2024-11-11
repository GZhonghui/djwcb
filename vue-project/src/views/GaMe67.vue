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
"2022-11-21": "",
"2022-11-13": "https://v.douyu.com/show/2Bj8vGEXg6yMObnd",
"2022-11-14": "https://v.douyu.com/show/Kg1VWR4AEGm7GbNA",
"2022-11-15": "https://v.douyu.com/show/worZv0bNz4lMJBk3",
"2022-11-16": "https://v.douyu.com/show/Aox27629B007Vz8Z",
"2022-11-22": "https://v.douyu.com/show/kDe0W2mQ48RMA4Bz",
"2022-11-24": "https://v.douyu.com/show/0zZVvP9Gnmq7O4E2",
"2022-11-25": "https://v.douyu.com/show/n8GzMXmzE2rW6qyP",
"2022-11-26": "https://v.douyu.com/show/Aox2762QJ5x7Vz8Z",
"2022-11-27": "https://v.douyu.com/show/yVmjvBbDPyRvqkNb",
"2022-11-28": "https://v.douyu.com/show/brN0Mm4z2yQ7pyxA",
"2022-11-29": "https://v.douyu.com/show/8pa9v5PoNapWVrqA",
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
