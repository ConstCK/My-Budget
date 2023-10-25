<template>
    <button class="btn" v-cloak>
        <slot></slot>
    </button>
</template>

<script>
export default {
    name: "user-button"
}
</script>

<style scoped>
.btn {
    font-family: "Secondary", Courier, monospace;
    font-weight: bold;
    font-size: 22px;
    min-width: 50px;
    min-height: 50px;
    background-color: teal;
    color: aqua;
    box-shadow: 3px 6px black;
    border-radius: 8px;
    border: none;
    padding: 10px 20px;
    margin: 20px;
    transition: all 0.5s ease-out;
    cursor: pointer;
}

.btn:hover {
    transform: scale(1.05);
    box-shadow: 4px 8px black;
    color: white;
    font-weight: bolder;
}

.btn:active {
    color: black;
    box-shadow: 2px 4px black;
    border-radius: 10px;
}

[v-cloak] {
    display: none;
}
</style>