<template>
    <div>
        <auth-header-full></auth-header-full>
        <nav-bar></nav-bar>
        <budget-form v-bind:header="header" :mode="currentMode" @submitForm="handleIncomeAddition"></budget-form>
    </div>
</template>

<script>
import AuthHeaderFull from "@/components/AuthHeaderFull.vue";
import NavBar from "@/components/NavBar.vue";
import BudgetForm from "@/components/BudgetForm.vue";
import { addIncome } from "@/API/apiServices.js"

export default {
    name: "income-view",
    components: {
        NavBar,
        AuthHeaderFull,
        BudgetForm
    },
    data() {
        return {
            token: localStorage.getItem("token"),
            header: "Добавление доходов",
            currentMode: "Income",
        }
    },
    methods: {
        handleIncomeAddition(event) {
            addIncome(this.token, event).then((response) => {
                console.log(response)
            }).catch((err) => {
                console.log(err)
            })
        }
    },
}
</script>

<style scoped></style>