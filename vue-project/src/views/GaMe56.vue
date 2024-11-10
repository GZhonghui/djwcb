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
"2023-06-27": "https://v.douyu.com/show/X3JzMaQVGx9MPQro",
"2023-06-28": "https://v.douyu.com/show/ERALvE8wbw5W1Vw0",
"2023-06-30": "https://v.douyu.com/show/ERALvE8w1dDW1Vw0",
"2023-07-01": "https://v.douyu.com/show/X3JzMaQVn5AMPQro",
"2023-07-02": "https://v.douyu.com/show/qJgOWxgOqQKMkVzL",
"2023-07-03": "https://v.douyu.com/show/NbwE7Z8VrlBWn5Zz",
"2023-07-04": "https://v.douyu.com/show/brN0MmxzOme7pyxA",
"2023-07-05": "https://v.douyu.com/show/NVm0WKNZzNwMJeBP",
"2023-07-06": "https://v.douyu.com/show/1LDR7QZla86MJzx8",
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
