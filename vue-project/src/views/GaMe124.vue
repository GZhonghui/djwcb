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
"2023-11-21": "https://v.douyu.com/show/2V0JMVG6BO4WRY5k",
"2023-11-22": "https://v.douyu.com/show/ERALvE8P95xW1Vw0",
"2023-11-26": "https://v.douyu.com/show/4xq3WDBDedj7LGNz",
"2023-11-27": "https://v.douyu.com/show/a2JEMJnmQeZMNxml",
"2023-11-28": "https://v.douyu.com/show/Yo4evygLrKXM8L62",
"2023-11-29": "https://v.douyu.com/show/brN0MmxZPQ07pyxA",
"2023-12-02": "https://v.douyu.com/show/kDe0W2DojXX7A4Bz",
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
