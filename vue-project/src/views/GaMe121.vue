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
"2024-05-22": "https://v.douyu.com/show/Aox276YpkR0vVz8Z",
"2024-05-24": "https://v.douyu.com/show/qJgOWx5o5PRvkVzL",
"2024-05-25": "https://v.douyu.com/show/Kg1VWRQVE1PMGbNA",
"2024-05-26": "https://v.douyu.com/show/jNBdvnbmxrNvE2yw",
"2024-05-28": "https://v.douyu.com/show/DO84vrRkd0lvedGr",
"2024-05-29": "https://v.douyu.com/show/2V0JMVQB2Y47RY5k",
"2024-05-30[周末放羊，加农炮]": "https://v.douyu.com/show/ZB5Kv9gx6dmMa93x",
"2024-06-03[传奇！女大一]": "https://v.douyu.com/show/yVmjvBgxN457qkNb",
"2024-06-06": "https://v.douyu.com/show/mPyq7obJxeqv1gLY",
"2024-06-07": "https://v.douyu.com/show/DrwnvzDylkGMPNaX",
"2024-06-08[终于过关女大一！]": "https://v.douyu.com/show/Qyz171lwVyQvBJj9",
"2024-06-09": "https://v.douyu.com/show/6Aw87OQ2XooWYGkg",
"2024-06-12": "https://v.douyu.com/show/0zZVvPQz62Y7O4E2",
"2024-06-13": "https://v.douyu.com/show/8pa9v5ep4ZavVrqA",
"2024-06-14": "https://v.douyu.com/show/XqeO74NxQKrWxywG",
"2024-06-15": "https://v.douyu.com/show/3rob7joD2DKMgkZl",
"2024-06-16": "https://v.douyu.com/show/JmbBMkoGb1QM40XA",
"2024-06-18": "https://v.douyu.com/show/X3JzMalJeNl7PQro",
"2024-06-19": "https://v.douyu.com/show/a4Jj7lBl42rWDk01",
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
