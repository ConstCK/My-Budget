<template>
    <div class="date-block">
        <div class="date-text">Сегодня:</div>
        <div class="date-value">{{ $store.state.currentDate.toLocaleDateString("ru") }}</div>

    </div>
</template>

<script>
export default {
    name: "date-block",
}
</script>

<style scoped>
.date-block {
    width: 100%;
    margin: 0 auto;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    font-family: "Primary", Courier, monospace;
    font-size: 48px;
    color: chocolate;
    border: 0.5px teal solid;
    box-shadow: 0 0 0 3px rgba(0, 128, 128, 0.5);
}

.date-text {
    margin: 20px;
}

.date-value {
    font-family: "Numeric", Courier, monospace;
}

@media (max-width: 767px) {
    .date-block {
        font-size: 32px;
    }
}
</style>