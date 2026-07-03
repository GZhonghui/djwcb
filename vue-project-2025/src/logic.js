import { defineStore } from "pinia"

// 加载数据
async function loadData() {
  // 获取数据
  // 这些数据放在 /public/ 下就能使用 fetch 直接获取
  // 并且在打包时会自动复制到 dist/ 下
  // 如果 JSON 数据较大或可能被更新：都建议放在 public，用 fetch 读取
  // 如果是小型配置文件或固定内容：建议放在 src/assets，用 import
  const index = await fetch("/data/index.json")
  // 将获取到的 JSON 数据转换为 JavaScript 对象
  // 注意：fetch 返回的是一个 Response 对象，需要调用 json() 方法来解析
  const indexData = await index.json()

  let gameList = []
  let gameDict = {}
  let recordDict = {} // id -> []
  let gameCount = 0

  let loadGame = function(date, name, comment, url) {
    if(!(name in gameDict)) { // dict 操作
      gameCount++;
      gameDict[name] = { // 创建 json，字段名有没有引号都可以
        "id": gameCount,
        "title": name,
        "time": date,
        "days": 0,
      }
      recordDict[gameCount] = []
    }
    let game = gameDict[name];
    // 记录该游戏“最新一条记录”的日期（日期是 YYYY-MM-DD，可直接按字符串比较）
    // 注意：数据文件并非严格按时间顺序加载（例如 2020_to_2022_misc.json 排在 2021/2022 之前），
    // 所以这里取较大值而不是直接覆盖，才能得到真正的最新日期
    if (date > game["time"]) {
      game["time"] = date;
    }
    game["days"]++;

    let id = game["id"]
    let recordID = recordDict[id].length + 1 // list 长度
    recordDict[id].push({
      id: recordID,
      title: date,
      comment: comment,
      url: url
    })
  }

  let loadDay = function(date, today) {
    for(const game of today.games) {
      // 判断是不是字符串
      if(typeof game === 'string' || game instanceof String) {
        loadGame(date, game, "", today.url)
      }
      // 判断是不是数组
      if(Array.isArray(game)) {
        loadGame(date, game[0], game[1], today.url)
      }
    }
  }

  let loadFile = function(json) {
    for(const date in json) {
      let today = json[date]
      loadDay(date, today)
    }
  }

  for(const fileName of indexData.files) {
    // 字符串拼接
    const response = await fetch(`/data/${fileName}`)
    const json = await response.json()
    loadFile(json)
  }

  // 将游戏列表转换为数组，按“最新记录日期”降序排序：最近玩过的游戏排在最前面
  // 日期相同时，用 id 降序作为稳定的次级排序
  gameList = Object.values(gameDict).sort((a, b) => {
    if (a.time !== b.time) {
      return a.time < b.time ? 1 : -1
    }
    return b.id - a.id
  });

  return {
    "files": indexData.files,
    "games": gameList,
    "records": recordDict
  }
}

// 定义 Pinia 状态管理的 store
// 这个 store 用于处理静态数据的加载和状态管理
// 使用 defineStore 定义一个名为 "StaticData" 的 store
// 不是很理解这种写法，但是就是这么写的
export const useStaticDataStore = defineStore("StaticData", {
  // 定义 store 的状态和数据本身
  state: () => ({
    data: null,
    isReady: false,
    loading: false,
    error: null,
    search_str: "",
  }),
  // 定义 store 的函数
  actions: {
    // 可以是异步函数
    async init() {
      if (this.isReady || this.loading) return
      try {
        this.loading = true
        // 异步函数中可以使用 await
        // 调用 loadData 函数加载数据
        // 并将结果赋值给 this.data
        this.data = await loadData()
        this.isReady = true
      } catch (e) {
        this.error = e
        console.error(e)
      } finally {
        this.loading = false
      }
    },
    updateSearchStr(new_str) {
      this.search_str = new_str
    }
  }
})