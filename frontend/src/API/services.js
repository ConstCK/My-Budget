import axios from "axios";
import {
  BASE_URL,
  LOGIN_URL,
  MAIN_DATA_URL,
  REGISTER_URL,
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

const getMainData = async () => {
  try {
    const response = await axios({
      baseURL: BASE_URL,
      url: MAIN_DATA_URL,
      method: "get",
      headers: {
        Authorization: "Token " + token,
      },
    });
    console.log(response);
    return response;
  } catch (error) {
    console.log(`Ошибка получения данных: ${error}`);
  }
};

export { login, register, getMainData };
