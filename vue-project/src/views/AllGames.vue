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
"王国保卫战4": "/game1",
"守望先锋": "/game2",
"户外": "/game3",
"魔兽世界": "/game4",
"亿万僵尸": "/game5",
"神都不良探": "/game6",
"土豆兄弟": "/game7",
"Only Up": "/game8",
"环世界": "/game9",
"60秒": "/game10",
"60秒2": "/game11",
"泰坦之魂": "/game12",
"潜水员戴夫": "/game13",
"以撒": "/game14",
"王国保卫战5": "/game15",
"中国式网游": "/game16",
"黑神话：悟空": "/game17",
"深海迷航": "/game18",
"漫威终极逆转": "/game19",
"逆转检察官": "/game20",
"超级键盘侠": "/game21",
"答题活动": "/game22",
"逆转检察官2": "/game23",
"美女室友竟然": "/game24",
"战神5": "/game25",
"关山大道路人王": "/game26",
"专业人士": "/game27",
"中国式网游DLC": "/game28",
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
