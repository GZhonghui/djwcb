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
"2023-03-15": "https://v.douyu.com/show/2Bj8vGE2rdLMObnd",
"2023-03-17": "https://v.douyu.com/show/aRbBv3PLEVg76PYV",
"2023-03-21": "https://v.douyu.com/show/85BAvqKNb3BMG4Lm",
"2023-03-22": "https://v.douyu.com/show/6Aw87OON4p47YGkg",
"2023-03-27": "https://v.douyu.com/show/Bjq4MerqAXxW5Ea8",
"2023-03-28": "https://v.douyu.com/show/JmbBMk943kQv40XA",
"2023-03-30": "https://v.douyu.com/show/qJgOWxZV2ol7kVzL",
"2023-03-31": "https://v.douyu.com/show/LDBbMAbdNbeWyJRP",
"2023-04-01": "https://v.douyu.com/show/Kg1VWR4zYem7GbNA",
"2023-04-02": "https://v.douyu.com/show/2Bj8vGEdaNDMObnd",
"2023-04-04": "https://v.douyu.com/show/NbwE7ZJmj0k7n5Zz",
"2023-04-05": "https://v.douyu.com/show/X3JzMaOrVyAvPQro",
"2023-04-06": "https://v.douyu.com/show/Aox2762VxXP7Vz8Z",
"2023-04-11": "https://v.douyu.com/show/8pa9v5PGROaWVrqA",
"2023-04-13": "https://v.douyu.com/show/Qyz171ZGk31MBJj9",
"2023-04-14": "https://v.douyu.com/show/jwzOvpGK3nQWZVRm",
"2023-04-15": "https://v.douyu.com/show/3rob7jOX3ykMgkZl",
"2023-04-16": "https://v.douyu.com/show/yVY8Ww6Jk1VMLOz9",
"2023-04-18": "https://v.douyu.com/show/DrwnvzZnJAVvPNaX",
"2023-04-21": "https://v.douyu.com/show/Kg1VWR4nwxL7GbNA",
"2023-04-22": "https://v.douyu.com/show/brN0Mm4Ye367pyxA",
"2023-04-23": "https://v.douyu.com/show/2V0JMVV9r6bMRY5k",
"2023-05-05": "https://v.douyu.com/show/ZB5Kv9eNo5eva93x",
"2023-05-06": "https://v.douyu.com/show/wLjGvLqYm107mO90",
"2023-05-07": "https://v.douyu.com/show/ERALvEbk0Qx71Vw0",
"2023-05-10": "https://v.douyu.com/show/JmbBMk9LzXZv40XA",
"2023-05-12": "https://v.douyu.com/show/yVY8WwdaD0BvLOz9",
"2023-05-20": "https://v.douyu.com/show/6Aw87O82zQDMYGkg",
"2024-05-01[和NO总双人战棋]": "https://v.douyu.com/show/r90XWgjK9xOMgk25",
"2024-05-03[和NO总双人战棋]": "https://v.douyu.com/show/Aox276DlE4KWVz8Z",
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
