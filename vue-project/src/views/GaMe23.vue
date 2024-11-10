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
"2023-01-04": "https://v.douyu.com/show/kDe0W2mz68XMA4Bz",
"2023-01-07": "https://v.douyu.com/show/GnzXvb9d5KbW462l",
"2023-01-18": "https://v.douyu.com/show/yVmjvBbRxwdvqkNb",
"2023-01-19": "https://v.douyu.com/show/wLjGvLqkx3x7mO90",
"2023-10-05": "https://v.douyu.com/show/LDBbMANQbRJWyJRP",
"2023-10-06": "https://v.douyu.com/show/yVY8Wwd0EoPvLOz9",
"2023-10-07": "https://v.douyu.com/show/wLjGvLxkkw0vmO90",
"2023-10-08": "https://v.douyu.com/show/85BAvq8np3eWG4Lm",
"2023-10-10[蜂后]": "https://v.douyu.com/show/jNBdvn80NxqME2yw",
"2023-10-11": "https://v.douyu.com/show/LDBbMANQjVVWyJRP",
"2023-10-13": "https://v.douyu.com/show/6Aw87O8365XMYGkg",
"2023-10-14": "https://v.douyu.com/show/a4Jj7l8adQj7Dk01",
"2023-10-15": "https://v.douyu.com/show/mPyq7o8PEr5M1gLY",
"2023-10-17": "https://v.douyu.com/show/wLjGvLxz99avmO90",
"2023-10-18": "https://v.douyu.com/show/Kg1VWR8JlqQ7GbNA",
"2023-10-20": "https://v.douyu.com/show/jwzOvpxDwzEvZVRm",
"2023-10-24": "https://v.douyu.com/show/2V0JMVGkknAWRY5k",
"2023-10-25": "https://v.douyu.com/show/ZB5Kv9Y0R6bva93x",
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
