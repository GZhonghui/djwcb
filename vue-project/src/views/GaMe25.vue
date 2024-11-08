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
"2024-09-01": "https://v.douyu.com/show/NVm0WK4ZYObvJeBP",
"2024-09-03": "https://v.douyu.com/show/85BAvqQK1nwvG4Lm",
"2024-09-04": "https://v.douyu.com/show/NVm0WK4zgAPvJeBP",
"2024-09-06": "https://v.douyu.com/show/XqeO74NAa1NWxywG",
"2024-09-07": "https://v.douyu.com/show/Aox276Y2O2NvVz8Z",
"2024-09-08": "https://v.douyu.com/show/NVm0WK4zoy0vJeBP",
"2024-09-10": "https://v.douyu.com/show/DrwnvzDZL6jMPNaX",
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
