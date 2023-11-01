<template>
    <div class="plan-form">
        <header class="header">Месячное планирование расходов</header>
        <div class="plan-cell" v-for="element in planList" :key="element.id">
            <div class="plan-category">{{ element.category_info.title }}</div>
            <div class="current-plan">Запланированный расход: {{ element.amount }}</div>
            <user-input class="input" v-model="data[element.id]" :placeholder="element.amount"></user-input>
        </div>
        <user-button :disabled="!validateForm" @click="handlePlanUpdate">Внести изменения</user-button>
    </div>
</template>

<script>
import UserButton from '@/components/UI/UserButton.vue';
import UserInput from '@/components/UI/UserInput.vue';
import { getPlans, updatePlans } from "@/API/apiServices.js"
import { amountValidation } from '@/Helpers/validationServices';

export default {
    name: "plan-form",
    components: {
        UserButton,
        UserInput,
    },
    data() {
        return {
            currentUser: localStorage.getItem("name"),
            token: localStorage.getItem("token"),
            planList: [],
            data: {},
        }
    },
    methods: {
        handlePlanUpdate() {
            updatePlans(this.token, this.data)
                .then((response) => {
                    getPlans(this.token)
                        .then((response) => {
                            this.planList = response.data
                            response.data.forEach(element => {
                                this.data[element.id] = element.amount
                            });
                        })
                        .catch((err) => { console.log(err) })
                })
                .catch((err) => {
                    console.log(err)
                })
        }
    },
    computed: {
        validateForm() {
            let result = true;
            for (let key in this.data) {
                if (!amountValidation(this.data[key])) {
                    result = false
                }
            }
            return result
        },

    },
    mounted() {
        getPlans(this.token)
            .then((response) => {
                this.planList = response.data
                response.data.forEach(element => {
                    this.data[element.id] = element.amount
                });
            })
            .catch((err) => { console.log(err) })
    }

}
</script>

<style scoped>
.plan-form {
    width: 99%;
    min-height: 60vh;
    margin: 0 auto 50px;
    display: flex;
    flex-direction: column;
    align-items: center;
    border: 0.5px teal solid;
    text-shadow: 4px 4px 4px rgba(0, 0, 0, 0.6);
    box-shadow: 0 0 0 3px rgba(0, 128, 128, 0.5);
    font-family: "Main", Courier, monospace;
    color: coral;
    font-size: 24px;
    font-weight: bold;
}

.header {
    font-family: "Primary", Courier, monospace;
    color: coral;
    margin: 20px;
    font-size: 32px;
}

.plan-cell {
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

.plan-category {
    margin: 20px;
    font-size: 32px;
}

.input {
    width: 25%;
}

[disabled] {
    pointer-events: none;
    background-color: white;
    color: black;
}
</style>