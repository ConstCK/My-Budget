<template>
    <input class="input" type="text" v-bind:value="modelValue" v-on:input="updateInput" />
</template>

<script>
export default {
    mame: "user-input",
    props: {
        modelValue: [String, Number],
    },
    methods: {
        updateInput(event) {
            this.$emit("update:modelValue", event.target.value)
        }
    }

}
</script>

<style scoped>
.input {
    width: 80%;
    font-family: "Basic", Courier, monospace;
    font-size: 28px;
    font-weight: bold;
    text-align: center;
    color: black;
    background-color: teal;
    border: 2px solid black;
    box-shadow: 0 0 3px 10px rgba(0, 195, 195, 0.6);
    padding: 10px;
    margin: 20px;
    cursor: pointer;
}

.input:focus {
    outline: 3px solid black;
}

*::placeholder {
    font-family: "Basic", Courier, monospace;
    color: black;
    font-weight: bold;
    font-size: 18px;
}

[v-cloak] {
    display: none;
}

@media (max-width: 991px) {
    *::placeholder {
        font-size: 16px;
    }

    .input {
        font-size: 18px;
    }
}

@media (max-width: 767px) {
    *::placeholder {
        font-size: 14px;
    }

    .input {
        font-size: 14px;
        box-shadow: 0 0 3px 5px rgba(0, 195, 195, 0.6);
        padding: 5px;
        margin: 10px;
    }
}
</style>