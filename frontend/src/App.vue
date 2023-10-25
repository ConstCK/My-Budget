<template>
  <router-view />
</template>

<style>
@font-face {
  font-family: "Primary";
  src: url("/src/assets/fonts/Karmen.ttf");
}

@font-face {
  font-family: "Secondary";
  src: url("/src/assets/fonts/Czizh.ttf");
}

@font-face {
  font-family: "Numeric";
  src: url("/src/assets/fonts/Schwabacher.ttf");
}

@font-face {
  font-family: "Main";
  src: url("/src/assets/fonts/Tolkien.ttf");
}

@font-face {
  font-family: "Manuscript";
  src: url("/src/assets/fonts/GoodVibesPro.ttf");
}

@font-face {
  font-family: "Capital";
  src: url("/src/assets/fonts/Sorcerer.ttf");
}

* {
  padding: 0;
  margin: 0;
  text-decoration: none;
  box-sizing: border-box;
  overflow-x: hidden;
}

#app {
  margin: 0 auto;
  width: 99%;
  min-height: 100vh;
  background-color: rgba(0, 0, 0, 0.8);
  box-shadow: 0 0 0 10px rgba(0, 0, 0, 0.7);
  overflow-x: hidden;
}
</style>
