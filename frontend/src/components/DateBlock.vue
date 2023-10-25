<template>
    <div class="date-block">
        <p class="date-text">Сегодня:</p> {{ $store.state.currentDate.toLocaleDateString("ru") }}
    </div>
</template>

<script>
export default {
    name: "date-block",
}
</script>

<style scoped>
.date-text {
    font-family: "Primary", Courier, monospace;
    margin: 30px;
}

.date-block {
    width: 100%;
    margin: 0 auto;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    font-family: "Numeric", Courier, monospace;
    font-size: 48px;
    color: chocolate;
    border: 0.5px teal solid;
    box-shadow: 0 0 0 3px rgba(0, 128, 128, 0.5);
}
</style>