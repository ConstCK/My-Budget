import { createStore } from "vuex";

export default createStore({
  state: {
    isAuth: false,
    currency: "₽",
    currentDate: new Date(),
  },
  getters: {},
  mutations: {
    logIn(state) {
      state.isAuth = true;
    },
    logOut(state) {
      state.isAuth = false;
    },
  },
  actions: {},
  modules: {},
});
