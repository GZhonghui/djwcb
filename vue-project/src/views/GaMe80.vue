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
"2023-08-19": "https://v.douyu.com/show/brN0MmxXXLO7pyxA",
"2023-08-20": "https://v.douyu.com/show/Kp1QM8AB15RWk4bj",
"2023-08-22": "https://v.douyu.com/show/2Bj8vGpky6V7Obnd",
"2023-08-23": "https://v.douyu.com/show/a4Jj7l8XRB67Dk01",
"2023-08-25": "https://v.douyu.com/show/worZv0ZXkpGMJBk3",
"2023-08-26": "https://v.douyu.com/show/yVY8Wwd5dmBvLOz9",
"2023-08-27": "https://v.douyu.com/show/ERALvE8B39aW1Vw0",
"2023-08-29": "https://v.douyu.com/show/a2JEMJnOeV2MNxml",
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
