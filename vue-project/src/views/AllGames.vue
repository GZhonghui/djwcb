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
"战旗": "/game20",
"港诡实录": "/game21",
"纸人": "/game22",
"甜蜜之家": "/game23",
"疑案追声": "/game24",
"疑案追声dlc": "/game25",
"奥日2": "/game26",
"cod16": "/game27",
"生化危机3": "/game28",
"风暴": "/game29",
"纸人2": "/game30",
"底特律变人": "/game31",
"茶杯头": "/game32",
"怪猎": "/game33",
"动物派对": "/game34",
"空洞骑士": "/game35",
"山中凶宅": "/game36",
"赛博朋克2077": "/game37",
"dota2": "/game38",
"地平线4": "/game39",
"戴森球": "/game40",
"烟火": "/game41",
"仁王2+dlc": "/game42",
"小小梦魇2": "/game43",
"赏金奇兵3": "/game44",
"生化危机8": "/game45",
"生化危机2重制版": "/game46",
"挺进地牢": "/game47",
"节奏医生": "/game48",
"饥荒": "/game49",
"泰拉瑞亚": "/game50",
"暗黑地牢": "/game51",
"消光2": "/game52",
"艾尔登法环": "/game53",
"逆转裁判": "/game54",
"魔兽怀旧服": "/game55",
"千爵史诗": "/game56",
"战神4": "/game57",
"茶杯头dlc": "/game58",
"亿万僵尸": "/game59",
"女鬼桥": "/game60",
"王国保卫战": "/game61",
"ow": "/game62",
"神都不良探": "/game63",
"土豆兄弟": "/game64",
"神海4": "/game65",
"大多数": "/game66",
"三国志14": "/game67",
"生化危机8dlc": "/game68",
"战神": "/game69",
"炉石活动": "/game70",
"太吾绘卷": "/game71",
"王国保卫战3": "/game72",
"王国保卫战4": "/game73",
"守望先锋": "/game74",
"神秘海域": "/game75",
"生化危机8 DLC": "/game76",
"三国演义": "/game77",
"鸭鸭杀": "/game78",
"同舟共济": "/game79",
"原神": "/game80",
"团建": "/game81",
"文盲杯": "/game82",
"海上狼人杀": "/game83",
"饥荒（联机）": "/game84",
"暴雪游戏水友赛": "/game85",
"永劫无间": "/game86",
"糖豆人": "/game87",
"暗黑地牢2": "/game88",
"植物大战僵尸95版": "/game89",
"捣蛋猪": "/game90",
"Propnight (玉米地)": "/game91",
"飞跃13号房": "/game92",
"8个笨比": "/game93",
"卧龙": "/game94",
"森林之子": "/game95",
"生化危机4": "/game96",
"抓鬼": "/game97",
"进击要塞": "/game98",
"Dark and Darker": "/game99",
"宋上繁华": "/game100",
"Dota自走棋": "/game101",
"英雄乱斗": "/game102",
"神界原罪2": "/game103",
"Only Up": "/game104",
"环世界": "/game105",
"60秒": "/game106",
"60秒2": "/game107",
"泰坦之魂": "/game108",
"潜水员戴夫": "/game109",
"全面战争模拟器": "/game110",
"炉石答题王": "/game111",
"雀魂": "/game112",
"整蛊邻居": "/game113",
"母胎单身": "/game114",
"三伏": "/game115",
"牢头生日": "/game116",
"请神See": "/game117",
"回到九龙": "/game118",
"边境检察官": "/game119",
"杀戮尖塔": "/game120",
"水浒传": "/game121",
"月圆之夜": "/game122",
"饥荒（巨人国）": "/game123",
"完蛋！我被美女包围了": "/game124",
"天际线2": "/game125",
"匹诺曹的谎言": "/game126",
"植物大战僵尸随机版": "/game127",
"孢子": "/game128",
"暖雪": "/game129",
"致命公司": "/game130",
"恐怖录像带": "/game131",
"漫漫长夜": "/game132",
"这是我的战争": "/game133",
"失心疯": "/game134",
"幻兽帕鲁": "/game135",
"奕仙牌": "/game136",
"逆转裁判456": "/game137",
"三国志战棋版": "/game138",
"爆战兄弟": "/game139",
"西游记": "/game140",
"请回答1988": "/game141",
"绝命毒师": "/game142",
"逆转裁判1-5": "/game143",
"掘地求升2": "/game144",
"小丑牌": "/game145",
"烈火英雄": "/game146",
"塔瑞斯世界": "/game147",
"风骚律师": "/game148",
"云顶之弈": "/game149",
"冰汽时代": "/game150",
"美女别打扰我学习": "/game151",
"冰汽时代2": "/game152",
"背包乱斗": "/game153",
"恶意不息": "/game154",
"哈迪斯2": "/game155",
"女鬼桥2": "/game156",
"蟹蟹寻宝奇遇": "/game157",
"植物大战僵尸杂交版": "/game158",
"弈仙牌": "/game159",
"老师生日": "/game160",
"法环DLC 黄金树幽影": "/game161",
"女儿生日": "/game162",
"气球塔防6": "/game163",
"漫长的季节": "/game164",
"火山的女儿": "/game165",
"求生岛 不老泉传说": "/game166",
"我为情狂": "/game167",
"风暴之城": "/game168",
"以撒": "/game169",
"王国保卫战5": "/game170",
"中国式网游": "/game171",
"黑神话：悟空": "/game172",
"深海迷航": "/game173",
"漫威终极逆转": "/game174",
"逆转检察官": "/game175",
"超级键盘侠": "/game176",
"答题活动": "/game177",
"逆转检察官2": "/game178",
"美女室友竟然": "/game179",
"战神5": "/game180",
"关山大道路人王": "/game181",
"专业人士": "/game182",
"中国式网游DLC": "/game183",
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
