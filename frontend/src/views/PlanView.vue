<template>
    <div>
        <auth-header-full></auth-header-full>
        <nav-bar></nav-bar>
    </div>
</template>

<script>
import AuthHeaderFull from "@/components/AuthHeaderFull.vue";
import NavBar from "@/components/NavBar.vue";
import MainBlock from "@/components/MainBlock.vue";

export default {
    name: "PlanView",
    components: {
        NavBar,
        AuthHeaderFull,
        MainBlock,
    },
}
</script>

<style scoped></style>