<template>
    <div class="nav-bar">
        <user-button class="nav-btn" @click="$router.push('income')">Доход</user-button>
        <user-button class="nav-btn" @click="$router.push('spending')">Расход</user-button>
        <user-button class="nav-btn" @click="$router.push('plan')">Планирование</user-button>
        <user-button class="nav-btn" @click="$router.push('statistic')">Статистика</user-button>
    </div>
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
    width: 99%;
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
</style>