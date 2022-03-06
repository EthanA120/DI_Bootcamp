/* TASK: Divisible By Three
    
    let numbers = [123, 8409, 100053, 333333333, 7]

    1. Loop through the array above and determine whether or not each number is divisible by three.
    2. Each time you loop console.log true or false.
*/
let numbers = [123, 8409, 100053, 333333333, 7];

for (let num of numbers) {
    console.log(num % 3 == 0)
}


/* TASK: Attendance
    
    let guestList = {
    randy: "Germany",
    karla: "France",
    wendy: "Japan",
    norman: "England",
    sam: "Argentina"
    }

    Given the object above where the key is the student’s name and the value is the country they are from.
    
    1. Prompt the student for their name.
    2. If the name is in the object, console.log the name of the student and the country they come from.
        For example: "Hi! I'm [name], and I'm from [country]."
            Hint: You don't need to use a for loop, just look up the statement if.. in
    3. If the name is not in the object, console.log: "Hi! I 'm a guest. "
*/

let guestList = {
    randy: "Germany",
    karla: "France",
    wendy: "Japan",
    norman: "England",
    sam: "Argentina"
    };

let nameInput = prompt("Enter your name");

if (nameInput in guestList) {
    console.log(`Hi! I'm ${nameInput}, and I'm from ${guestList[nameInput]}`);
} else {
    console.log("Hi! I'm a guest.")
}


/* TASK: Playing with numbers
    
    let age = [20,5,12,43,98,55];
    Requirements : Don’t use built-in Javascript methods to answer the following questions.
        You have to create the logic by yourself. Use simple for loops.

    1. Console.log the sum of all the numbers in the age array.
    2. Console.log the highest age in the array.
*/
let age = [20,5,12,43,98,55];
let sumOfArray = 0;
let highestAge = 0;

for (let i = 0; i < age.length; i++) {
    sumOfArray += age[i];
    if (highestAge < age[i]) {
        highestAge = age[i];
    }
}
console.log(sumOfArray);
console.log(highestAge);