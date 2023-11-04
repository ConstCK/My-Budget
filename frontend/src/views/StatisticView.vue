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
                <div class="data-bar">
                    <user-button class="btn" :class="dataDisplay == 'all' ? 'active' : 'inactive'"
                        @click="handleAllRequest">Все</user-button>
                    <user-button class="btn" :class="dataDisplay == 'categorized' ? 'active' : 'inactive'"
                        @click="handleCategorizedRequest">По категориям</user-button>
                    <user-button class="btn" :class="dataDisplay == 'chart' ? 'active' : 'inactive'"
                        @click="handleChartRequest">Графики</user-button>
                </div>
                <div class="info-header" v-show="dataDisplay !== 'chart'">Доходы</div>
                <div class="message" v-show="!incomeData">Нет данных...</div>
                <bar-chart v-show="dataDisplay === 'chart'" v-if="loaded" :data="incomeChartData"
                    :options="incomeOptions"></bar-chart>
                <div class="income-statistic" v-show="dataDisplay === 'categorized'">
                    <div class="statistic-cell" v-for="element in allIncome" :key="element.id">
                        <div class="row">
                            <div class="income-title">{{ element.title }}</div>
                            <div class="income-amount">{{ element.overall }}{{ $store.state.currency }}</div>
                        </div>
                    </div>
                </div>
                <div class="income-statistic" v-show="dataDisplay === 'all'">
                    <div class="statistic-cell" v-for="element in allIncome" :key="element.id">
                        <div class="row">
                            <div class="income-title">{{ element.category_title }}</div>
                            <div class="income-description">{{ element.description }}</div>
                            <div class="income-date">{{ element.created_at }}</div>
                            <div class="income-amount">{{ element.amount }}{{ $store.state.currency }}</div>
                        </div>
                    </div>
                </div>
                <div class="info-header" v-show="dataDisplay !== 'chart'">Расходы</div>
                <div class="message" v-show="!spendingsData">Нет данных...</div>
                <bar-chart v-show="dataDisplay === 'chart'" v-if="loaded" :data="spendingChartData"
                    :options="spendingOptions"></bar-chart>
                <div class="spending-statistic" v-show="dataDisplay === 'categorized'">
                    <div class="statistic-cell" v-for="element in allSpendings" :key="element.id">
                        <div class="row">
                            <div class="spending-title">{{ element.title }}</div>
                            <div class="spending-details">{{ element.overall }}{{ $store.state.currency }}</div>
                        </div>
                    </div>
                </div>
                <div class="spending-statistic" v-show="dataDisplay === 'all'">
                    <div class="statistic-cell" v-for="element in allSpendings" :key="element.id">
                        <div class="row">
                            <div class="spending-title">{{ element.category_title }}</div>
                            <div class="spending-description">{{ element.description }}</div>
                            <div class="spending-date">{{ element.created_at }}</div>
                            <div class="spending-amount">{{ element.amount }}{{ $store.state.currency }}</div>
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
                            <div class="income-amount">{{ element.overall }}{{ $store.state.currency }}</div>
                        </div>
                    </div>
                </div>
                <div class="info-header">Расходы за {{ currentYear }} год</div>
                <div class="message" v-show="!spendingsData">Нет данных...</div>
                <div class="spending-statistic">
                    <div class="statistic-cell" v-for="element in allSpendings" :key="element.id">
                        <div class="row">
                            <div class="spending-title">{{ element.title }}</div>
                            <div class="spending-amount">{{ element.overall }}{{ $store.state.currency }}</div>
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
                            <div class="income-amount">{{ element.overall }}{{ $store.state.currency }}</div>
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
                            <div class="planned-amount">{{ element.planned }}{{ $store.state.currency }}</div>
                        </div>
                        <div class="actual row">
                            <div class="category-title">Фактический расход</div>
                            <div class="spending-title">{{ element.title }}</div>
                            <div class="actual-amount"
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
import { getGeneralStatistic, getAnnualStatistic, getMonthStatistic, getAllStatistic } from "@/API/apiServices.js";
import { MONTHS } from "@/constants/constants.js"
import BarChart from "@/components/UI/BarChart.vue";


export default {
    name: "statistic-view",
    components: {
        NavBar,
        AuthHeaderFull,
        UserButton,
        UserSelect,
        BarChart,
    },
    data() {
        return {
            token: localStorage.getItem("token"),
            allSpendings: [],
            allIncome: [],
            dataDisplay: "all",
            planList: [],
            mode: null,
            currentYear: "",
            currentMonth: "",
            months: MONTHS,
            loaded: false,
            incomeChartData: {
                labels: [],
                datasets: [
                    {
                        label: 'Доходы',
                        backgroundColor: '#008080',
                        data: []
                    },
                ]
            },
            spendingChartData: {
                labels: [],
                datasets: [
                    {
                        label: 'Расходы',
                        backgroundColor: '#FF4500',
                        data: []
                    },
                ]
            },
            spendingOptions: {
                responsive: true,
                maintainAspectRatio: true,
                plugins: {
                    legend: {
                        position: 'top',
                        labels: {
                            color: "#FFFFFF",
                            font: {
                                size: 24,
                                family: 'Main',
                            }
                        }
                    },
                },
                scales: {
                    x: {
                        ticks: {
                            font: {
                                family: 'Main',
                            },
                            autoSkip: false,
                            maxRotation: 95,
                            minRotation: 85,
                            color: "#FFFFFF",
                            padding: 15,
                        }
                    },
                    y: {
                        ticks: {
                            color: "#FFFFFF",
                        }
                    }
                }
            },
            incomeOptions: {
                responsive: true,
                maintainAspectRatio: true,
                plugins: {
                    legend: {
                        position: 'top',
                        labels: {
                            color: "#FFFFFF",
                            font: {
                                size: 24,
                                family: 'Main',
                            }
                        }
                    },
                },
                scales: {
                    x: {
                        ticks: {
                            font: {
                                family: 'Main',
                            },
                            color: "#FFFFFF",
                            padding: 15,
                        }
                    },
                    y: {
                        ticks: {
                            color: "#FFFFFF",
                        }
                    }
                }
            }
        }
    },
    methods: {
        handleGeneralStatistic() {
            this.mode = "General";
            this.currentYear = "";
            this.currentMonth = "";
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
        handleAllRequest() {
            getAllStatistic(this.token).then((response) => {
                this.dataDisplay = "all";
                this.allIncome = response.data.income
                this.allSpendings = response.data.spending
            }).catch((err) => {
                console.log(err)
            })
        },
        handleCategorizedRequest() {
            getGeneralStatistic(this.token).then((response) => {
                this.dataDisplay = "categorized";
                this.allIncome = response.data.income;
                this.allSpendings = response.data.spending;
            }).catch((err) => {
                console.log(err)
            })
        },
        handleChartRequest() {
            getGeneralStatistic(this.token).then((response) => {
                this.dataDisplay = "chart";
                this.allIncome = response.data.income;
                this.allSpendings = response.data.spending;
                this.incomeChartData["labels"] = this.getIncomeLabels
                this.incomeChartData["datasets"][0]["data"] = this.getIncomeData
                this.spendingChartData["labels"] = this.getSpendingLabels
                this.spendingChartData["datasets"][0]["data"] = this.getSpendingData
                this.loaded = true;
            }).catch((err) => {
                console.log(err)
            })
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
        },
        getIncomeLabels() {
            let result = [];
            this.allIncome.forEach((e) => {
                result.push(e.title)
            })
            return result
        },
        getSpendingLabels() {
            let result = [];
            this.allSpendings.forEach((e) => {
                result.push(e.title)
            })
            return result
        },
        getIncomeData() {
            let result = [];
            this.allIncome.forEach((e) => {
                result.push(e.overall)
            })
            return result
        },
        getSpendingData() {
            let result = [];
            this.allSpendings.forEach((e) => {
                result.push(e.overall)
            })
            return result
        },
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
    margin: 5px 15px;
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

.income-title,
.spending-title {
    min-width: 20%;
    text-align: start;
    margin: 10px;
}

.income-description,
.spending-description {
    min-width: 32%;
    text-align: center;
    margin: 10px;
}

.income-date,
.spending-date {
    min-width: 18%;
    margin: 10px;
}

.income-amount,
.spending-amount {
    min-width: 15%;
    text-align: end;
    margin: 10px;
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

.planned-amount,
.actual-amount {
    width: 20%;
    text-align: right;
}

.date-bar,
.data-bar {
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

@media (max-width: 991px) {
    .info-header {
        margin: 10px;
        font-size: 28px;
    }

    .row {
        padding: 5px;
    }

    .row>div {
        margin: 5px;
    }

    .statistic-cell {
        font-size: 16px;
    }
}

@media (max-width: 767px) {

    .btn,
    .select {
        min-width: 60px;
        min-height: 30px;
        width: 100px;
        margin: 10px;
        padding: 5px;
        font-size: 16px;
    }

    .statistic-cell {
        font-size: 10px;
    }

    .info-header {
        margin: 10px;
        font-size: 24px;
    }

    .message {
        margin: 5px;
        font-size: 18px;
    }

}
</style>