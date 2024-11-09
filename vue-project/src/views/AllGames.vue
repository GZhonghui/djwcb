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
"原神": "/game21",
"团建": "/game22",
"文盲杯": "/game23",
"海上狼人杀": "/game24",
"饥荒": "/game25",
"饥荒（联机）": "/game26",
"暗黑地牢": "/game27",
"永劫无间": "/game28",
"糖豆人": "/game29",
"暗黑地牢2": "/game30",
"植物大战僵尸95版": "/game31",
"捣蛋猪": "/game32",
"飞跃13号房": "/game33",
"Propnight (玉米地)": "/game34",
"卧龙": "/game35",
"森林2": "/game36",
"炉石战棋": "/game37",
"生化危机4": "/game38",
"进击要塞": "/game39",
"宋上繁华": "/game40",
"Only Up": "/game41",
"环世界": "/game42",
"60秒": "/game43",
"60秒2": "/game44",
"泰坦之魂": "/game45",
"潜水员戴夫": "/game46",
"杀戮尖塔": "/game47",
"匹诺曹的谎言": "/game48",
"植物大战僵尸随机版": "/game49",
"孢子": "/game50",
"暖雪": "/game51",
"漫漫长夜": "/game52",
"小丑牌": "/game53",
"风骚律师": "/game54",
"以撒": "/game55",
"王国保卫战5": "/game56",
"中国式网游": "/game57",
"黑神话：悟空": "/game58",
"深海迷航": "/game59",
"漫威终极逆转": "/game60",
"逆转检察官": "/game61",
"超级键盘侠": "/game62",
"答题活动": "/game63",
"逆转检察官2": "/game64",
"美女室友竟然": "/game65",
"战神5": "/game66",
"关山大道路人王": "/game67",
"专业人士": "/game68",
"中国式网游DLC": "/game69",
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
