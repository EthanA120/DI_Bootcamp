// Ex1: Favorite Color
let me = ["my","favorite","color","is","blue"]
console.log(me.join(" "))

// Ex2: Mixup
let str1 = "Hello";
let str2 = "World";

let finalString = str2.slice(0, 2) + str1.slice(2, str1.length) + " " + str1.slice(0, 2) + str2.slice(2, str1.length);
console.log(finalString);

// Ex3: Calculator
let num1 = parseInt(prompt("Enter the first number"));
let num2 = parseInt(prompt("Enter the second number"));
alert(num1 + num2)
