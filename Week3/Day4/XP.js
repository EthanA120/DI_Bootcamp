/* TASK: Simple if/else statement

    1. Create 2 variables, x and y. Each of them should have a different numeric value.
    2. Write an if/else statement that checks which number is bigger.

    Example:
        let x = 5;
        let y = 2;

        You should display:
        x is the biggest number
*/
let x = 5;
let y = 2;

if (x > y) {
    console.log(`${x} is the biggest number`);
} else {
    console.log(`${y} is the biggest number`);
}

/* TASK: Chihuahua
    
    1. Create a variable called newDog where it's value is "Chihuahua".
    2. Check and display how many letters are in newDog.
    3. Display the newDog variable in uppercase and then in lowercase
        (no need to create new variables, just console.log twice).
    4. Check if the variable newDog is equal to "Chihuahua"
        - if it does, display '1 love Chihuahuas, it's my favorite dog breed'
        - else, console. log '1 dont care, I prefer cats'
*/
let newDog = "Chihuahua";
console.log(newDog.length);
console.log(newDog.toUpperCase(), newDog.toLowerCase());

if (newDog == "Chihuahua") {
    console.log("I love Chihuahuas, it's my favorite dog breed");
} else {
    console.log("I dont care, I prefer cats");
}

/* TASK: Even or Odd
        
    1. Prompt the user for a number and save it to a variable.
    2. Check whether the variable is even or odd.
        - If it is even, display: "x is an even number". Where x is the actual number the user chose.
        - If it is odd, display: "x is an odd number". Where x is the actual number the user chose.
*/
let userInput = parseInt(prompt("Enter a number"));

if (userInput % 2 == 0) {
    console.log(`${userInput} is an even number`);
} else {
    console.log(`${userInput} is an odd number`);
}

/* TASK: Group Chat
    
    Below is an array of users that are online in a group chat.
        let users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"]

    Using the array above, console.log the number of users that are connected to the group chat based on the following rules:
        - If there is no users (the users array is empty), console.log “no one is online”.
        - If there is 1 user, console.log “<name_user> is online”.
        - If there are 2 users, console.log “<name_user1> and <name_user2> are online”.
        - If there are more than 2 users, console.log the first two names in the users array and the number of additional users online.
        
        For example, if there are 5 users, it should display:
            name_user1, name_user2 and 3 more are online
*/
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