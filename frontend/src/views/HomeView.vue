<template>
  <div class="home">
    <auth-block></auth-block>
    <nav-bar></nav-bar>
    <main-block></main-block>
  </div>
</template>

<script>
import AuthBlock from "@/components/AuthBlock.vue";
import NavBar from "@/components/NavBar.vue"
import MainBlock from "@/components/MainBlock.vue"
export default {
  name: 'HomeView',
  components: {
    NavBar,
    AuthBlock,
    MainBlock,
},
}
</script>

<style scoped>
</style>