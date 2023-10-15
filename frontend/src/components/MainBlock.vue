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
import { getMainData } from '@/API/services';
import DateBlock from './DateBlock.vue';

export default {
    name: "main-block",
    components: {
        DateBlock,
    },
    data() {
        return {
            currentBudget: 0,
            currentSpending: 0,
            currentIncome: 0,
            token: localStorage.getItem("token")
        }
    },
    methods: {

    },
    mounted() {
        // getMainData(this.token)
    }
}
</script>

<style scoped>
.main-block {
    width: 99%;
    min-height: 60vh;
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
}

.month-income {
    font-family: "Main", Courier, monospace;
    font-size: 36px;
    font-weight: bold;
    background-color: rgba(0, 195, 195, 0.8);
    border: 0.5px solid;
    width: 50%;
    padding: 40px 20px;
    text-align: center;
}

.month-spending {
    font-family: "Main", Courier, monospace;
    font-size: 36px;
    font-weight: bold;
    width: 50%;
    background-color: rgba(0, 195, 195, 0.8);
    border: 0.5px solid;
    padding: 40px 20px;
    text-align: center;
}
</style>