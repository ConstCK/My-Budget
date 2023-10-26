<template>
    <div class="category-list">
        <div :key="element.id" v-for="element in data">
            <div class="category-cell">
                <div class="category-title">{{ element.title }}</div>
                <div class="category-descriptioon">{{ element.description }}</div>
                <user-button :disabled="element.title == 'Прочее'" @click="handleClick(element.id)">Удалить</user-button>
            </div>
        </div>
    </div>
</template>

<script>
import UserButton from '@/components/UI/UserButton.vue';
export default {
    name: "category-list",
    components: {
        UserButton,
    },
    props: {
        data: Array,
        require: true,
    },
    methods: {
        handleClick(id) {
            this.$emit("deleteCategory", id)
        },
    }
}
</script>

<style scoped>
.category-list {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin: 20px;
}

.category-cell {
    width: 80vw;
    border: 1px teal solid;
    background-color: rgba(0, 0, 0, 0.5);
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    font-family: 'Main', Courier, monospace;
    color: coral;
}

.category-title {
    margin: 10px 20px;
    font-size: 32px;
}

[disabled] {
    pointer-events: none;
    background-color: white;
    color: black;
}
</style>