<template>
    <nav class="nav-bar">
        <user-button class="nav-btn" @click="$router.push('income')">Доход</user-button>
        <user-button class="nav-btn" @click="$router.push('spending')">Расход</user-button>
        <user-button class="nav-btn" @click="$router.push('statistic')">Статистика</user-button>
        <user-button class="nav-btn" @click="$router.push('plan')">Планирование</user-button>
    </nav>
</template>

<script>
import UserButton from '@/components/UI/UserButton.vue';
export default {
    name: "nav-bar",
    components: {
        UserButton,
    }
}
</script>

<style scoped>
.nav-bar {
    width: 98%;
    margin: 0 auto;
    display: flex;
    flex-direction: row;
    justify-content: center;
    border: 0.5px teal solid;
    box-shadow: 0 0 0 3px rgba(0, 128, 128, 0.5);
    padding: 20px 10px;
}

.nav-btn {
    width: 200px;
}

@media (max-width: 991px) {
    .nav-btn {
        padding: 10px;
        font-size: 16px;
        min-height: 30px;
    }
}

@media (max-width: 767px) {
    .nav-btn {
        padding: 2px 5px;
        font-size: 9px;
        margin: 10px;
        min-height: 30px;
    }
}
</style>