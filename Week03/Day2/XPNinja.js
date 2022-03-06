// Exercise 1: Evaluation
console.log(5 >= 1) // true - 5 is bigger than 1
console.log(0 === 1) // false - 0 is equal to 1 by type but not by value
console.log(4 <= 1) // false - 4 is neither equal to 4 nor bigger than it
console.log(1 != 1) // false - 1 isn't different than 1
console.log("A" > "B") // false - ASCII value of A is smaller than B
console.log("B" < "C") // true - ASCII value of C is bigger than B
console.log("a" > "A") // true - ASCII value of a is bigger than A
console.log("b" < "A") // false - ASCII value of lowercase latin letters are bigger than the uppercase ones
console.log(true === false) // false - true is equal to false by type but not by value
console.log(true != true) // false - true isn't different than true

// Exercise 2: Ask for numbers
let numStr = prompt('Enter numbers seperated with ","').split(",");
console.log(numStr.reduce((a, b) => parseInt(a) + parseInt(b)));

// Exercise 3: Find Nemo
let userInput = prompt("Enter something");
let nemoIndex = userInput.split(" ").indexOf("Nemo");

if(nemoIndex >= 0){
console.log("I found Nemo at", nemoIndex);
}
else {
    console.log("I can't find Nemo");
}

// Exercise 4: Boom
let userStr = parseInt(prompt("Enter a number"));
let output;

if(userStr <= 2) {
    output = "boom";
}
if(userStr > 2) {
    output = "b" + "o".repeat(userStr) + "m";
}
if(userStr % 2 == 0 && userStr >= 2){
    output += "!";
}
if(userStr % 5 == 0 && userStr > 2){
    output = output.toUpperCase();
}

console.log(output)