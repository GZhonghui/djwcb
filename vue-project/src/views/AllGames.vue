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
"太吾绘卷": "/game8",
"王国保卫战3": "/game9",
"王国保卫战4": "/game10",
"守望先锋": "/game11",
"户外": "/game12",
"魔兽世界": "/game13",
"神都不良探": "/game14",
"土豆兄弟": "/game15",
"神秘海域": "/game16",
"生化危机8 DLC": "/game17",
"三国演义": "/game18",
"三国志14": "/game19",
"大多数": "/game20",
"鸭鸭杀": "/game21",
"同舟共济": "/game22",
"原神": "/game23",
"团建": "/game24",
"文盲杯": "/game25",
"海上狼人杀": "/game26",
"饥荒": "/game27",
"饥荒（联机）": "/game28",
"暗黑地牢": "/game29",
"永劫无间": "/game30",
"糖豆人": "/game31",
"暗黑地牢2": "/game32",
"植物大战僵尸95版": "/game33",
"捣蛋猪": "/game34",
"飞跃13号房": "/game35",
"Propnight (玉米地)": "/game36",
"卧龙": "/game37",
"森林2": "/game38",
"炉石战棋": "/game39",
"生化危机4": "/game40",
"进击要塞": "/game41",
"宋上繁华": "/game42",
"Only Up": "/game43",
"环世界": "/game44",
"60秒": "/game45",
"60秒2": "/game46",
"泰坦之魂": "/game47",
"潜水员戴夫": "/game48",
"杀戮尖塔": "/game49",
"匹诺曹的谎言": "/game50",
"植物大战僵尸随机版": "/game51",
"孢子": "/game52",
"暖雪": "/game53",
"漫漫长夜": "/game54",
"这是我的战争": "/game55",
"失心疯": "/game56",
"幻兽帕鲁": "/game57",
"奕仙牌": "/game58",
"逆转裁判456": "/game59",
"三国志战棋版": "/game60",
"爆战兄弟": "/game61",
"西游记": "/game62",
"请回答1988": "/game63",
"绝命毒师": "/game64",
"逆转裁判1-5": "/game65",
"掘地求升2": "/game66",
"小丑牌": "/game67",
"烈火英雄": "/game68",
"塔瑞斯世界": "/game69",
"风骚律师": "/game70",
"云顶之弈": "/game71",
"冰汽时代": "/game72",
"美女别打扰我学习": "/game73",
"冰汽时代2": "/game74",
"背包乱斗": "/game75",
"恶意不息": "/game76",
"奥日2": "/game77",
"哈迪斯2": "/game78",
"女鬼桥2": "/game79",
"蟹蟹寻宝奇遇": "/game80",
"植物大战僵尸杂交版": "/game81",
"弈仙派": "/game82",
"老师生日": "/game83",
"法环DLC 黄金树幽影": "/game84",
"女儿生日": "/game85",
"气球塔防6": "/game86",
"漫长的季节": "/game87",
"火山的女儿": "/game88",
"求生岛 不老泉传说": "/game89",
"我为情狂": "/game90",
"风暴之城": "/game91",
"以撒": "/game92",
"王国保卫战5": "/game93",
"中国式网游": "/game94",
"黑神话：悟空": "/game95",
"深海迷航": "/game96",
"漫威终极逆转": "/game97",
"逆转检察官": "/game98",
"超级键盘侠": "/game99",
"答题活动": "/game100",
"逆转检察官2": "/game101",
"美女室友竟然": "/game102",
"战神5": "/game103",
"关山大道路人王": "/game104",
"专业人士": "/game105",
"中国式网游DLC": "/game106",
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
