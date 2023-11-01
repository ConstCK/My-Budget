<template>
    <div class="budget-form">
        <header class="header" v-text="header"></header>
        <user-select class="select" v-model="category">
            <option class="option" v-for="cat in categories" :key="cat.id" :value="cat.id">
                {{ cat.title }}
            </option>
        </user-select>
        <user-input v-model="description" placeholder="Добавьте описание...">
        </user-input>
        <user-input v-model="amount" placeholder="Добавьте сумму...">
        </user-input>
        <DatePicker v-model="date" :style="{
            'background-color': 'rgb(0,155,155)',
            'width': '80%',
            'color': 'black',
            'margin': '20px auto'
        }" />
        <user-button :disabled="!validateForm" @click="handleClick">Добавить</user-button>
    </div>
</template>

<script>
import { DatePicker } from 'v-calendar';
import 'v-calendar/style.css';
import UserSelect from '@/components/UI/UserSelect.vue';
import UserInput from '@/components/UI/UserInput.vue';
import UserButton from '@/components/UI/UserButton.vue';
import { getIncomeCategories, getSpendingCategories } from "@/API/apiServices";
import { amountValidation } from "@/Helpers/validationServices.js";

export default {
    name: "budget-form",
    components: {
        UserSelect,
        UserInput,
        UserButton,
        DatePicker,
    },
    props: {
        header: {
            type: String,
            required: true
        },
        mode: {
            type: String,
            required: true,
        },
    },
    data() {
        return {
            token: localStorage.getItem("token"),
            categories: [],
            category: "",
            description: "",
            amount: "",
            date: new Date(),
            formData: {},
        }
    },
    methods: {
        handleClick() {
            this.formData = {
                "category": this.category,
                "description": this.description,
                "amount": this.amount,
                "date": this.date.toDateString(),
            }
            this.$emit("submitForm", this.formData)
            this.category = "";
            this.description = "";
            this.amount = "";
            this.date = new Date();
        }
    },
    computed: {
        validateForm() {
            return amountValidation(this.amount)
        }
    },
    mounted() {
        if (this.mode == "Income") {
            getIncomeCategories(this.token).then((response) => {
                this.categories = response.data
            }).catch((err) => {
                console.log(err)
            })
        } else if (this.mode == "Spending") {
            getSpendingCategories(this.token).then((response) => {
                this.categories = response.data
            }).catch((err) => {
                console.log(err)
            })
        } else {
            console.log("Ошибка режима получения данных...")
        }
    },

}
</script>

<style scoped>
.budget-form {
    width: 99%;
    min-height: 60vh;
    margin: 0 auto 50px;
    display: flex;
    flex-direction: column;
    align-items: center;
    border: 0.5px teal solid;
    box-shadow: 0 0 0 3px rgba(0, 128, 128, 0.5);
}

.header {
    font-family: "Primary", Courier, monospace;
    color: coral;
    margin: 20px;
    font-size: 32px;
}

[disabled] {
    pointer-events: none;
    background-color: white;
    color: black;
}
</style>