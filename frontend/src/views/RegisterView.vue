<template>
    <login-block></login-block>
    <register-form v-bind:header="header"></register-form>
</template>

<script>
import LoginBlock from "@/components/LoginBlock.vue";
import RegisterForm from "@/components/RegisterForm.vue";
export default {
    name: "RegisterView",
    components: {
        LoginBlock, RegisterForm
    },
    data() {
        return {
            header: "Страница регистрации"
        }
    }
}
</script>

<style scoped></style>