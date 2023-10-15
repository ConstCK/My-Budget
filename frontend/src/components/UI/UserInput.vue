<template>
    <input class="input" type="text" v-bind:value="modelValue" v-on:input="updateInput" />
</template>

<script>
export default {
    mame: "user-input",
    props: {
        modelValue: [String],
        required: false,
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
    font-family: "Basic", Courier, monospace;
    font-size: 28px;
    width: 60%;
    text-align: center;
    color: white;
    background-color: teal;
    border: 2px solid black;
    box-shadow: 0 0 3px 10px rgba(0, 195, 195, 0.6);
    padding: 15px;
    margin: 40px;
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
</style>