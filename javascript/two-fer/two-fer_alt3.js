export const twoFer = (name) => {
  let string1 = `One for you, one for me.`;
  let string2 = `One for ${name}, one for me.`;

  let outputString = name == "" || name == null ? string1 : string2;

  return outputString;
};
