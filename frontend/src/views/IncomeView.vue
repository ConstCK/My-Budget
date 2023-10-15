<template>
    <div>
        <auth-block></auth-block>
        <nav-bar></nav-bar>
    </div>
</template>

<script>
import AuthBlock from "@/components/AuthBlock.vue";
import NavBar from "@/components/NavBar.vue"
import MainBlock from "@/components/MainBlock.vue"
export default {
    name: "IncomeView",
    components: {
        NavBar,
        AuthBlock,
        MainBlock,
    },
}
</script>

<style scoped></style>