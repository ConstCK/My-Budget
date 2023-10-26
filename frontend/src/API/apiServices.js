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

const getMainData = async (user, token) => {
  try {
    const response = await axios({
      baseURL: BASE_URL,
      url: MAIN_DATA_URL,
      method: "post",
      headers: {
        Authorization: "Token " + token,
      },
      data: {
        user: user,
      },
    });
    return response;
  } catch (error) {
    console.log(`Ошибка получения данных: ${error}`);
  }
};

const getIncomeCategories = async (user, token) => {
  try {
    const response = await axios({
      baseURL: BASE_URL,
      url: INCOME_CATEGORY_URL,
      method: "post",
      headers: {
        Authorization: "Token " + token,
      },
      data: {
        user: user,
      },
    });
    return response;
  } catch (error) {
    console.log(`Ошибка получения данных: ${error}`);
  }
};

const getSpendingCategories = async (user, token) => {
  try {
    const response = await axios({
      baseURL: BASE_URL,
      url: SPENDING_CATEGORY_URL,
      method: "post",
      headers: {
        Authorization: "Token " + token,
      },
      data: {
        user: user,
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

const addCategory = async (user, title, description, mode, token) => {
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
        user: user,
        title: title,
        description: description,
      },
    });
    return response;
  } catch (error) {
    console.log(`Ошибка добавления данных: ${error}`);
  }
};

const addIncome = async (user, token, data) => {
  try {
    const response = await axios({
      baseURL: BASE_URL,
      url: ADD_INCOME_URL,
      method: "post",
      headers: {
        Authorization: "Token " + token,
      },
      data: {
        user: user,
        data: data,
      },
    });
    return response;
  } catch (error) {
    console.log(`Ошибка добавления данных: ${error}`);
  }
};

const addSpending = async (user, token, data) => {
  try {
    const response = await axios({
      baseURL: BASE_URL,
      url: ADD_SPENDING_URL,
      method: "post",
      headers: {
        Authorization: "Token " + token,
      },
      data: {
        user: user,
        data: data,
      },
    });
    return response;
  } catch (error) {
    console.log(`Ошибка добавления данных: ${error}`);
  }
};

const getPlans = async (user, token) => {
  try {
    const response = await axios({
      baseURL: BASE_URL,
      url: PLANS_URL,
      method: "post",
      headers: {
        Authorization: "Token " + token,
      },
      data: {
        user: user,
      },
    });
    return response;
  } catch (error) {
    console.log(`Ошибка получения данных: ${error}`);
  }
};

const updatePlans = async (user, token, data) => {
  try {
    const response = await axios({
      baseURL: BASE_URL,
      url: UPDATE_PLANS_URL,
      method: "post",
      headers: {
        Authorization: "Token " + token,
      },
      data: {
        user: user,
        data: data,
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
};
