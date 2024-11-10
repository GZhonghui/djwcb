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
"COS": "/game3",
"闲聊": "/game4",
"户外": "/game5",
"魔兽世界": "/game6",
"结婚": "/game7",
"炉石战棋": "/game8",
"LOL": "/game9",
"夜嫁": "/game10",
"层层恐惧": "/game11",
"心魔": "/game12",
"COD16 大逃杀": "/game13",
"甜蜜之家2": "/game14",
"异起See": "/game15",
"隐形守护者": "/game16",
"风暴英雄": "/game17",
"盗贼之海": "/game18",
"只狼": "/game19",
"茶杯头": "/game20",
"战神": "/game21",
"亿万僵尸": "/game22",
"炉石活动": "/game23",
"太吾绘卷": "/game24",
"王国保卫战3": "/game25",
"王国保卫战4": "/game26",
"守望先锋": "/game27",
"神都不良探": "/game28",
"土豆兄弟": "/game29",
"神秘海域": "/game30",
"生化危机8 DLC": "/game31",
"三国演义": "/game32",
"三国志14": "/game33",
"大多数": "/game34",
"鸭鸭杀": "/game35",
"同舟共济": "/game36",
"饥荒": "/game37",
"原神": "/game38",
"团建": "/game39",
"文盲杯": "/game40",
"海上狼人杀": "/game41",
"饥荒（联机）": "/game42",
"暗黑地牢": "/game43",
"暴雪游戏水友赛": "/game44",
"永劫无间": "/game45",
"糖豆人": "/game46",
"暗黑地牢2": "/game47",
"植物大战僵尸95版": "/game48",
"捣蛋猪": "/game49",
"Propnight (玉米地)": "/game50",
"飞跃13号房": "/game51",
"8个笨比": "/game52",
"卧龙": "/game53",
"森林2": "/game54",
"森林之子": "/game55",
"生化危机4": "/game56",
"抓鬼": "/game57",
"进击要塞": "/game58",
"Dark and Darker": "/game59",
"宋上繁华": "/game60",
"Dota自走棋": "/game61",
"英雄乱斗": "/game62",
"神界原罪2": "/game63",
"Only Up": "/game64",
"环世界": "/game65",
"60秒": "/game66",
"60秒2": "/game67",
"泰坦之魂": "/game68",
"潜水员戴夫": "/game69",
"全面战争模拟器": "/game70",
"炉石答题王": "/game71",
"雀魂": "/game72",
"整蛊邻居": "/game73",
"母胎单身": "/game74",
"三伏": "/game75",
"牢头生日": "/game76",
"请神See": "/game77",
"回到九龙": "/game78",
"异起看": "/game79",
"边境检察官": "/game80",
"动物派对": "/game81",
"杀戮尖塔": "/game82",
"水浒传": "/game83",
"月圆之夜": "/game84",
"饥荒（巨人国）": "/game85",
"完蛋！我被美女包围了": "/game86",
"天际线2": "/game87",
"匹诺曹的谎言": "/game88",
"植物大战僵尸随机版": "/game89",
"孢子": "/game90",
"暖雪": "/game91",
"致命公司": "/game92",
"恐怖录像带": "/game93",
"漫漫长夜": "/game94",
"这是我的战争": "/game95",
"失心疯": "/game96",
"幻兽帕鲁": "/game97",
"奕仙牌": "/game98",
"逆转裁判456": "/game99",
"三国志战棋版": "/game100",
"爆战兄弟": "/game101",
"西游记": "/game102",
"请回答1988": "/game103",
"绝命毒师": "/game104",
"逆转裁判1-5": "/game105",
"掘地求升2": "/game106",
"小丑牌": "/game107",
"烈火英雄": "/game108",
"塔瑞斯世界": "/game109",
"风骚律师": "/game110",
"云顶之弈": "/game111",
"冰汽时代": "/game112",
"美女别打扰我学习": "/game113",
"冰汽时代2": "/game114",
"背包乱斗": "/game115",
"恶意不息": "/game116",
"奥日2": "/game117",
"哈迪斯2": "/game118",
"女鬼桥2": "/game119",
"蟹蟹寻宝奇遇": "/game120",
"植物大战僵尸杂交版": "/game121",
"弈仙派": "/game122",
"老师生日": "/game123",
"法环DLC 黄金树幽影": "/game124",
"女儿生日": "/game125",
"气球塔防6": "/game126",
"漫长的季节": "/game127",
"火山的女儿": "/game128",
"求生岛 不老泉传说": "/game129",
"我为情狂": "/game130",
"风暴之城": "/game131",
"以撒": "/game132",
"王国保卫战5": "/game133",
"中国式网游": "/game134",
"黑神话：悟空": "/game135",
"深海迷航": "/game136",
"漫威终极逆转": "/game137",
"逆转检察官": "/game138",
"超级键盘侠": "/game139",
"答题活动": "/game140",
"逆转检察官2": "/game141",
"美女室友竟然": "/game142",
"战神5": "/game143",
"关山大道路人王": "/game144",
"专业人士": "/game145",
"中国式网游DLC": "/game146",
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
