const twoFer = (who) => {
  who = who || "you";
  return `One for ${who}, one for me.`;
};

console.log(twoFer());

console.log(twoFer("Mikael"));
