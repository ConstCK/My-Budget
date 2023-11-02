<template>
    <div>
        <auth-header-full></auth-header-full>
        <nav-bar></nav-bar>
        <div class="statistic-block">
            <header class="header">Отчеты</header>
            <nav class="nav-bar">
                <user-button :class="mode == 'General' ? 'active' : 'inactive'"
                    @click="handleGeneralStatistic">Общие</user-button>
                <user-button :class="mode == 'Annual' ? 'active' : 'inactive'" @click="handleAnnualStatistic">За
                    год</user-button>
                <user-button :class="mode == 'Month' ? 'active' : 'inactive'" @click="handleMonthStatistic">За
                    месяц</user-button>
            </nav>
            <div class="info-block" v-show="mode == 'General'">
                <div class="info-header">Доходы</div>
                <div class="message" v-show="!incomeData">Нет данных...</div>
                <div class="income-statistic">
                    <div class="statistic-cell" v-for="element in allIncome" :key="element.id">
                        <div class="row">
                            <div class="income-title">{{ element.title }}</div>
                            <div class="income-details">{{ element.overall }}{{ $store.state.currency }}</div>
                        </div>
                    </div>
                </div>
                <div class="info-header">Расходы</div>
                <div class="message" v-show="!spendingsData">Нет данных...</div>
                <div class="income-statistic">
                    <div class="statistic-cell" v-for="element in allSpendings" :key="element.id">
                        <div class="row">
                            <div class="income-title">{{ element.title }}</div>
                            <div class="income-details">{{ element.overall }}{{ $store.state.currency }}</div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="info-block" v-show="mode == 'Annual'">
                <div class="date-bar">
                    <user-select class="select" v-model="currentYear">
                        <option v-for="year in getYears" :key="year">{{ year }}</option>
                    </user-select>
                    <user-button class="btn" @click="handleAnnualRequest">Запрос</user-button>
                </div>
                <div class="info-header">Доходы за {{ currentYear }} год</div>
                <div class="message" v-show="!incomeData">Нет данных...</div>
                <div class="income-statistic">
                    <div class="statistic-cell" v-for="element in allIncome" :key="element.id">
                        <div class="row">
                            <div class="income-title">{{ element.title }}</div>
                            <div class="income-details">{{ element.overall }}{{ $store.state.currency }}</div>
                        </div>
                    </div>
                </div>
                <div class="info-header">Расходы за {{ currentYear }} год</div>
                <div class="message" v-show="!spendingsData">Нет данных...</div>
                <div class="spending-statistic">
                    <div class="statistic-cell" v-for="element in allSpendings" :key="element.id">
                        <div class="row">
                            <div class="spending-title">{{ element.title }}</div>
                            <div class="spending-details">{{ element.overall }}{{ $store.state.currency }}</div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="info-block" v-show="mode == 'Month'">
                <div class="date-bar">
                    <user-select class="select" v-model="currentYear">
                        <option v-for="year in getYears" :key="year">{{ year }}</option>
                    </user-select>
                    <user-select class="select" v-model="currentMonth">
                        <option v-for="month, index in months" :value="index">{{ month }}</option>
                    </user-select>
                    <user-button class="btn" @click="handleMonthRequest">Запрос</user-button>
                </div>

                <div class="info-header">Доходы за {{ getFullMonth }} {{ currentYear }} год</div>
                <div class="message" v-show="!incomeData">Нет данных...</div>
                <div class="income-statistic">
                    <div class="statistic-cell" v-for="element in allIncome" :key="element.id">
                        <div class="row">
                            <div class="income-title">{{ element.title }}</div>
                            <div class="income-details">{{ element.overall }}{{ $store.state.currency }}</div>
                        </div>
                    </div>
                </div>
                <div class="info-header">Расходы за {{ getFullMonth }} {{ currentYear }} год</div>
                <div class="message" v-show="!spendingsData">Нет данных...</div>
                <div class="spending-statistic">
                    <div class="statistic-cell" v-for="element in allSpendings" :key="element.id">
                        <div class="planned row">
                            <div class="category-title">Запланированный расход</div>
                            <div class="spending-title">{{ element.title }}</div>
                            <div class="planned-details">{{ element.planned }}{{ $store.state.currency }}</div>
                        </div>
                        <div class="actual row">
                            <div class="category-title">Фактический расход</div>
                            <div class="spending-title">{{ element.title }}</div>
                            <div class="actual-details"
                                :class="element.planned >= element.overall ? 'positive' : 'negative'">
                                {{ element.overall }}{{ $store.state.currency }}</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import AuthHeaderFull from "@/components/AuthHeaderFull.vue";
import NavBar from "@/components/NavBar.vue";
import UserButton from "@/components/UI/UserButton.vue";
import UserSelect from "@/components/UI/UserSelect.vue";
import { getGeneralStatistic, getAnnualStatistic, getMonthStatistic } from "@/API/apiServices.js";
import { MONTHS } from "@/constants/constants.js"


export default {
    name: "StatisticView",
    components: {
        NavBar,
        AuthHeaderFull,
        UserButton,
        UserSelect,
    },
    data() {
        return {
            token: localStorage.getItem("token"),
            allSpendings: [],
            allIncome: [],
            planList: [],
            mode: null,
            currentYear: "",
            currentMonth: "",
            months: MONTHS,
        }
    },
    methods: {
        handleGeneralStatistic() {
            this.mode = "General";
            this.currentYear = "";
            this.currentMonth = "";
            getGeneralStatistic(this.token).then((response) => {
                this.allIncome = response.data.income
                this.allSpendings = response.data.spending
            }).catch((err) => {
                console.log(err)
            })
        },
        handleAnnualStatistic() {
            this.mode = "Annual";
            this.currentYear = "";
            this.currentMonth = "";
            this.allIncome = "";
            this.allSpendings = "";
        },
        handleMonthStatistic() {
            this.mode = "Month";
            this.currentYear = "";
            this.currentMonth = "";
            this.allIncome = "";
            this.allSpendings = "";
        },
        handleAnnualRequest() {
            getAnnualStatistic(this.token, this.currentYear).then((response) => {
                this.allIncome = response.data.income
                this.allSpendings = response.data.spending
            }).catch((err) => {
                console.log(err)
            })
        },
        handleMonthRequest() {
            getMonthStatistic(this.token, this.currentYear, this.currentMonth).then((response) => {
                this.allIncome = response.data.income
                this.allSpendings = response.data.spending
                console.log(this.allSpendings)
            }).catch((err) => {
                console.log(err)
            })
        }
    },
    computed: {
        getYears() {
            const third = this.$store.state.currentDate.getFullYear()
            const first = third - 2
            const second = third - 1
            return [first, second, third]
        },
        getFullMonth() {
            return MONTHS[this.currentMonth]
        },
        spendingsData() {
            return this.allSpendings.length > 0
        },
        incomeData() {
            return this.allIncome.length > 0
        }
    },
}
</script>

<style scoped>
.statistic-block {
    width: 98%;
    min-height: 60vh;
    margin: 0 auto 50px;
    display: flex;
    flex-direction: column;
    align-items: center;
    border: 0.5px teal solid;
    box-shadow: 0 0 0 3px rgba(0, 128, 128, 0.5);
    padding: 10px;
}

.nav-bar {
    display: flex;
    align-items: center;
}

.info-block {
    display: flex;
    flex-direction: column;
    align-items: center;
}

.header {
    font-family: "Primary", Courier, monospace;
    color: coral;
    margin: 20px;
    font-size: 32px;
}

.info-header {
    font-family: "Secondary", Courier, monospace;
    font-size: 24px;
    font-weight: bolder;
    color: coral;
    margin: 15px;
    padding: 10px;
    text-align: center;
}

.message {
    font-family: "Main", Courier, monospace;
    color: coral;
    margin: 15px;
    padding: 10px;
    text-align: center;
    font-size: 24px;
}

.statistic-cell {
    width: 80vw;
    border: 1px teal solid;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;
    font-family: 'Main', Courier, monospace;
    font-size: 24px;
    color: coral;
}

.row {
    width: 80vw;
    border: 0.1px teal solid;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    font-family: 'Main', Courier, monospace;
    color: coral;
    padding: 15px;
}

.actual {
    background-color: rgba(0, 0, 0, 0.8);
}

.planned {
    background-color: rgba(0, 0, 0, 0.3);
}

.category-title {
    width: 35%;
}

.planned-details,
.actual-details {
    width: 20%;
    text-align: right;
}

.date-bar {
    display: flex;
    flex-direction: row;
    justify-content: center;
}

.btn,
.select {
    min-width: 160px;
    width: 200px;
}

.active {
    outline: 2px coral solid;
    color: red;
}

.positive {
    color: green
}

.negative {
    color: red;
}

@media (max-width: 767px) {

    .btn,
    .select {
        min-width: 60px;
        min-height: 50px;
        width: 100px;
        margin: 10px;
        padding: 5px;
        font-size: 16px;
    }

    .statistic-cell {
        font-size: 12px;
    }
}
</style>