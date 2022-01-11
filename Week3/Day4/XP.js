// Exercise 1: Simple if/else statement
console.log("Ex1:")
let x = 5;
let y = 2;

if (x > y) {
    console.log(`${x} is the biggest number`);
} else {
    console.log(`${y} is the biggest number`);
}

// Exercise 2: Chihuahua
console.log("Ex2:")
let newDog = "Chihuahua";
console.log(newDog.length);
console.log(newDog.toUpperCase(), newDog.toLowerCase());

if (newDog == "Chihuahua") {
    console.log("I love Chihuahuas, it's my favorite dog breed");
} else {
    console.log("I dont care, I prefer cats");
}

// Exercise 3: Even or Odd
console.log("Ex3:")
let userInput = parseInt(prompt("Enter a number"));

if (userInput % 2 == 0) {
    console.log(`${userInput} is an even number`);
} else {
    console.log(`${userInput} is an odd number`);
}

// Exercise 4: Group Chat
console.log("Ex4:")
let users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"];

if (users.length == 0) {
    console.log("No one is online");
} else if (users.length == 1) {
    console.log(`${users[0]} is online`);
} else if(users.length == 2) {
    console.log(`${users[0]} and ${users[1]} are online`);
} else if(users.length > 2) {
    console.log(`${users[0]}, ${users[1]} and ${users.length - 2} others are online`);
}