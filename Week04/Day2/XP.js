/* TASK: Information
    
    Part I: function with no parameters
    1. Create a function called infoAboutMe () that takes no parameter.
    2. The function should console.log a sentence about you (ie. your name, age, hobbies ect...).
    3. Call the function.
    
    Part II: function with three parameters
    1. Create a function called infoAbout Person (personName, personAge, person FavoriteColor) that takes 3 parameters.
    2. The function should console.log a sentence about the person (ie. "You name is .., you are.
        years old, your favorite color is
    3. Call the function twice with the following arguments:
        infoAboutPerson ("David", 45, "blue ")
        infoAboutPerson ( "Josh ", 12, "yellow")
*/
// Part 1
function infoAboutMe(){
    console.log("My name is Ethan");
}

infoAboutMe();

// Part 2
function infoAboutPerson(personName, personAge, personFavoriteColor){
    
    console.log(`Your name is ${personName}, you are ${personAge} years old, your favorite color is ${personFavoriteColor}`);
}

infoAboutPerson("David", 45, "blue");
infoAboutPerson("Josh", 12, "yellow");


/* TASK: Tips
    
    John created a simple tip calculator to help calculate how much to tip when he and his family go to restaurants.

    1. Create a function named calculateTip () that takes no parameter.
    2. Inside the function, ask John for the amount of the bill.
    3. Here are the rules
        If the bill is less than $50, tip 20%.
        If the bill is between $50 and $200, tip 15%.
        If the bill is more than $200, tip 10%.
    4. Console.log the tip amount and the final bill (bill + tip).
    5. Call the calculateTip () function.
*/
function calculateTip(){
    
    let userBill = parseInt(prompt("Enter the bill"));
    let tip;

    if (userBill < 50){
        tip = 0.2;
    } else if (50 <= userBill && userBill < 200) {
        tip = 0.15;
    } else if (200 <= userBill) {
        tip = 0.1;
    }

    console.log(`Bill is ${userBill}, tip is ${tip}, the calculated bill is ${tip * userBill + userBill}`);
}

calculateTip();


/* TASK: Find the numbers divisible by 23
    
    1. Create a function call isDivisible () that takes no parameter.
    2. In the function, Ioop through numbers O to 500.
    3. Console.log all the numbers divisible by 23.
    4. At the end, console.log the sum of all numbers that are divisible by 2
        Outcome : 0 23 46 69 92 115 138 161 184 207 230 253 276 299 322 345 368 391 414 437 460 483
        Sum : 5313
    5. Bonus: Add a parameter divisor to the function.
        isDivisible(divisor)
        
        Example:
        isDivisible(3) : Console.log all the numbers divisible by 3, and their sum
        isDivisible(45) : Console.log all the numbers divisible by 45, and their sum
*/
function isDivisible(divisor){
    
    let outcome = [];
    let j = 0;
    let sum = 0;

    for (let i = 0; i < 500; i++) {
        if (i % divisor == 0) {
            outcome[j] = i;
            sum += i;
            j++;
        }
    }
    console.log(outcome)
    console.log(sum);
}

isDivisible(23);


/* TASK: Shopping List
    
    let stock = {
        "banana": 6, 
        "apple": 0,
        "pear": 12,
        "orange": 32,
        "blueberry":1
    }

    let prices = {
        "banana": 4, 
        "apple": 2, 
        "pear": 1,
        "orange": 1.5,
        "blueberry":10
    }

    1. Add the stock and prices objects to your js file.
    2. Create an array called shoppingList with the following items:
        "banana", "orange", and "apple". It means that you have 1 banana, 1 orange and 1 apple in your cart.
    3. Create a function called myBill() that takes no parameters.
    4. The function should return the total price of your shoppingList. In order to do this you must follow these rules:
        1. The item must be in stock.
        2. If the item is in stock find out the price in the prices object.
    5. Call the myBill () function.
    6. Bonus: If the item is in stock, decrease the item's stock by 1
*/
let stock = { 
    "banana": 6, 
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry":1
}

let prices = {    
    "banana": 4, 
    "apple": 2, 
    "pear": 1,
    "orange": 1.5,
    "blueberry":10
}

let shoppingList = ["banana", "orange", "apple"];

function myBill(){

    let sum = 0;
    for (const item of shoppingList) {
        if (item in stock && stock[item] > 0) {
            sum += prices[item];
            stock[item]--;            
        }
    }
    
    console.log(sum);
    console.log(stock);
}

myBill();


/* TASK: What’s in my wallet?
    
    Note: Read the illustration (point 4), while reading the instructions.

    1. Create a function named changeEnough (itemPrice, amountofchange) that receives two arguments:
        - an item price.
        - and an array representing the amount of change in your pocket.

    2. In the function, determine whether or not you can afford the item.
        - If the sum of the change is bigger or equal than the item's price (ie. it means that you can afford the item), the function should return true
        - If the sum of the change is smaller than the item's price (ie. it means that you cannot afford the item) the function should return false.

    3. Change will always be represented in the rollowing order quarters, dimes, nickels, pennies.
        A quarters is 0.25
        A dimes is 0.10
        A nickel is 0.05
        A penny is 0.01

    4. To illustrate:
        After you created the function, invoke it like this:

        changeEnough(4.25, [25, 20, 5, 0]);

        - The value 4.25 represents the item’s price.
        - The array [25, 20, 5, 0] represents 25 quarters, 20 dimes, 5 nickels and 0 pennies.
        - The function should return true, since having 25 quarters, 20 dimes, 5 nickels and 0 pennies gives you 6.25 + 2 + .25 + 0 = 8.50 which is bigger than 4.25 (the total amount due)
*/
function changeEnough(itemPrice, amountOfChange){
    
    let currency = [0.25, 0.1, 0.05, 0.01];
    let sumOfChange = 0;

    for (const i in amountOfChange) {
        sumOfChange += amountOfChange[i] * currency[i];
    }
    // console.log(sumOfChange);

    if (sumOfChange > itemPrice) {
        return true;
    } else {
        return false;
    }
}

console.log(changeEnough(4.25, [25, 20, 5, 0]));
console.log(changeEnough(14.11, [2,100,0,0]));
console.log(changeEnough(0.75, [0,0,20,5]));


/* TASK: Vacations Costs
    
    Let’s create functions that calculate your vacation’s costs:

    1. Define a function called hotelCost().
        - It should ask the user for the number of nights they would like to stay in the hotel.
        - If the user doesn’t answer or if the answer is not a number, ask again.
        - The hotel costs $140 per night. The function should return the total price of the hotel.

    2. Define a function called planeRideCost().
        - It should ask the user for their destination.
        - If the user doesn’t answer or if the answer is not a string, ask again.
        - The function should return a different price depending on the location.
            * “London”: 183$
            * “Paris” : 220$
            * All other destination : 300$

    3. Define a function called rentalCarCost().
        - It should ask the user for the number of days they would like to rent the car.
        - If the user doesn’t answer or if the answer is not a number, ask again.
        - Calculate the cost to rent the car. The car costs $40 everyday.
            * If the user rents a car for more than 10 days, they get a 5% discount.
        - The function should return the total price of the car rental.

    4. Define a function called totalVacationCost() that returns the total cost of the user’s vacation by calling the 3 functions that you created above.
        Example : The car cost: $x, the hotel cost: $y, the plane tickets cost: $z.
        Hint: You have to call the functions hotelCost(), planeRideCost() and rentalCarCost() inside the function totalVacationCost().

    5. Call the function totalVacationCost()

    6. Bonus: Instead of using a prompt inside the 3 first functions, only use a prompt inside the totalVacationCost() function. You need to change the 3 first functions, accordingly.

*/
function hotelCost(){
    
    let nightCost = 140;
    let numOfNights;

    while (true) {
        numOfNights = parseInt(prompt("How many nights would you like to stay?"));
        if (!isNaN(numOfNights)) {
            break;
        }
    }
    return numOfNights * nightCost;
}


function planeRideCost(){
    
    let destinationCost = {london: 183, paris: 220, other: 300};
    let destination;

    while (true) {
        destination = prompt("What is your destination?").toLocaleLowerCase();
        if (!/[^a-z]/.test(destination)) {
            break;
        }
    }

    if (!(destination in destinationCost)) {
        destination = "other";
    }
    
    return destinationCost[destination];
}


function rentalCarCost(){

    let dayCost = 40;
    let numOfDays;

    while (true) {
        numOfDays = parseInt(prompt("How many days would you like to rent?"));
        if (!isNaN(numOfDays)) {
            break;
        }
    }

    if (numOfDays <= 10) {
        return dayCost * numOfDays;
    } else {
        return dayCost * numOfDays * 0.95;
    }
}


function totalVacationCost() {

    let hotel = hotelCost();
    let plane = planeRideCost();
    let car = rentalCarCost()
    let totalCost = hotel + plane + car;
    console.log(`Hotel cost: ${hotel}$, destination cost: ${plane}$ and car rental cost: ${car}$`);
    console.log(`Total cost: ${totalCost}$`);
}

totalVacationCost();