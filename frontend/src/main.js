import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import { setupCalendar } from "v-calendar";

const app = createApp(App);
app.use(store);
app.use(router);
app.use(setupCalendar, {});
app.mount("#app");
