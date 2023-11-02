import axios from "axios";
import {
  BASE_URL,
  INCOME_CATEGORY_URL,
  SPENDING_CATEGORY_URL,
  LOGIN_URL,
  MAIN_DATA_URL,
  REGISTER_URL,
  DELETE_INCOME_CATEGORY_URL,
  DELETE_SPENDING_CATEGORY_URL,
  ADD_INCOME_CATEGORY_URL,
  ADD_SPENDING_CATEGORY_URL,
  ADD_INCOME_URL,
  ADD_SPENDING_URL,
  PLANS_URL,
  UPDATE_PLANS_URL,
  GENERAL_STATISTIC_URL,
  ANNUAL_STATISTIC_URL,
  MONTH_STATISTIC_URL,
  ALL_STATISTIC_URL,
} from "@/constants/constants";

const login = async (user, password) => {
  try {
    const response = await axios({
      baseURL: BASE_URL,
      url: LOGIN_URL,
      method: "post",
      data: {
        username: user,
        password: password,
      },
    });
    return response;
  } catch (error) {
    console.log(`Неверные данные: ${error}`);
  }
};

const register = async (user, password) => {
  try {
    const response = await axios({
      baseURL: BASE_URL,
      url: REGISTER_URL,
      method: "post",
      data: {
        username: user,
        password: password,
      },
    });
    return response;
  } catch {
    console.log(`Неверные данные: ${error}`);
  }
};

const getMainData = async (token) => {
  try {
    const response = await axios({
      baseURL: BASE_URL,
      url: MAIN_DATA_URL,
      method: "get",
      headers: {
        Authorization: "Token " + token,
      },
    });
    return response;
  } catch (error) {
    console.log(`Ошибка получения данных: ${error}`);
  }
};

const getIncomeCategories = async (token) => {
  try {
    const response = await axios({
      baseURL: BASE_URL,
      url: INCOME_CATEGORY_URL,
      method: "get",
      headers: {
        Authorization: "Token " + token,
      },
    });
    return response;
  } catch (error) {
    console.log(`Ошибка получения данных: ${error}`);
  }
};

const getSpendingCategories = async (token) => {
  try {
    const response = await axios({
      baseURL: BASE_URL,
      url: SPENDING_CATEGORY_URL,
      method: "get",
      headers: {
        Authorization: "Token " + token,
      },
    });
    return response;
  } catch (error) {
    console.log(`Ошибка получения данных: ${error}`);
  }
};

const deleteIncomeCategory = async (id, token) => {
  try {
    const response = await axios({
      baseURL: BASE_URL,
      url: DELETE_INCOME_CATEGORY_URL,
      method: "post",
      headers: {
        Authorization: "Token " + token,
      },
      data: {
        id: id,
      },
    });
    return response;
  } catch (error) {
    console.log(`Ошибка удаления данных: ${error}`);
  }
};

const deleteSpendingCategory = async (id, token) => {
  try {
    const response = await axios({
      baseURL: BASE_URL,
      url: DELETE_SPENDING_CATEGORY_URL,
      method: "post",
      headers: {
        Authorization: "Token " + token,
      },
      data: {
        id: id,
      },
    });
    return response;
  } catch (error) {
    console.log(`Ошибка удаления данных: ${error}`);
  }
};

const addCategory = async (title, description, mode, token) => {
  try {
    const response = await axios({
      baseURL: BASE_URL,
      url:
        mode == "Income" ? ADD_INCOME_CATEGORY_URL : ADD_SPENDING_CATEGORY_URL,
      method: "post",
      headers: {
        Authorization: "Token " + token,
      },
      data: {
        title: title,
        description: description,
      },
    });
    return response;
  } catch (error) {
    console.log(`Ошибка добавления данных: ${error}`);
  }
};

const addIncome = async (token, data) => {
  try {
    const response = await axios({
      baseURL: BASE_URL,
      url: ADD_INCOME_URL,
      method: "post",
      headers: {
        Authorization: "Token " + token,
      },
      data: {
        data: data,
      },
    });
    return response;
  } catch (error) {
    console.log(`Ошибка добавления данных: ${error}`);
  }
};

const addSpending = async (token, data) => {
  try {
    const response = await axios({
      baseURL: BASE_URL,
      url: ADD_SPENDING_URL,
      method: "post",
      headers: {
        Authorization: "Token " + token,
      },
      data: {
        data: data,
      },
    });
    return response;
  } catch (error) {
    console.log(`Ошибка добавления данных: ${error}`);
  }
};

const getPlans = async (token) => {
  try {
    const response = await axios({
      baseURL: BASE_URL,
      url: PLANS_URL,
      method: "get",
      headers: {
        Authorization: "Token " + token,
      },
    });
    return response;
  } catch (error) {
    console.log(`Ошибка получения данных: ${error}`);
  }
};

const updatePlans = async (token, data) => {
  try {
    const response = await axios({
      baseURL: BASE_URL,
      url: UPDATE_PLANS_URL,
      method: "post",
      headers: {
        Authorization: "Token " + token,
      },
      data: {
        data: data,
      },
    });
    return response;
  } catch (error) {
    console.log(`Ошибка получения данных: ${error}`);
  }
};

const getGeneralStatistic = async (token) => {
  try {
    const response = await axios({
      baseURL: BASE_URL,
      url: GENERAL_STATISTIC_URL,
      method: "get",
      headers: {
        Authorization: "Token " + token,
      },
    });
    return response;
  } catch (error) {
    console.log(`Ошибка получения данных: ${error}`);
  }
};

const getAllStatistic = async (token) => {
  try {
    const response = await axios({
      baseURL: BASE_URL,
      url: ALL_STATISTIC_URL,
      method: "get",
      headers: {
        Authorization: "Token " + token,
      },
    });
    return response;
  } catch (error) {
    console.log(`Ошибка получения данных: ${error}`);
  }
};

const getAnnualStatistic = async (token, year) => {
  try {
    const response = await axios({
      baseURL: BASE_URL,
      url: ANNUAL_STATISTIC_URL,
      method: "post",
      headers: {
        Authorization: "Token " + token,
      },
      data: {
        year: year,
      },
    });
    return response;
  } catch (error) {
    console.log(`Ошибка получения данных: ${error}`);
  }
};

const getMonthStatistic = async (token, year, month) => {
  try {
    const response = await axios({
      baseURL: BASE_URL,
      url: MONTH_STATISTIC_URL,
      method: "post",
      headers: {
        Authorization: "Token " + token,
      },
      data: {
        year: year,
        month: month,
      },
    });
    return response;
  } catch (error) {
    console.log(`Ошибка получения данных: ${error}`);
  }
};

export {
  login,
  register,
  getMainData,
  getIncomeCategories,
  getSpendingCategories,
  deleteIncomeCategory,
  deleteSpendingCategory,
  addCategory,
  addIncome,
  addSpending,
  getPlans,
  updatePlans,
  getGeneralStatistic,
  getAnnualStatistic,
  getMonthStatistic,
  getAllStatistic,
};
