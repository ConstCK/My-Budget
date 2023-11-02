<template>
    <div class="category-list">
        <div :key="element.id" v-for="element in data">
            <div class="category-cell">
                <div class="category-title">{{ element.title }}</div>
                <div class="category-description">{{ element.description }}</div>
                <user-button class="delete-btn" :disabled="element.title == 'Прочее'"
                    @click="handleClick(element.id)">Удалить</user-button>
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
    width: 90vw;
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
    width: 20%;
    margin: 15px;
    padding: 5px;
    font-size: 32px;
}

.category-description {
    width: 45%;
    margin: 15px;
    padding: 5px;
    text-align: center;
    font-size: 20px;
}

.delete-btn {
    width: 20%;
}

[disabled] {
    pointer-events: none;
    background-color: white;
    color: black;
}

@media (max-width: 991px) {
    .category-title {
        font-size: 24px;
    }

    .category-description {
        font-size: 16px;
    }

    .btn {
        font-size: 18px;
        padding: 5px 10px;
        min-height: 40px;
    }
}

@media (max-width: 767px) {
    .category-title {
        margin: 10px;
        font-size: 10px;
    }

    .category-description {
        margin: 10px;
        font-size: 8px;
    }

    .btn {
        margin: 10px;
        padding: 5px 10px;
        font-size: 12px;
        min-height: 30px;
    }
}
</style>