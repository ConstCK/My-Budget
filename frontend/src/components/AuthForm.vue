<template>
    <div class="auth-form">
        <header class="auth-header" v-text="header"></header>
        <div class="error-message" v-text="errorMessage"></div>
        <user-input v-model="user" placeholder="Введите фамилию..." />
        <user-input v-model="password" placeholder="Введите пароль..." />
        <user-button :disabled="!validatePassword" @click="handleAuth">Отправить</user-button>
    </div>
</template>

<script>
import UserInput from "@/components/UI/UserInput.vue";
import UserButton from "@/components/UI/UserButton.vue";
import { passwordValidation } from "@/Helpers/validationServices.js"

export default {
    name: "auth-form",
    components: {
        UserInput, UserButton
    },
    props: {
        header: String,
        errorMessage: String,
    },
    data() {
        return {
            user: "",
            password: "",
        }
    },
    methods: {
        handleAuth() {
            this.$emit("submitForm", { "user": this.user, "password": this.password })
        }
    },
    computed: {
        validatePassword() {
            return passwordValidation(this.password)
        }
    }
}
</script>

<style scoped>
.auth-form {
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

.error-message {
    font-family: "Main", Courier, monospace;
    font-size: 24px;
    color: goldenrod;
    text-align: center;
    margin: 10px 20px;
}

.auth-header {
    font-family: "Primary", Courier, monospace;
    color: coral;
    margin: 20px;
    font-size: 32px;
}

[disabled] {
    pointer-events: none;
    background-color: white;
    color: black;
}

@media (max-width: 991px) {
    .auth-header {
        margin: 50px auto 20px;
    }

    .auth-form {
        width: 98%;
        justify-content: start;
    }
}
</style>