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
"2024-03-09": "https://v.douyu.com/show/DrwnvzgxQ6l7PNaX",
"2024-03-10": "https://v.douyu.com/show/a2JEMJn1dVYMNxml",
"2024-03-12": "https://v.douyu.com/show/1LDR7QZrpZgMJzx8",
"2024-03-13": "https://v.douyu.com/show/jNBdvn8yVXJME2yw",
"2024-03-15": "https://v.douyu.com/show/a2JEMJnqKmkMNxml",
"2024-03-16": "https://v.douyu.com/show/n8GzMX82dKAM6qyP",
"2024-03-17": "https://v.douyu.com/show/4xq3WDBGYwN7LGNz",
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
