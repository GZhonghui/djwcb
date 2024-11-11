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
"2024-06-21[放羊]": "https://v.douyu.com/show/0Q8mMY506wjM49Ad",
"2024-06-22": "https://v.douyu.com/show/8KxjMdl8DYQMVLwb",
"2024-06-23": "https://v.douyu.com/show/yVY8WwDAzXPvLOz9",
"2024-06-25": "https://v.douyu.com/show/jwzOvp1Z91X7ZVRm",
"2024-06-26[放羊]": "https://v.douyu.com/show/qJgOWx52KbNvkVzL",
"2024-06-28": "https://v.douyu.com/show/0zZVvPQR9Vb7O4E2",
"2024-06-29": "https://v.douyu.com/show/wLjGvLrQKPpMmO90",
"2024-07-01": "https://v.douyu.com/show/LDBbMAKJQ0yvyJRP",
"2024-07-02": "https://v.douyu.com/show/brN0MmQODwOMpyxA",
"2024-07-04[老头环战老头]": "https://v.douyu.com/show/EO0XvNwNyDj7DrBd",
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
