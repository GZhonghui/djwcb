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
"饥荒": "/game23",
"原神": "/game24",
"团建": "/game25",
"文盲杯": "/game26",
"海上狼人杀": "/game27",
"饥荒（联机）": "/game28",
"暗黑地牢": "/game29",
"暴雪游戏水友赛": "/game30",
"永劫无间": "/game31",
"糖豆人": "/game32",
"暗黑地牢2": "/game33",
"植物大战僵尸95版": "/game34",
"捣蛋猪": "/game35",
"Propnight (玉米地)": "/game36",
"飞跃13号房": "/game37",
"8个笨比": "/game38",
"卧龙": "/game39",
"森林2": "/game40",
"森林之子": "/game41",
"炉石战棋": "/game42",
"生化危机4": "/game43",
"抓鬼": "/game44",
"进击要塞": "/game45",
"Dark and Darker": "/game46",
"宋上繁华": "/game47",
"Dota自走棋": "/game48",
"英雄乱斗": "/game49",
"神界原罪2": "/game50",
"Only Up": "/game51",
"环世界": "/game52",
"60秒": "/game53",
"60秒2": "/game54",
"泰坦之魂": "/game55",
"潜水员戴夫": "/game56",
"全面战争模拟器": "/game57",
"炉石答题王": "/game58",
"雀魂": "/game59",
"整蛊邻居": "/game60",
"母胎单身": "/game61",
"三伏": "/game62",
"牢头生日": "/game63",
"请神See": "/game64",
"回到九龙": "/game65",
"异起看": "/game66",
"边境检察官": "/game67",
"动物派对": "/game68",
"杀戮尖塔": "/game69",
"水浒传": "/game70",
"月圆之夜": "/game71",
"饥荒（巨人国）": "/game72",
"完蛋！我被美女包围了": "/game73",
"天际线2": "/game74",
"匹诺曹的谎言": "/game75",
"植物大战僵尸随机版": "/game76",
"孢子": "/game77",
"暖雪": "/game78",
"致命公司": "/game79",
"恐怖录像带": "/game80",
"漫漫长夜": "/game81",
"这是我的战争": "/game82",
"失心疯": "/game83",
"幻兽帕鲁": "/game84",
"奕仙牌": "/game85",
"逆转裁判456": "/game86",
"三国志战棋版": "/game87",
"爆战兄弟": "/game88",
"西游记": "/game89",
"请回答1988": "/game90",
"绝命毒师": "/game91",
"逆转裁判1-5": "/game92",
"掘地求升2": "/game93",
"小丑牌": "/game94",
"烈火英雄": "/game95",
"塔瑞斯世界": "/game96",
"风骚律师": "/game97",
"云顶之弈": "/game98",
"冰汽时代": "/game99",
"美女别打扰我学习": "/game100",
"冰汽时代2": "/game101",
"背包乱斗": "/game102",
"恶意不息": "/game103",
"奥日2": "/game104",
"哈迪斯2": "/game105",
"女鬼桥2": "/game106",
"蟹蟹寻宝奇遇": "/game107",
"植物大战僵尸杂交版": "/game108",
"弈仙派": "/game109",
"老师生日": "/game110",
"法环DLC 黄金树幽影": "/game111",
"女儿生日": "/game112",
"气球塔防6": "/game113",
"漫长的季节": "/game114",
"火山的女儿": "/game115",
"求生岛 不老泉传说": "/game116",
"我为情狂": "/game117",
"风暴之城": "/game118",
"以撒": "/game119",
"王国保卫战5": "/game120",
"中国式网游": "/game121",
"黑神话：悟空": "/game122",
"深海迷航": "/game123",
"漫威终极逆转": "/game124",
"逆转检察官": "/game125",
"超级键盘侠": "/game126",
"答题活动": "/game127",
"逆转检察官2": "/game128",
"美女室友竟然": "/game129",
"战神5": "/game130",
"关山大道路人王": "/game131",
"专业人士": "/game132",
"中国式网游DLC": "/game133",
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
