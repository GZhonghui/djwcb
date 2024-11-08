<template>
  <div id="app">
    <router-view />
  </div>
</template>

<script>
export default {
  name: 'App'
};
</script>

<style>
/* Global styles */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  background-color: #ffffff;
}

#app {
  font-family: Arial, sans-serif;
  color: #333;
  
  /* Center content */
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
}
</style>