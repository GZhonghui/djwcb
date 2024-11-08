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
"炉石登顶": "/game1",
"王国保卫战4": "/game2",
"守望先锋": "/game3",
"户外": "/game4",
"魔兽世界": "/game5",
"亿万僵尸": "/game6",
"神都不良探": "/game7",
"土豆兄弟": "/game8",
"神秘海域": "/game9",
"生化危机8 DLC": "/game10",
"三国演义": "/game11",
"三国志14": "/game12",
"大多数": "/game13",
"鸭鸭杀": "/game14",
"同舟共济": "/game15",
"Only Up": "/game16",
"环世界": "/game17",
"60秒": "/game18",
"60秒2": "/game19",
"泰坦之魂": "/game20",
"潜水员戴夫": "/game21",
"以撒": "/game22",
"王国保卫战5": "/game23",
"中国式网游": "/game24",
"黑神话：悟空": "/game25",
"深海迷航": "/game26",
"漫威终极逆转": "/game27",
"逆转检察官": "/game28",
"超级键盘侠": "/game29",
"答题活动": "/game30",
"逆转检察官2": "/game31",
"美女室友竟然": "/game32",
"战神5": "/game33",
"关山大道路人王": "/game34",
"专业人士": "/game35",
"中国式网游DLC": "/game36",
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
