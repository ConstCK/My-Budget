<template>
    <auth-header-short></auth-header-short>
    <auth-form v-bind:header="header" v-bind:errorMessage="errorMessage" @submitForm="handleLogin"></auth-form>
</template>

<script>
import { login } from "@/API/apiServices";
import AuthHeaderShort from "@/components/AuthHeaderShort.vue";
import AuthForm from "@/components/AuthForm.vue";

export default {
    name: "login-view",
    components: {
        AuthHeaderShort, AuthForm
    },
    data() {
        return {
            header: "Страница авторизации",
            errorMessage: "",
        }
    },
    methods: {
        handleLogin(event) {
            login(event.user, event.password).then(
                (response) => {
                    this.$store.commit("logIn")
                    localStorage.setItem("name", event.user);
                    localStorage.setItem("token", response.data["token"]);
                    this.$router.push("/")
                }).catch((err) => {
                    this.errorMessage = "Ошибка авторизации";
                    localStorage.setItem("name", "");
                    localStorage.setItem("token", "");
                })
        }
    }
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