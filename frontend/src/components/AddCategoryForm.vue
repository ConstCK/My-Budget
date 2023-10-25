<template>
    <div class="add-category-form">
        <div class="category-header">Добавление категории</div>
        <user-input v-model="data.title" placeholder="Название..."></user-input>
        <user-input v-model="data.description" placeholder="Описание..."></user-input>
        <user-button @click="handleClick">Добавить</user-button>
    </div>
</template>

<script>
import UserButton from '@/components/UI/UserButton.vue';
import UserInput from '@/components/UI/UserInput.vue';
export default {
    name: "add-category-form",
    components: {
        UserButton,
        UserInput,
    },
    props: {
        header: String,
    },
    data() {
        return {
            data: {
                title: "",
                description: "",
            }
        }
    },
    methods: {
        handleClick() {
            this.$emit("submitForm", this.data)
            this.data = {
                title: "",
                description: "",
            }
        }
    }
}
</script>

<style scoped>
.add-category-form {
    width: 90vw;
    display: flex;
    flex-direction: column;
    align-items: center;
}

.category-header {
    font-family: "Primary", Courier, monospace;
    font-size: 36px;
    color: coral;
    margin: 20px 0 0 0;
}
</style>