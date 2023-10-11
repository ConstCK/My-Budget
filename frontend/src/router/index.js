import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/spending",
    name: "spending",
    component: () => import("../views/SpendingView.vue"),
  },
  {
    path: "/income",
    name: "income",
    component: IncomeView,
  },
  {
    path: "/plan",
    name: "plan",
    component: PlanView,
  },
  {
    path: "/statistic",
    name: "statistic",
    component: StatisticView,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
