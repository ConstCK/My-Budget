<template>
    <div class="login-form">
        <h1 class="auth-header" v-text="header"></h1>
        <div class="login-message">{{ errorMessage }}</div>
        <user-input v-model="user" placeholder="Введите фамилию..." />
        <user-input v-model="password" placeholder="Введите пароль..." />
        <user-button @click="handleRegister">Отправить</user-button>
    </div>
</template>

<script>
import UserInput from "@/components/UI/UserInput.vue";
import UserButton from "./UI/UserButton.vue";
import { register } from "@/API/services";
export default {
    name: "register-form",
    components: {
        UserInput, UserButton
    },
    props: {
        header: String,
    },
    data() {
        return {
            user: "",
            password: "",
            errorMessage: ""
        }
    },
    methods: {
        handleRegister() {
            register(this.user, this.password).then(
                (response) => {
                    this.$store.commit("logIn")
                    localStorage.setItem("name", this.user);
                    localStorage.setItem("token", response.data["token"]);
                    this.$router.push("/")
                }).catch((err) => {
                    this.errorMessage = "Ошибка регистрации";
                    this.user = "";
                    this.password = "";
                    localStorage.setItem("name", "");
                    localStorage.setItem("token", "");

                })
        }
    }
}
</script>

<style scoped>
.login-form {
    width: 99%;
    min-height: 80vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    margin: 0 auto;
    border: 0.5px teal solid;
    box-shadow: 0 0 0 3px rgba(0, 128, 128, 0.5);
}

.login-message {
    font-family: "Primary", Courier, monospace;
    font-size: 44px;
    color: chocolate;
}

.auth-header {
    font-family: "Primary", Courier, monospace;
    color: coral;
    margin: 20px;
}
</style>