const authValidation = (password) => {
  let isNum = false;
  let isStr = false;
  let size = false;

  for (let i = 0; i < password.length; i++) {
    if (/^[0-9]$/.test(password[i])) {
      isNum = true;
    } else if (/^[a-zA-Z]+$/.test(password[i])) {
      isStr = true;
    }
  }
  if (password.length > 7) {
    size = true;
  }
  return size && isStr && isNum;
};

const budgetValidation = (amount) => {
  return amount.length > 0 && Number.isInteger(Number(amount));
};

export { authValidation, budgetValidation };
