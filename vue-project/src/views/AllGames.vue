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
"PUBG": "/game2",
"只狼": "/game3",
"茶杯头": "/game4",
"战神": "/game5",
"亿万僵尸": "/game6",
"炉石活动": "/game7",
"王国保卫战4": "/game8",
"守望先锋": "/game9",
"户外": "/game10",
"魔兽世界": "/game11",
"神都不良探": "/game12",
"土豆兄弟": "/game13",
"神秘海域": "/game14",
"生化危机8 DLC": "/game15",
"三国演义": "/game16",
"三国志14": "/game17",
"大多数": "/game18",
"鸭鸭杀": "/game19",
"同舟共济": "/game20",
"Only Up": "/game21",
"环世界": "/game22",
"60秒": "/game23",
"60秒2": "/game24",
"泰坦之魂": "/game25",
"潜水员戴夫": "/game26",
"以撒": "/game27",
"王国保卫战5": "/game28",
"中国式网游": "/game29",
"黑神话：悟空": "/game30",
"深海迷航": "/game31",
"漫威终极逆转": "/game32",
"逆转检察官": "/game33",
"超级键盘侠": "/game34",
"答题活动": "/game35",
"逆转检察官2": "/game36",
"美女室友竟然": "/game37",
"战神5": "/game38",
"关山大道路人王": "/game39",
"专业人士": "/game40",
"中国式网游DLC": "/game41",
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
