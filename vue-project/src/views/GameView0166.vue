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
"2024-07-21": "https://v.douyu.com/show/mPyq7ob334Vv1gLY",
"2024-07-22": "https://v.douyu.com/show/DrwnvzD8Z3mMPNaX",
"2024-07-23": "https://v.douyu.com/show/ERALvEqajBnv1Vw0",
"2024-07-24": "https://v.douyu.com/show/Kg1VWRQOYBDMGbNA",
"2024-07-26": "https://v.douyu.com/show/jwzOvp1ObNq7ZVRm",
"2024-07-30": "https://v.douyu.com/show/8pa9v5e54jKvVrqA",
"2024-07-31[月末放羊]": "https://v.douyu.com/show/DO84vrRBk6YvedGr",
"2024-08-02": "https://v.douyu.com/show/Qyz171l5Oa1vBJj9",
"2024-08-03": "https://v.douyu.com/show/1LDR7QR8RABMJzx8",
"2024-08-04": "https://v.douyu.com/show/NbwE7ZYlAJPvn5Zz",
"2024-08-06": "https://v.douyu.com/show/a2JEMJJ20ZYMNxml",
"2024-08-07": "https://v.douyu.com/show/XqeO74NgYl2WxywG",
"2024-08-13": "https://v.douyu.com/show/yVY8WwD315LvLOz9",
"2024-08-14": "https://v.douyu.com/show/ZB5Kv9grebbMa93x",
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
@import "@/styles/common.css";
</style>
