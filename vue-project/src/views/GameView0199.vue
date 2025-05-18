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
"2025-02-07": "https://v.douyu.com/show/X3JzMalgVL97PQro",
"2025-02-08": "https://v.douyu.com/show/Aox276Y4D9mvVz8Z",
"2025-02-09": "https://v.douyu.com/show/qJgOWx506yrvkVzL",
"2025-02-11": "https://v.douyu.com/show/2Bj8vG3OwoVvObnd",
"2025-02-12": "https://v.douyu.com/show/2Bj8vG3OO6rvObnd",
"2025-02-14": "https://v.douyu.com/show/85BAvqQnpXRvG4Lm",
"2025-02-15": "https://v.douyu.com/show/aRbBv3YOjOyM6PYV",
"2025-02-16": "https://v.douyu.com/show/8KxjMdlgZoxMVLwb",
"2025-02-18": "https://v.douyu.com/show/Qyz171lVdd5vBJj9",
"2025-02-19": "https://v.douyu.com/show/yVY8WwD0JkrvLOz9",
"2025-02-21": "https://v.douyu.com/show/yVY8WwDnXZ8vLOz9",
"2025-02-22": "https://v.douyu.com/show/4xq3WDzY2dR7LGNz",
"2025-02-23": "https://v.douyu.com/show/ZB5Kv9gjXaeMa93x",
"2025-02-25": "https://v.douyu.com/show/6Aw87OQ3gmoWYGkg",
"2025-02-26": "https://v.douyu.com/show/Yo4evyDnQ8kW8L62",
"2025-02-27": "https://v.douyu.com/show/mPyq7obPrzVv1gLY",
"2025-03-02": "https://v.douyu.com/show/qJgOWx5nLZNvkVzL",
"2025-03-04": "https://v.douyu.com/show/XqeO74Nmy1yWxywG",
"2025-03-05": "https://v.douyu.com/show/X3JzMalzo6l7PQro",
"2025-03-07": "https://v.douyu.com/show/a4Jj7lBa1ZbWDk01",
"2025-03-08": "https://v.douyu.com/show/kDe0W2gbAwnvA4Bz",
"2025-03-09": "https://v.douyu.com/show/2V0JMVQkaB67RY5k",
"2025-03-11": "https://v.douyu.com/show/Kp1QM8YeaP6Wk4bj",
"2025-03-12": "https://v.douyu.com/show/2V0JMVQkG8k7RY5k",
"2025-03-14": "https://v.douyu.com/show/4xq3WDz5VV07LGNz",
"2025-03-15": "https://v.douyu.com/show/DrwnvzDqYk0MPNaX",
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
