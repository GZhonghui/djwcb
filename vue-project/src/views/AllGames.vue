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
"Only Up": "/game1",
"环世界": "/game2",
"60秒": "/game3",
"60秒2": "/game4",
"泰坦之魂": "/game5",
"潜水员戴夫": "/game6",
"以撒": "/game7",
"王国保卫战5": "/game8",
"中国式网游": "/game9",
"黑神话：悟空": "/game10",
"户外": "/game11",
"深海迷航": "/game12",
"漫威终极逆转": "/game13",
"逆转检察官": "/game14",
"超级键盘侠": "/game15",
"答题活动": "/game16",
"逆转检察官2": "/game17",
"美女室友竟然": "/game18",
"战神5": "/game19",
"关山大道路人王": "/game20",
"专业人士": "/game21",
"中国式网游DLC": "/game22",
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
