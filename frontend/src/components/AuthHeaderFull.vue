<template>
    <div class="auth-block">
        <nav class="auth-left">
            <user-button class="auth-btn" @click="$router.push('/')"><img class="btn-img" src="@/assets/images/home.svg"
                    alt="home"></user-button>
            <user-button class="auth-btn" @click="$router.push('settings')"><img class="btn-img"
                    src="@/assets/images/settings.svg" alt="settings"></user-button>
            <user-button v-if="$store.state.isAuth === false" @click="$router.push('login')">Войти</user-button>
            <user-button v-else @click="changeFamily">Сменить семью</user-button>
            <user-button @click="$router.push('register')">Регистрация</user-button>
        </nav>
        <div class="auth-right">
            <div class="family-name">Семья: {{ name }}</div>
        </div>
    </div>
</template>

<script>
import UserButton from '@/components/UI/UserButton.vue';
export default {
    name: "auth-header-full",
    components: {
        UserButton,
    },
    data() {
        return {
            name: localStorage.getItem("name"),
        }

    },
    methods: {
        changeFamily() {
            localStorage.setItem("name", "");
            localStorage.setItem("token", "");
            this.$store.commit("logOut")
            this.$router.push('login')
        }
    },
}
</script>

<style scoped>
.auth-block {
    width: 99%;
    margin: 0 auto;
    font-family: "Capital", Courier, monospace;
    font-size: 24px;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    border: 0.5px teal solid;
    box-shadow: 0 0 0 3px rgba(0, 128, 128, 0.5);
    padding: 20px 10px;
}

.auth-left {
    width: 70%;
    display: flex;
    flex-direction: row;
    align-items: center;
}

.family-name {
    margin: 10px 0 0 30px;
    color: chocolate;
}

.auth-right {
    width: 30%;
    display: flex;
    flex-direction: row;
    justify-content: start;
    font-size: 16px;
}

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

.btn-img:active {
    filter: invert(0%) sepia(89%) saturate(7466%) hue-rotate(50deg) brightness(91%) contrast(96%);
}
</style>