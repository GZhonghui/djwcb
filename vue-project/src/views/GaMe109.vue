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
"2023-07-11": "https://v.douyu.com/show/0zZVvPo9mOmWO4E2",
"2023-07-14": "https://v.douyu.com/show/Kg1VWR84Jjm7GbNA",
"2023-07-25": "https://v.douyu.com/show/DrwnvzgDAzn7PNaX",
"2023-07-26": "https://v.douyu.com/show/1LDR7QZRJR6MJzx8",
"2023-07-30": "https://v.douyu.com/show/85BAvq8QykbWG4Lm",
"2023-08-01[有比赛]": "https://v.douyu.com/show/LDBbMANA43BWyJRP",
"2023-08-03[有比赛]": "https://v.douyu.com/show/kDe0W2Dkk387A4Bz",
"2023-08-18": "https://v.douyu.com/show/Aox276De2e2WVz8Z",
"2023-08-30": "https://v.douyu.com/show/8pa9v5NXLpR7VrqA",
"2023-11-30": "https://v.douyu.com/show/n8GzMX8e0r1M6qyP",
"2023-12-01[比赛海选]": "https://v.douyu.com/show/yVY8WwdpDLVvLOz9",
"2023-12-11[比赛-16强]": "https://v.douyu.com/show/qJgOWxgwRLZMkVzL",
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
