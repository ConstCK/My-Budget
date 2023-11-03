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
    width: 98%;
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
    text-align: center;
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
    min-width: 20%;
}

.current-plan {
    min-width: 50%;
    text-align: center;
}

.input {
    min-width: 22%;
}

[disabled] {
    pointer-events: none;
    background-color: white;
    color: black;
}

@media (max-width: 991px) {
    .plan-category {
        min-width: 25%;
        font-size: 28px;
    }

    .current-plan {
        min-width: 40%;
        font-size: 24px;
    }

    .input {
        min-width: 20%;
    }

    .plan-cell {
        width: 90vw;
    }
}

@media (max-width: 767px) {
    .header {
        font-size: 22px;
    }

    .plan-category {
        font-size: 14px;
        margin: 6px;
        min-width: 25%;
    }

    .current-plan {
        font-size: 10px;
        margin: 6px;
        min-width: 40%;
    }

    .input {
        min-width: 20%;
        font-size: 12px;
        margin: 10px 6px;
        min-width: 15%;
    }

    .btn {
        min-height: 30px;
        font-size: 16px;
    }
}
</style>