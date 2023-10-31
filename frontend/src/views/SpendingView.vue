<template>
    <div>
        <auth-header-full></auth-header-full>
        <nav-bar></nav-bar>
        <budget-form v-bind:header="header" :mode="currentMode" @submitForm="handleSpendingAddition"></budget-form>
    </div>
</template>

<script>
import AuthHeaderFull from "@/components/AuthHeaderFull.vue";
import NavBar from "@/components/NavBar.vue";
import BudgetForm from "@/components/BudgetForm.vue";
import { addSpending } from "@/API/apiServices.js";

export default {
    name: "SpendingView",
    components: {
        NavBar,
        AuthHeaderFull,
        BudgetForm,
    },
    data() {
        return {
            token: localStorage.getItem("token"),
            header: "Добавление расходов",
            currentMode: "Spending",
        }
    },
    methods: {
        handleSpendingAddition(event) {
            addSpending(this.token, event).then((response) => {
                console.log(response)
            }).catch((err) => {
                console.log(err)
            })
        }
    },
}
</script>

<style scoped></style>