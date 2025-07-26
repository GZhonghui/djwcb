import { defineStore } from "pinia"

async function loadData() {
  const index = await fetch("/data/index.json")
  const indexData = await index.json()

  let gameList = []
  let gameDict = {}
  let gameCount = 0

  let loadGame = function(date, name, comment, url) {
    if(!(name in gameDict)) {
      gameCount++;
      gameDict[name] = {
        "id": gameCount,
        "title": name,
        "time": date,
        "days": 0,
      }
    }
    let game = gameDict[name];
    game["time"] = date;
    game["days"]++;
  }

  let loadDay = function(date, today) {
    for(const game of today.games) {
      if(typeof game === 'string' || game instanceof String) {
        loadGame(date, game, "", today.url)
      }
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
    const response = await fetch(`/data/${fileName}`)
    const json = await response.json()
    loadFile(json)
  }

  gameList = Object.values(gameDict).sort((a, b) => b.id - a.id);

  return {
    "files": indexData.files,
    "games": gameList
  }
}

export const useStaticDataStore = defineStore("StaticData", {
  state: () => ({
    data: null,
    isReady: false,
    loading: false,
    error: null
  }),
  actions: {
    async init() {
      if (this.isReady || this.loading) return
      try {
        this.loading = true
        this.data = await loadData()
        this.isReady = true
      } catch (e) {
        this.error = e
        console.error(e)
      } finally {
        this.loading = false
      }
    }
  }
})