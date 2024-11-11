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
"2021-12-15": "",
"2023-01-21": "https://v.douyu.com/show/2V0JMVVRnxEMRY5k",
"2023-01-28": "https://v.douyu.com/show/8pa9v5PmNyqWVrqA",
"2023-01-30": "https://v.douyu.com/show/XqeO74AR02nMxywG",
"2023-02-02": "https://v.douyu.com/show/XqeO74AnxN1MxywG",
"2023-02-03": "https://v.douyu.com/show/aRbBv3PyA6m76PYV",
"2023-02-04": "https://v.douyu.com/show/X3JzMaOAzDGvPQro",
"2023-02-05": "https://v.douyu.com/show/3rob7jOAeZbMgkZl",
"2023-02-08": "https://v.douyu.com/show/6Aw87OOXb0j7YGkg",
"2023-02-09": "https://v.douyu.com/show/2Bj8vGEYPnQMObnd",
"2023-02-11": "https://v.douyu.com/show/n8GzMXmp1LVW6qyP",
"2023-02-12": "https://v.douyu.com/show/X3JzMaOp65LvPQro",
"2023-02-15": "https://v.douyu.com/show/1LDR7QJ6XAVMJzx8",
"2023-02-16": "https://v.douyu.com/show/2V0JMVV6p5aMRY5k",
"2023-02-18": "https://v.douyu.com/show/0zZVvP9eZRo7O4E2",
"2023-02-19": "https://v.douyu.com/show/0zZVvP9eBw57O4E2",
"2023-02-22": "https://v.douyu.com/show/1LDR7QJALoBMJzx8",
"2023-02-23": "https://v.douyu.com/show/XqeO74Aw2myMxywG",
"2023-02-25": "https://v.douyu.com/show/2V0JMVV2g2DMRY5k",
"2023-02-26": "https://v.douyu.com/show/aRbBv3PBoPX76PYV",
"2023-03-02": "https://v.douyu.com/show/yVmjvBbybpdvqkNb",
"2023-03-05": "https://v.douyu.com/show/Kg1VWR4ywRr7GbNA",
"2023-03-07": "https://v.douyu.com/show/r90XWgqlXOw7gk25",
"2023-03-08": "https://v.douyu.com/show/LDBbMAb6NDyWyJRP",
"2023-03-09": "https://v.douyu.com/show/3rob7jOV0kbMgkZl",
"2023-03-10": "https://v.douyu.com/show/EO0XvN3JQk87DrBd",
"2023-03-14": "https://v.douyu.com/show/Kg1VWR40Q0L7GbNA",
"2023-03-15": "https://v.douyu.com/show/2Bj8vGE2rdLMObnd",
"2023-03-16": "https://v.douyu.com/show/DO84vrKyLAl7edGr",
"2023-03-18": "https://v.douyu.com/show/Aox2762LPA27Vz8Z",
"2023-03-20": "https://v.douyu.com/show/4xq3WDpZEzjWLGNz",
"2023-03-22": "https://v.douyu.com/show/6Aw87OON4p47YGkg",
"2023-03-26": "https://v.douyu.com/show/0Q8mMY9LRAjM49Ad",
"2023-03-28": "https://v.douyu.com/show/JmbBMk943kQv40XA",
"2023-03-30": "https://v.douyu.com/show/qJgOWxZV2ol7kVzL",
"2023-03-31": "https://v.douyu.com/show/LDBbMAbdNbeWyJRP",
"2023-04-01": "https://v.douyu.com/show/Kg1VWR4zYem7GbNA",
"2023-04-02": "https://v.douyu.com/show/2Bj8vGEdaNDMObnd",
"2023-04-04": "https://v.douyu.com/show/NbwE7ZJmj0k7n5Zz",
"2023-04-06": "https://v.douyu.com/show/Aox2762VxXP7Vz8Z",
"2023-04-07": "https://v.douyu.com/show/2Bj8vGEReeQMObnd",
"2023-04-08": "https://v.douyu.com/show/X3JzMaOr2VAvPQro",
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
