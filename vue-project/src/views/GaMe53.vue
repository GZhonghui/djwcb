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
"2023-02-24": "https://v.douyu.com/show/NVm0WKzOoV8MJeBP",
"2023-02-25": "https://v.douyu.com/show/2V0JMVV2g2DMRY5k",
"2023-03-03": "https://v.douyu.com/show/r90XWgq8zkK7gk25",
"2023-03-04": "https://v.douyu.com/show/aRbBv3Pg3jD76PYV",
"2023-03-07": "https://v.douyu.com/show/r90XWgqlXOw7gk25",
"2023-03-14": "https://v.douyu.com/show/Kg1VWR40Q0L7GbNA",
"2023-03-15": "https://v.douyu.com/show/2Bj8vGE2rdLMObnd",
"2023-03-16": "https://v.douyu.com/show/DO84vrKyLAl7edGr",
"2023-03-18": "https://v.douyu.com/show/Aox2762LPA27Vz8Z",
"2023-03-21": "https://v.douyu.com/show/85BAvqKNb3BMG4Lm",
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
