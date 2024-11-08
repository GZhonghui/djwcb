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
"神秘海域": "/game8",
"生化危机8 DLC": "/game9",
"三国演义": "/game10",
"三国志14": "/game11",
"大多数": "/game12",
"鸭鸭杀": "/game13",
"同舟共济": "/game14",
"Only Up": "/game15",
"环世界": "/game16",
"60秒": "/game17",
"60秒2": "/game18",
"泰坦之魂": "/game19",
"潜水员戴夫": "/game20",
"以撒": "/game21",
"王国保卫战5": "/game22",
"中国式网游": "/game23",
"黑神话：悟空": "/game24",
"深海迷航": "/game25",
"漫威终极逆转": "/game26",
"逆转检察官": "/game27",
"超级键盘侠": "/game28",
"答题活动": "/game29",
"逆转检察官2": "/game30",
"美女室友竟然": "/game31",
"战神5": "/game32",
"关山大道路人王": "/game33",
"专业人士": "/game34",
"中国式网游DLC": "/game35",
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
