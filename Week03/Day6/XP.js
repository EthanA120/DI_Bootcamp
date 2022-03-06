/* TASK: List of people

    let people = ["Greg", "Mary", "Devon", "James"]

    1. Write code to remove "Greg" from the people array.
    2. Write code to replace "James" to "Jason".
    3. Write code to add your name to the end of the people array.
    4. Write code that console.logs Mary's index. take a look at the indexof method on Google.
    5. Write code to make a copy of the people array using the slice method.
        - The copy should NOT include "Mary" or your name.
        - Hint: remember that now the people array should look like this let people = ["Mary", "Devon", "Jason ", "Yourname"]
        - Hint: Check out the documentation for the slice method
    6. Write code that gives the index of "Foo". Why does it return -1?
    7. Create a variable called last which value is the last element of the array.
    
    Hint: What is the relationship between the index of the last element in the array and the length of the array?
*/
// Part 1
let people = ["Greg", "Mary", "Devon", "James"];

people.splice(0,1);
people.splice(2, 1, "Jason");
people.push("Ethan")
console.log(people.indexOf("Mary"));
let peopleCopy = people.slice(1, people.length - 1);
console.log(people.indexOf("Foo")); // It can't find the word "Foo" in the array so it returns undefined index -1
let last = peopleCopy[people.length - 1]

console.log(people);
console.log(peopleCopy);

// Part 2
for (let i = 0; i < people.length; i++) {
    console.log(people[i]);
}

for (let i = 0; i < people.length; i++) {
    console.log(people[i]);
    if (people[i] == "Jason") {
        break;
    }
}


/* TASK: Your favorite colors
    
    1. Create an array called colors where the value is a list of your five favorite colors.
    2. Loop through the array and as you loop console.log a string like so: "My #1 choice is blue", "My #2 choice is red" ect...
    3. Bonus: Change it to console.log "My 1st choice", "My 2nd choice", "My 3rd choice", picking the correct suffix for each number.
        Hint: create an array of suffixes to do the Bonus
*/
let colors = ["white", "black", "red", "green", "blue"];
let suffix = ["st", "nd", "rd", "th", "th"];

for (let i = 0; i < colors.length; i++) {
    console.log(`My #${i+1} choice is ${colors[i]}`);
}

for (let i = 0; i < colors.length; i++) {
    console.log(`My ${i+1}${suffix[i]} choice is ${colors[i]}`);
}


/* TASK: Repeat the question
    
    1. Prompt the user for a number.
        Hint : Check the data type you receive from the prompt (ie. Use the typeof method)

    2. While the number is smaller than 10 continue asking the user for a new number.
        Tip : Which while loop is more relevant for this situation?

*/
let userNum = parseInt(prompt("Enter a number"));
console.log(userNum);

while (userNum < 10) {
    userNum = parseInt(prompt("Enter a number"));
    console.log(userNum);
}


/* TASK: Building Management
    
    let building = {
        numberOfFloors : 4,
        numberOfAptByFloor : {
            firstFloor : 3,
            secondFloor : 4,
            thirdFloor : 9,
            fourthFloor : 2,
        },
        nameOfTenants : ["Sarah", "Dan", "David"],
        numberOfRoomsAndRent:  {
            sarah: [3, 990],
            dan :  [4, 1000],
            david : [1, 500],
        },
    }

    1. Copy and paste this object to your Javascript file.
    2. Console.log the number of floors in the building.
    3. Console.log how many apartments are on the floors 1 and 3.
    4. Console.log the name of the second tenant and the number of rooms he has in his apartment.
    5. Check if the sum of Sarah's and David's rent is bigger than Dan's rent. If it is, than increase Dan's rent to 1200.
*/
let building = {
    numberOfFloors : 4,
    numberOfAptByFloor : {
        firstFloor : 3,
        secondFloor : 4,
        thirdFloor : 9,
        fourthFloor : 2,
    },
    nameOfTenants : ["Sarah", "Dan", "David"],
    numberOfRoomsAndRent:  {
        sarah: [3, 990],
        dan :  [4, 1000],
        david : [1, 500],
    },
};

console.log(building.numberOfFloors);
console.log(building["numberOfAptByFloor"]["firstFloor"], building.numberOfAptByFloor["thirdFloor"]);
console.log(building.nameOfTenants[1], building.numberOfRoomsAndRent[building.nameOfTenants[1].toLowerCase()][0]);

if (building.numberOfRoomsAndRent["sarah"][1] + building.numberOfRoomsAndRent["david"][1] > building.numberOfRoomsAndRent["dan"][1]) {
    building.numberOfRoomsAndRent["dan"][1] = 1200;
    console.log(building.numberOfRoomsAndRent["dan"][1]);
}


/* TASK: Family
    
    1. Create an object called family with a few key value pairs.
    2. Using a for loop, console.log the keys of the object.
    3. Using a for loop, console.log the values of the object.
*/

let family = {father: "Homer", mother: "Marge", son: "Bart", daughter: "Lisa", baby: "Maggie"};

for (let key in family) {
    console.log(key);
    console.log(family[key])
}


/* TASK: 
    
    let details = {
        my: 'name',
        is: 'Rudolf',
        the: 'raindeer'
    }

    Given the object above and using a for loop, console.log “my name is Rudolf the raindeer”
*/
let details = { my: 'name', is: 'Rudolf', the: 'raindeer'};
let sentense = "";
for (let key in details) {
    sentense += `${key} ${details[key]} `;
}
console.log(sentense);


/* TASK: Secret Group
    
    let names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];

    
    1. A group of friends have decided to start a secret society.
        The society’s name will be the first letter of each of their names sorted in alphabetical order.
        Hint: a string is an array of letters
    2. Console.log the name of their secret society. The output should be “ABJKPS”
*/
let names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
names.sort();
let societyName = "";

for (let i = 0; i < names.length; i++) {
    societyName += names[i][0];
}

console.log(societyName)