<template>
    <div class="auth-block">
        <nav class="auth-left desktop">
            <user-button class="auth-btn" @click="$router.push('/')"><img class="btn-img" src="@/assets/images/home.svg"
                    alt="home"></user-button>
            <user-button class="auth-btn" @click="$router.push('settings')"><img class="btn-img"
                    src="@/assets/images/settings.svg" alt="settings"></user-button>
            <user-button v-if="$store.state.isAuth === false" @click="$router.push('login')">Войти</user-button>
            <user-button v-else @click="changeFamily">Сменить семью</user-button>
            <user-button @click="$router.push('register')">Регистрация</user-button>
        </nav>
        <nav class="auth-left mobile">
            <div :class="menuStatusClosed ? 'menu-button' : 'menu-button opened'" @click="handleClick">
                <div></div>
                <div></div>
                <div></div>
            </div>
        </nav>
        <div :class="menuStatusClosed ? 'menu-invisible' : 'menu-visible'">
            <user-button class="auth-btn" @click="$router.push('/')"><img class="btn-img" src="@/assets/images/home.svg"
                    alt="home"></user-button>
            <user-button class="auth-btn" @click="$router.push('settings')"><img class="btn-img"
                    src="@/assets/images/settings.svg" alt="settings"></user-button>
            <user-button v-if="$store.state.isAuth === false" @click="$router.push('login')">Войти</user-button>
            <user-button v-else @click="changeFamily">Сменить семью</user-button>
            <user-button @click="$router.push('register')">Регистрация</user-button>
        </div>
        <div class="auth-right">
            <div>Семья: {{ name }}</div>
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
            menuStatusClosed: true,
        }

    },
    methods: {
        changeFamily() {
            localStorage.setItem("name", "");
            localStorage.setItem("token", "");
            this.$store.commit("logOut")
            this.$router.push('login')
        },
        handleClick() {
            this.menuStatusClosed = !this.menuStatusClosed;
        }
    },
}
</script>

<style scoped>
.auth-block {
    width: 98%;
    margin: 10px auto 0;
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

.auth-right {
    width: 40%;
    display: flex;
    flex-direction: row;
    justify-content: end;
    font-size: 16px;
    margin: 10px 20px;
    color: chocolate;
}

.auth-right>div {
    text-align: end;
}

.auth-btn {
    display: flex;
    align-items: center;
    justify-content: center;
}

.desktop {
    display: flex;
}

.mobile {
    display: none;
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

.menu-invisible {
    display: none;
}

.menu-visible {
    position: absolute;
    margin: 0 auto;
    left: 2%;
    top: 10%;
    min-width: 96%;
    display: flex;
    flex-direction: column;
    z-index: 1;
    background-color: rgba(0, 0, 0, 0.9);
    border-radius: 20px;
}

.menu-button {
    width: 30px;
    height: 24px;
    position: relative;
    margin: 10px;
    transform: rotate(0deg);
    transition: .5s ease-in-out;
    cursor: pointer;
    overflow: hidden;
}

.opened {
    width: 30px;
    height: 24px;
    position: relative;
    margin: 10px;
    transform: rotate(0deg);
    transition: .5s ease-in-out;
    cursor: pointer;
    z-index: 1;
}

.menu-button div {
    position: absolute;
    height: 2px;
    width: 100%;
    transform: rotate(0deg);
    transition: .25s ease-in-out;
    background-color: teal;
}

.opened div {
    position: absolute;
    height: 2px;
    width: 100%;
    right: 10px;
    transform: rotate(0deg);
    transition: .25s ease-in-out;
    background-color: teal;
}

.menu-button div:nth-child(1) {
    top: 0px;
}

.menu-button div:nth-child(2) {
    top: 9px;
}

.menu-button div:nth-child(3) {
    top: 18px;
}

.opened div:nth-child(1) {
    top: 12px;
    left: 0;
    transform: rotate(45deg);
}

.opened div:nth-child(2) {
    display: none;
    left: -60px;
}

.opened div:nth-child(3) {
    top: 12px;
    right: 0;
    transform: rotate(-45deg);
}

@media (max-width: 991px) {
    .btn {
        padding: 5px 10px;
        font-size: 12px;
    }


}

@media (max-width: 767px) {
    .desktop {
        display: none;
    }

    .mobile {
        display: flex;
        flex-direction: column;
        width: 30%;
    }

    .auth-right {
        width: 50%;
        font-size: 12px;
        align-self: center;
    }
}
</style>