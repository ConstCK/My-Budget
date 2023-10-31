<template>
    <div class="settings">
        <auth-header-full></auth-header-full>
        <nav-bar></nav-bar>
        <div v-cloak class="settings-block">
            <h1 class="settings-header">Категории {{ header }}</h1>
            <user-button :class="categoryMode == null ? 'disabled' : ''" @click="toggleMode">
                {{ primaryButtonText }} {{ secondaryButtonText }}
            </user-button>
            <div class="settings-selection">
                <user-button :class="categoryMode == 'Income' ? 'active' : 'inactive'" @click="handleIncomeCategories">
                    Доходы
                </user-button>
                <user-button :class="categoryMode == 'Spending' ? 'active' : 'inactive'"
                    @click="handleSpendingCategories">Расходы</user-button>
            </div>
            <div v-if="displayCategories == true">
                <category-list :data="categories" @deleteCategory="handleCategoryDeletion"></category-list>
            </div>
            <div v-else>
                <add-category-form @submitForm="handleCategoryAddition"></add-category-form>
            </div>

        </div>
    </div>
</template>

<script>
import AuthHeaderFull from "@/components/AuthHeaderFull.vue";
import NavBar from "@/components/NavBar.vue"
import MainBlock from "@/components/MainBlock.vue"
import UserButton from "@/components/UI/UserButton.vue";
import CategoryList from "@/components/CategoryList.vue";
import AddCategoryForm from "@/components/AddCategoryForm.vue";
import {
    getIncomeCategories,
    getSpendingCategories,
    deleteIncomeCategory,
    deleteSpendingCategory,
    addCategory,
}
    from "@/API/apiServices";

export default {
    name: "settings-view",
    components: {
        NavBar,
        AuthHeaderFull,
        MainBlock,
        UserButton,
        CategoryList,
        AddCategoryForm,
    },
    data() {
        return {
            token: localStorage.getItem("token"),
            categories: [],
            header: "доходов и расходов",
            primaryButtonText: "Добавить категорию",
            secondaryButtonText: "...",
            categoryMode: null,
            displayCategories: true,
            trigger: false,
        }
    },
    methods: {
        handleIncomeCategories() {
            this.categoryMode = "Income";
            this.header = "доходов";
            this.secondaryButtonText = "доходов";
            getIncomeCategories(this.token).then((response) => {
                this.categories = response.data
            }).catch((err) => {
                console.log("Ошибка получения данных", err)
            })
        },
        handleSpendingCategories() {
            this.categoryMode = "Spending";
            this.header = "расходов";
            this.secondaryButtonText = "расходов";
            getSpendingCategories(this.token).then((response) => {
                this.categories = response.data
            }).catch((err) => {
                console.log("Ошибка получения данных", err)
            })
        },
        handleCategoryDeletion(id) {
            if (this.categoryMode == "Income") {
                deleteIncomeCategory(id, this.token).then((response) => {
                    this.categories = this.categories.filter((element) => {
                        return element.id != id
                    })
                }).catch((err) => {
                    console.log(err)
                })
            } else {
                deleteSpendingCategory(id, this.token).then((response) => {
                    this.categories = this.categories.filter((element) => {
                        return element.id != id
                    })
                }).catch((err) => {
                    console.log(err)
                })
            }
        },
        toggleMode() {
            this.displayCategories = !this.displayCategories;
            if (this.primaryButtonText == "Добавить категорию") {
                this.primaryButtonText = "Показать категории"

            } else {
                this.primaryButtonText = "Добавить категорию"
            }
        },
        handleCategoryAddition(event) {
            addCategory(
                event["title"],
                event["description"],
                this.categoryMode,
                this.token).then((response) => {
                    if (response) { this.categories.push(response.data) }
                }).catch((err) => {
                    console.log(err)
                })
        }
    },
    watch: {
        trigger() {
            if (this.categoryMode == "Income") {
                getIncomeCategories(this.currentUser, this.token).then((response) => {
                    this.categories = response.data
                })
            } else {
                getSpendingCategories(this.currentUser, this.token).then((response) => {
                    this.categories = response.data
                })
            }
        }
    },
}
</script>

<style scoped>
.settings-block {
    width: 99%;
    min-height: 60vh;
    margin: 0 auto 20px;
    border: 0.5px teal solid;
    box-shadow: 0 0 0 3px rgba(0, 128, 128, 0.5);
    text-shadow: 4px 4px 4px rgba(0, 0, 0, 0.6);
    display: flex;
    flex-direction: column;
    align-items: center;
}

.settings-selection {
    display: flex;
    flex-direction: row;
    justify-content: center;
}

.settings-header {
    font-family: "Primary", Courier, monospace;
    color: coral;
    margin: 40px 0 0 0;
    text-align: center;
}

.btn {
    min-width: 160px;
    max-width: 340px;
}

.active {
    outline: 2px coral solid;
    color: red;
}

.disabled {
    pointer-events: none;
    background-color: white;
    color: black;
}
</style>