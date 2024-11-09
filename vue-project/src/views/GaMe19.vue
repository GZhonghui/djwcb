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
"2022-11-28": "https://v.douyu.com/show/brN0Mm4z2yQ7pyxA",
"2023-01-12": "https://v.douyu.com/show/brN0Mm4E8E37pyxA",
"2023-01-14": "https://v.douyu.com/show/JmbBMk9J9AYv40XA",
"2023-01-15": "https://v.douyu.com/show/0Q8mMY9NgxjM49Ad",
"2023-01-18": "https://v.douyu.com/show/yVmjvBbRxwdvqkNb",
"2023-02-01": "https://v.douyu.com/show/jwzOvpGDoxDWZVRm",
"2023-02-02": "https://v.douyu.com/show/XqeO74AnxN1MxywG",
"2023-02-08": "https://v.douyu.com/show/6Aw87OOXb0j7YGkg",
"2023-02-15": "https://v.douyu.com/show/1LDR7QJ6XAVMJzx8",
"2023-02-18": "https://v.douyu.com/show/0zZVvP9eZRo7O4E2",
"2023-03-01": "https://v.douyu.com/show/8pa9v5Pyb4pWVrqA",
"2023-04-07": "https://v.douyu.com/show/2Bj8vGEReeQMObnd",
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
