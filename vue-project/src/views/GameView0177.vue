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
"2024-10-13": "https://v.douyu.com/show/2V0JMVQ1baq7RY5k",
"2024-10-15": "https://v.douyu.com/show/85BAvqQGGERvG4Lm",
"2024-10-16": "https://v.douyu.com/show/JmbBMkoR530M40XA",
"2024-10-17": "https://v.douyu.com/show/jNBdvnbRxwzvE2yw",
"2024-10-18": "https://v.douyu.com/show/wLjGvLrA0laMmO90",
"2024-10-22": "https://v.douyu.com/show/wLjGvLrALwNMmO90",
"2024-10-23": "https://v.douyu.com/show/mPyq7obYzajv1gLY",
"2024-10-25": "https://v.douyu.com/show/wLjGvLrKl3RMmO90",
"2024-10-27": "https://v.douyu.com/show/yVY8WwD41BzvLOz9",
"2024-10-28": "https://v.douyu.com/show/8KxjMdl1kmPMVLwb",
"2024-10-29": "https://v.douyu.com/show/aRbBv3Y8X3oM6PYV",
"2024-10-30": "https://v.douyu.com/show/kDe0W2gy48nvA4Bz",
"2024-11-01": "https://v.douyu.com/show/6Aw87OQKRLDWYGkg",
"2024-11-03": "https://v.douyu.com/show/aRbBv3Y8gmYM6PYV",
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
