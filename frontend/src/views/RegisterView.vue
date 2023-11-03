<template>
    <auth-header-short></auth-header-short>
    <auth-form v-bind:header="header" :errorMessage="errorMessage" @submitForm="handleRegister"></auth-form>
</template>

<script>
import { register } from "@/API/apiServices";
import AuthHeaderShort from "@/components/AuthHeaderShort.vue";
import AuthForm from "@/components/AuthForm.vue";

export default {
    name: "register-view",
    components: {
        AuthHeaderShort, AuthForm
    },
    data() {
        return {
            header: "Страница регистрации",
            errorMessage: "",
        }
    },
    methods: {
        handleRegister(event) {
            register(event.user, event.password).then(
                (response) => {
                    this.$store.commit("logIn")
                    localStorage.setItem("name", event.user);
                    localStorage.setItem("token", response.data["token"]);
                    this.$router.push("/")
                }).catch((err) => {
                    this.errorMessage = "Ошибка регистрации. Возможно такой пользователь существует.\
                    Также пароль должен быть не меннее 8 символов и состоять из цифр и букв.";
                    localStorage.setItem("name", "");
                    localStorage.setItem("token", "");
                })
        }

    }
}
</script>

<style scoped></style>