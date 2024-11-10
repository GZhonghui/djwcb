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
"回到首页": "/",
"2024-09-27": "https://v.douyu.com/show/Yo4evyDgeDRW8L62",
"2024-09-28": "https://v.douyu.com/show/2V0JMVQGzqb7RY5k",
"2024-09-29": "https://v.douyu.com/show/0Q8mMY55krmM49Ad",
"2024-10-01": "https://v.douyu.com/show/kDe0W2ggDrPvA4Bz",
"2024-10-02": "https://v.douyu.com/show/kDe0W2ggy8ovA4Bz",
"2024-10-04": "https://v.douyu.com/show/a2JEMJJJ4w2MNxml",
"2024-10-05": "https://v.douyu.com/show/ZB5Kv9ggnemMa93x",
"2024-10-06": "https://v.douyu.com/show/0Q8mMY556x8M49Ad",
"2024-10-07": "https://v.douyu.com/show/85BAvqQQeXwvG4Lm",
"2024-10-09": "https://v.douyu.com/show/Yo4evyDD30NW8L62",
"2024-10-10": "https://v.douyu.com/show/jNBdvnbbnyPvE2yw",
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
