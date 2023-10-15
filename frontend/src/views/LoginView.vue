<template>
    <login-block></login-block>
    <login-form v-bind:header="header"></login-form>
</template>

<script>
import LoginBlock from "@/components/LoginBlock.vue";
import LoginForm from "@/components/LoginForm.vue";

export default {
    name: "AuthView",
    components: {
        LoginBlock, LoginForm
    },
    data() {
        return {
            header: "Страница авторизации"
        }
    },
}
</script>

<style scoped>
.auth-btn {
    display: flex;
    align-items: center;
}

.btn-img {
    filter: invert(98%) sepia(58%) saturate(3301%) hue-rotate(101deg) brightness(108%) contrast(104%);
}

.btn-img:hover {
    filter: invert(100%) sepia(100%) saturate(0%) hue-rotate(1deg) brightness(107%) contrast(101%);
}
</style>