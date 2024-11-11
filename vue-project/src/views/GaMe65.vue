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
"2023-06-06": "https://v.douyu.com/show/Aox276Dk14NWVz8Z",
"2023-06-07": "https://v.douyu.com/show/6Aw87O8mqGgMYGkg",
"2023-06-09": "https://v.douyu.com/show/4xq3WDBKqOo7LGNz",
"2023-06-10": "https://v.douyu.com/show/X3JzMaQm60GMPQro",
"2023-06-11": "https://v.douyu.com/show/Drwnvzgm68n7PNaX",
"2023-06-13": "https://v.douyu.com/show/2V0JMVGlJBAWRY5k",
"2023-06-14": "https://v.douyu.com/show/85BAvq8RKkyWG4Lm",
"2023-06-16": "https://v.douyu.com/show/r90XWgjdOQ2Mgk25",
"2023-06-17": "https://v.douyu.com/show/LDBbMAN5YNBWyJRP",
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
