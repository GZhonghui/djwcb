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
"2022-07-15": "https://v.douyu.com/show/Kg1VWRBDKJmWGbNA",
"2022-07-17": "https://v.douyu.com/show/qJgOWxm9wRnvkVzL",
"2022-07-19": "https://v.douyu.com/show/85BAvqOZjOKMG4Lm",
"2022-07-26": "https://v.douyu.com/show/85BAvqOpKO1MG4Lm",
"2022-07-27": "https://v.douyu.com/show/6Aw87OZRDVdvYGkg",
"2022-07-28": "https://v.douyu.com/show/r90XWgYmAmQ7gk25",
"2022-07-29": "https://v.douyu.com/show/jwzOvp3NjlLWZVRm",
"2022-07-30": "https://v.douyu.com/show/yVmjvB5JGYAWqkNb",
"2022-08-01": "https://v.douyu.com/show/XqeO744YA8e7xywG",
"2022-08-02": "https://v.douyu.com/show/XqeO744Yr427xywG",
"2022-08-03": "https://v.douyu.com/show/jNBdvnqLlLRWE2yw",
"2022-08-04": "https://v.douyu.com/show/Kg1VWRB6yANWGbNA",
"2022-08-05": "https://v.douyu.com/show/0zZVvPAj4J37O4E2",
"2022-08-06": "https://v.douyu.com/show/mPyq7oVRkA5v1gLY",
"2022-08-07": "https://v.douyu.com/show/85BAvqOEGrqMG4Lm",
"2022-08-09": "https://v.douyu.com/show/JmbBMkl2mkwW40XA",
"2022-08-10": "https://v.douyu.com/show/yVY8Wwwpzg8WLOz9",
"2022-08-11": "https://v.douyu.com/show/a2JEMJgeRw0WNxml",
"2022-08-12": "https://v.douyu.com/show/yVY8WwwkdGAWLOz9",
"2022-08-13": "https://v.douyu.com/show/brN0MmzK51bWpyxA",
"2022-08-14": "https://v.douyu.com/show/brN0MmzK68QWpyxA",
"2022-08-15": "https://v.douyu.com/show/wLjGvLZ1jPjMmO90",
"2022-08-18": "https://v.douyu.com/show/1LDR7Qlw1bgvJzx8",
"2022-08-19": "https://v.douyu.com/show/6Aw87OZr3yXvYGkg",
"2022-08-20": "https://v.douyu.com/show/LDBbMA8Yr4q7yJRP",
"2022-08-21": "https://v.douyu.com/show/0Q8mMYGQbnNv49Ad",
"2022-08-23": "https://v.douyu.com/show/0Q8mMYGV5j8v49Ad",
"2022-08-24": "https://v.douyu.com/show/n8GzMXKqglJ76qyP",
"2022-08-25": "https://v.douyu.com/show/kDe0W29YB6gMA4Bz",
"2022-08-27": "https://v.douyu.com/show/Yo4evyK4mdNM8L62",
"2022-08-28": "https://v.douyu.com/show/DO84vr9z8OwWedGr",
"2022-08-30": "https://v.douyu.com/show/Kp1QM8RyPKpvk4bj",
"2022-10-10": "https://v.douyu.com/show/JmbBMklEw6yW40XA",
"2023-01-11": "https://v.douyu.com/show/DrwnvzZYLjQvPNaX",
"2023-01-13": "https://v.douyu.com/show/EO0XvN325587DrBd",
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
