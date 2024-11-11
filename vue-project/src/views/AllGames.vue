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
"港诡实录": "/game20",
"纸人": "/game21",
"甜蜜之家": "/game22",
"疑案追声": "/game23",
"疑案追声dlc": "/game24",
"奥日2": "/game25",
"cod16": "/game26",
"生化危机3": "/game27",
"风暴": "/game28",
"纸人2": "/game29",
"底特律变人": "/game30",
"茶杯头": "/game31",
"怪猎": "/game32",
"动物派对": "/game33",
"空洞骑士": "/game34",
"山中凶宅": "/game35",
"赛博朋克2077": "/game36",
"dota2": "/game37",
"地平线4": "/game38",
"戴森球": "/game39",
"烟火": "/game40",
"仁王2+dlc": "/game41",
"小小梦魇2": "/game42",
"赏金奇兵3": "/game43",
"生化危机8": "/game44",
"生化危机2重制版": "/game45",
"挺进地牢": "/game46",
"节奏医生": "/game47",
"饥荒": "/game48",
"泰拉瑞亚": "/game49",
"暗黑地牢": "/game50",
"消光2": "/game51",
"艾尔登法环": "/game52",
"逆转裁判": "/game53",
"魔兽怀旧服": "/game54",
"千爵史诗": "/game55",
"战神": "/game56",
"茶杯头dlc": "/game57",
"亿万僵尸": "/game58",
"女鬼桥": "/game59",
"王国保卫战": "/game60",
"ow": "/game61",
"神都不良探": "/game62",
"土豆兄弟": "/game63",
"神海4": "/game64",
"大多数": "/game65",
"三国志14": "/game66",
"生化危机8 DLC": "/game67",
"炉石活动": "/game68",
"太吾绘卷": "/game69",
"王国保卫战3": "/game70",
"王国保卫战4": "/game71",
"守望先锋": "/game72",
"神秘海域": "/game73",
"三国演义": "/game74",
"鸭鸭杀": "/game75",
"同舟共济": "/game76",
"原神": "/game77",
"团建": "/game78",
"文盲杯": "/game79",
"海上狼人杀": "/game80",
"饥荒（联机）": "/game81",
"暴雪游戏水友赛": "/game82",
"永劫无间": "/game83",
"糖豆人": "/game84",
"暗黑地牢2": "/game85",
"植物大战僵尸95版": "/game86",
"捣蛋猪": "/game87",
"Propnight (玉米地)": "/game88",
"飞跃13号房": "/game89",
"8个笨比": "/game90",
"卧龙": "/game91",
"森林之子": "/game92",
"生化危机4": "/game93",
"抓鬼": "/game94",
"进击要塞": "/game95",
"Dark and Darker": "/game96",
"宋上繁华": "/game97",
"Dota自走棋": "/game98",
"英雄乱斗": "/game99",
"神界原罪2": "/game100",
"Only Up": "/game101",
"环世界": "/game102",
"60秒": "/game103",
"60秒2": "/game104",
"泰坦之魂": "/game105",
"潜水员戴夫": "/game106",
"全面战争模拟器": "/game107",
"炉石答题王": "/game108",
"雀魂": "/game109",
"整蛊邻居": "/game110",
"母胎单身": "/game111",
"三伏": "/game112",
"牢头生日": "/game113",
"请神See": "/game114",
"回到九龙": "/game115",
"边境检察官": "/game116",
"杀戮尖塔": "/game117",
"水浒传": "/game118",
"月圆之夜": "/game119",
"饥荒（巨人国）": "/game120",
"完蛋！我被美女包围了": "/game121",
"天际线2": "/game122",
"匹诺曹的谎言": "/game123",
"植物大战僵尸随机版": "/game124",
"孢子": "/game125",
"暖雪": "/game126",
"致命公司": "/game127",
"恐怖录像带": "/game128",
"漫漫长夜": "/game129",
"这是我的战争": "/game130",
"失心疯": "/game131",
"幻兽帕鲁": "/game132",
"奕仙牌": "/game133",
"逆转裁判456": "/game134",
"三国志战棋版": "/game135",
"爆战兄弟": "/game136",
"西游记": "/game137",
"请回答1988": "/game138",
"绝命毒师": "/game139",
"逆转裁判1-5": "/game140",
"掘地求升2": "/game141",
"小丑牌": "/game142",
"烈火英雄": "/game143",
"塔瑞斯世界": "/game144",
"风骚律师": "/game145",
"云顶之弈": "/game146",
"冰汽时代": "/game147",
"美女别打扰我学习": "/game148",
"冰汽时代2": "/game149",
"背包乱斗": "/game150",
"恶意不息": "/game151",
"哈迪斯2": "/game152",
"女鬼桥2": "/game153",
"蟹蟹寻宝奇遇": "/game154",
"植物大战僵尸杂交版": "/game155",
"弈仙牌": "/game156",
"老师生日": "/game157",
"法环DLC 黄金树幽影": "/game158",
"女儿生日": "/game159",
"气球塔防6": "/game160",
"漫长的季节": "/game161",
"火山的女儿": "/game162",
"求生岛 不老泉传说": "/game163",
"我为情狂": "/game164",
"风暴之城": "/game165",
"以撒": "/game166",
"王国保卫战5": "/game167",
"中国式网游": "/game168",
"黑神话：悟空": "/game169",
"深海迷航": "/game170",
"漫威终极逆转": "/game171",
"逆转检察官": "/game172",
"超级键盘侠": "/game173",
"答题活动": "/game174",
"逆转检察官2": "/game175",
"美女室友竟然": "/game176",
"战神5": "/game177",
"关山大道路人王": "/game178",
"专业人士": "/game179",
"中国式网游DLC": "/game180",
      }
    };
  },
  methods: {
    go(link) {
      if (link) if (link.startsWith('/')) {
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
