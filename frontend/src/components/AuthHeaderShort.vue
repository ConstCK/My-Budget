<template>
    <div class="login-block">
        <user-button class="auth-btn" @click="$router.push('/')">
            <img class="btn-img" src="@/assets/images/home.svg" alt="home">
        </user-button>
    </div>
</template>

<script>
import UserButton from '@/components/UI/UserButton.vue';
export default {
    name: "auth-header-short",
    components: {
        UserButton,
    },
}
</script>
<style scoped>
.login-block {
    display: flex;
    flex-direction: row;
    justify-content: start;
    width: 99%;
    margin: 0 auto;
    font-family: "Primary", Courier, monospace;
    font-weight: bolder;
    border: 0.5px teal solid;
    box-shadow: 0 0 0 3px rgba(0, 128, 128, 0.5);
    padding: 20px 10px;
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
</style>