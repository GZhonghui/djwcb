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
"2019-05-21[拍婚纱照]": "https://v.douyu.com/show/yVY8WwAnBYA7LOz9",
"2022-10-03": "https://v.douyu.com/show/0zZVvPA42KE7O4E2",
"2022-11-23": "https://v.douyu.com/show/DrwnvzZP62nvPNaX",
"2023-01-21": "https://v.douyu.com/show/2V0JMVVRnxEMRY5k",
"2023-05-16": "https://v.douyu.com/show/2V0JMVGBOlAWRY5k",
"2023-05-17[状态太差，旅游一周]": "https://v.douyu.com/show/wLjGvLxoaY0vmO90",
"2023-09-11[宁波象山]": "https://v.douyu.com/show/2V0JMVGdYwkWRY5k",
"2023-09-12[宁波象山]": "https://v.douyu.com/show/kDe0W2Djjb87A4Bz",
"2023-09-13[宁波象山]": "https://v.douyu.com/show/85BAvq8wPXwWG4Lm",
"2023-10-02[钓鱼]": "https://v.douyu.com/show/jNBdvn8knARME2yw",
"2023-10-16[钓鱼]": "https://v.douyu.com/show/ZB5Kv9YjkPKva93x",
"2024-02-09[大年夜，户外烟花]": "https://v.douyu.com/show/brN0Mmxkjr57pyxA",
"2024-04-29[大鲤鱼]": "https://v.douyu.com/show/mPyq7o8OVrmM1gLY",
"2024-05-13[周一钓鱼]": "https://v.douyu.com/show/ZB5Kv9YN8j2va93x",
"2024-05-20[钓鱼]": "https://v.douyu.com/show/a2JEMJnRN3DMNxml",
"2024-07-28[小戴在CJ]": "https://v.douyu.com/show/jNBdvnbVKQzvE2yw",
"2024-08-28": "https://v.douyu.com/show/JmbBMkolAxKM40XA",
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
