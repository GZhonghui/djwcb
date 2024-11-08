<template>
  <div id="app">
    <GeneratedButtons />
  </div>
</template>

<script>
import GeneratedButtons from './components/GeneratedButtons.vue';

export default {
  name: 'App',
  components: {
    GeneratedButtons
  }
};
</script>

<style>
/* Remove page margin and padding */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

#app {
  font-family: Arial, sans-serif;
  color: #333;
  background-color: #f5e8e4; /* Matching background color with GeneratedButtons.vue */
  margin: 0;
  padding: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
}
</style>
