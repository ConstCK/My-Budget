<template>
    <div>
        <auth-header-full></auth-header-full>
        <nav-bar></nav-bar>
        <plan-form></plan-form>
    </div>
</template>

<script>
import AuthHeaderFull from "@/components/AuthHeaderFull.vue";
import NavBar from "@/components/NavBar.vue";
import PlanForm from "@/components/PlanForm.vue";

export default {
    name: "plan-view",
    components: {
        NavBar,
        AuthHeaderFull,
        PlanForm,
    },
}
</script>

<style scoped></style>