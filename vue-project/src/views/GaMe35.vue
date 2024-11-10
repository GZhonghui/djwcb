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
"2023-01-01": "https://v.douyu.com/show/DO84vrKpNGY7edGr",
"2023-01-02": "https://v.douyu.com/show/Yo4evyxlGdXW8L62",
"2023-01-03": "https://v.douyu.com/show/yVmjvBbz19AvqkNb",
"2023-01-05": "https://v.douyu.com/show/NVm0WKzkEQjMJeBP",
"2023-01-06": "https://v.douyu.com/show/Qyz171ZjBp0MBJj9",
"2023-01-08": "https://v.douyu.com/show/6Aw87OOnNPj7YGkg",
"2023-01-12": "https://v.douyu.com/show/brN0Mm4E8E37pyxA",
"2023-01-14": "https://v.douyu.com/show/JmbBMk9J9AYv40XA",
"2023-01-15": "https://v.douyu.com/show/0Q8mMY9NgxjM49Ad",
"2023-01-18": "https://v.douyu.com/show/yVmjvBbRxwdvqkNb",
"2023-01-25": "https://v.douyu.com/show/4xq3WDpYAZRWLGNz",
"2023-02-01": "https://v.douyu.com/show/jwzOvpGDoxDWZVRm",
"2023-02-02": "https://v.douyu.com/show/XqeO74AnxN1MxywG",
"2023-02-04": "https://v.douyu.com/show/X3JzMaOAzDGvPQro",
"2023-02-08": "https://v.douyu.com/show/6Aw87OOXb0j7YGkg",
"2023-02-09": "https://v.douyu.com/show/2Bj8vGEYPnQMObnd",
"2023-02-11": "https://v.douyu.com/show/n8GzMXmp1LVW6qyP",
"2023-02-12": "https://v.douyu.com/show/X3JzMaOp65LvPQro",
"2023-02-15": "https://v.douyu.com/show/1LDR7QJ6XAVMJzx8",
"2023-02-18": "https://v.douyu.com/show/0zZVvP9eZRo7O4E2",
"2023-03-01": "https://v.douyu.com/show/8pa9v5Pyb4pWVrqA",
"2023-03-09": "https://v.douyu.com/show/3rob7jOV0kbMgkZl",
"2023-04-01": "https://v.douyu.com/show/Kg1VWR4zYem7GbNA",
"2023-04-02": "https://v.douyu.com/show/2Bj8vGEdaNDMObnd",
"2023-04-06": "https://v.douyu.com/show/Aox2762VxXP7Vz8Z",
"2023-04-07": "https://v.douyu.com/show/2Bj8vGEReeQMObnd",
"2023-04-10": "https://v.douyu.com/show/r90XWgqgDl27gk25",
"2023-04-12": "https://v.douyu.com/show/Bjq4MerNbZqW5Ea8",
"2023-04-16": "https://v.douyu.com/show/yVY8Ww6Jk1VMLOz9",
"2023-04-22": "https://v.douyu.com/show/brN0Mm4Ye367pyxA",
"2023-04-26": "https://v.douyu.com/show/X3JzMaObjPPvPQro",
"2023-04-29": "https://v.douyu.com/show/2Bj8vGEJkneMObnd",
"2023-04-30": "https://v.douyu.com/show/85BAvqKJP4eMG4Lm",
"2023-10-19": "https://v.douyu.com/show/XqeO74DmJNe7xywG",
"2024-03-01": "https://v.douyu.com/show/qJgOWxgVjeNMkVzL",
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
