<template>
    <div>
        <auth-header-full></auth-header-full>
        <nav-bar></nav-bar>
    </div>
</template>

<script>
import AuthHeaderFull from "@/components/AuthHeaderFull.vue";
import NavBar from "@/components/NavBar.vue"

export default {
    name: "StatisticView",
    components: {
        NavBar,
        AuthHeaderFull,
    },
}
</script>

<style scoped></style>