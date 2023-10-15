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
    component: () => import("../views/IncomeView.vue"),
  },
  {
    path: "/plan",
    name: "plan",
    component: () => import("../views/PlanView.vue"),
  },
  {
    path: "/statistic",
    name: "statistic",
    component: () => import("../views/StatisticView.vue"),
  },
  {
    path: "/settings",
    name: "settings",
    component: () => import("../views/SettingsView.vue"),
  },
  {
    path: "/login",
    name: "login",
    component: () => import("../views/LoginView.vue"),
  },
  {
    path: "/register",
    name: "register",
    component: () => import("../views/RegisterView.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
