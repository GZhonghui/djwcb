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
"2024-02-04": "https://v.douyu.com/show/yVY8WwdzNyVvLOz9",
"2024-03-22": "https://v.douyu.com/show/8pa9v5NGDpp7VrqA",
"2024-03-25": "https://v.douyu.com/show/a2JEMJnzb8oMNxml",
"2024-03-27": "https://v.douyu.com/show/DO84vr8qaLlMedGr",
"2024-04-01": "https://v.douyu.com/show/Kg1VWR8rgJm7GbNA",
"2024-04-02": "https://v.douyu.com/show/aRbBv3Ama5XM6PYV",
"2024-04-03": "https://v.douyu.com/show/qJgOWxgpoVeMkVzL",
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
