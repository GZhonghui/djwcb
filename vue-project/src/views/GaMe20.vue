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
"2022-07-01": "https://v.douyu.com/show/Kg1VWRB2njQWGbNA",
"2022-07-08": "https://v.douyu.com/show/DrwnvzKq8wQ7PNaX",
"2022-07-09": "https://v.douyu.com/show/ZB5Kv9o0O38Ma93x",
"2022-07-10": "https://v.douyu.com/show/0Q8mMYGogoNv49Ad",
"2022-07-12": "https://v.douyu.com/show/DO84vr92PrQWedGr",
"2022-07-13": "https://v.douyu.com/show/qJgOWxmEjZRvkVzL",
"2020-08-27[断了一截，9-16续上，和怪猎一起]": "",
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
