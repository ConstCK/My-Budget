<template>
  <div class="home">
    <auth-header-full></auth-header-full>
    <nav-bar></nav-bar>
    <main-block></main-block>
  </div>
</template>

<script>
import AuthHeaderFull from "@/components/AuthHeaderFull.vue";
import NavBar from "@/components/NavBar.vue";
import MainBlock from "@/components/MainBlock.vue";

export default {
  name: 'HomeView',
  components: {
    NavBar,
    AuthHeaderFull,
    MainBlock,
  },
}
</script>

<style scoped></style>