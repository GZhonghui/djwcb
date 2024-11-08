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
/* Global styles */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

/* Set SVG background on body to cover the entire webpage */
body {
  background-color: #ffffff;
  /*
  background-image: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 600 144' width='600' height='144' style='opacity: 0.5; filter: grayscale(0.5);'><text x='0em' y='1em' font-size='60' transform='rotate(0 37.5 36)'>🐷</text><text x='1.25em' y='2em' font-size='60' transform='rotate(0 112.5 96)'>🤡</text><text x='2.5em' y='1em' font-size='60' transform='rotate(0 187.5 36)'>👽</text><text x='3.75em' y='2em' font-size='60' transform='rotate(0 262.5 96)'>😈</text><text x='5em' y='1em' font-size='60' transform='rotate(0 337.5 36)'>🤗</text><text x='6.25em' y='2em' font-size='60' transform='rotate(0 412.5 96)'>🤓</text><text x='7.5em' y='1em' font-size='60' transform='rotate(0 487.5 36)'>💩</text><text x='8.75em' y='2em' font-size='60' transform='rotate(0 562.5 96)'>😧</text></svg>");
  background-repeat: repeat;
  background-size: auto;
  */
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
