<template>
    <select class="select" @change="updateSelect" :value="modelValue">
        <option disabled selected class="option" default value="">{{ defaultOption }}</option>
        <slot></slot>
    </select>
</template>

<script>
export default {
    name: "user-select",
    props: {
        modelValue: {
            type: [String, Number],
            required: true,
        }
    },
    data() {
        return {
            defaultOption: "-------"
        }
    },
    methods: {
        updateSelect(event) {
            this.$emit("update:modelValue", event.target.value)
        }
    },

}
</script>

<style scoped>
.select {
    width: 80%;
    font-family: "Main", Courier, monospace;
    font-size: 22px;
    background-color: teal;
    color: aqua;
    box-shadow: 3px 6px black;
    border-radius: 8px;
    border: none;
    padding: 10px 20px;
    margin: 20px;
    transition: all 0.5s ease-out;
    text-align: center;
    outline: none;
    cursor: pointer;
}

.select:hover {
    transform: scale(1.05);
    box-shadow: 4px 8px black;
    color: black;
    font-weight: bolder;
    font-weight: bolder;
}

@media (max-width: 991px) {
    .select {
        font-size: 18px;
    }
}

@media (max-width: 767px) {
    .select {
        font-size: 14px;
    }
}
</style>