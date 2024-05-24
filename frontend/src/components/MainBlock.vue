<template>
    <div class="main-block">
        <date-block></date-block>
        <div class="budget">
            Текуший бюджет:
            {{ currentBudget }} {{ $store.state.currency }}
        </div>
        <div class="budget-details">
            <div class="month-income"> Доходы за {{ $store.state.currentDate.toLocaleDateString("ru", { month: "long" }) }}:
                {{ currentIncome }} {{ $store.state.currency }}
            </div>
            <div class="month-spending"> Расходы за {{ $store.state.currentDate.toLocaleDateString("ru", { month: "long" })
            }}:
                {{ currentSpending }} {{ $store.state.currency }}
            </div>
        </div>

    </div>
</template>

<script>
import { getMainData } from '@/API/apiServices.js';
import DateBlock from '@/components/DateBlock.vue';

export default {
    name: "main-block",
    components: {
        DateBlock,
    },
    data() {
        return {
            currentUser: localStorage.getItem("name"),
            token: localStorage.getItem("token"),
            currentBudget: 0,
            currentSpending: 0,
            currentIncome: 0,
        }
    },
    mounted() {

        if (this.currentUser !== null) {
            this.$store.commit("logIn")
            getMainData(this.token).then((response) => {
                this.currentBudget = response.data.balance;
                this.currentIncome = response.data.income["total_income"];
                this.currentSpending = response.data.spending["total_spending"];
            }).catch((error) => {
                console.log("Ошибка получения данных:", error)
            })
        }
    }
}
</script>

<style scoped>
.main-block {
    width: 98%;
    margin: 0 auto;
    border: 0.5px teal solid;
    box-shadow: 0 0 0 3px rgba(0, 128, 128, 0.5);
    text-shadow: 4px 4px 4px rgba(0, 0, 0, 0.6);
}

.budget {
    width: 90%;
    font-family: "Main", Courier, monospace;
    font-size: 48px;
    font-weight: bold;
    color: black;
    background-color: rgba(0, 195, 195, 0.8);
    margin: 20px auto;
    padding: 50px;
    text-align: center;
    border: 0.5px solid;
    border-radius: 30px;
    box-shadow: 0 0 2px 7px rgba(0, 128, 128, 0.4);

}

.budget-details {
    width: 90%;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    margin: 30px auto;
    border-radius: 30px;
    box-shadow: 0 0 2px 7px rgba(0, 128, 128, 0.4);
    overflow: hidden;
}

.month-income,
.month-spending {
    font-family: "Main", Courier, monospace;
    font-size: 32px;
    font-weight: bold;
    background-color: rgba(0, 195, 195, 0.8);
    border: 0.5px solid;
    min-width: 50%;
    padding: 30px;
    text-align: center;
}


@media (max-width: 991px) {
    .budget {
        font-size: 36px;
    }

    .budget-details {
        height: 110px;
    }

    .month-income,
    .month-spending {
        min-height: 100%;
        font-size: 24px;

    }

}

@media (max-width: 767px) {
    .budget {
        font-size: 32px;
        padding: 30px;
    }

    .budget-details {
        height: 90px;
    }

    .month-income,
    .month-spending {
        min-height: 100%;
        font-size: 16px;
    }
}
</style>