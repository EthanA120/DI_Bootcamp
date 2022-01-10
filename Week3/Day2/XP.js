// Ex1:
console.log('Ex1:');
let favoriteFood = 'Tortilla';
let favoriteMeal = 'lunch';

console.log('I eat ' + favoriteFood + ' at every ' + favoriteMeal);

// Ex2:
let watchedSeries = ["black mirror", "money heist", "the big bang theory"];
let watchedSeriesLength = watchedSeries.length;
let myWatchedSeries = watchedSeries.slice(0, -1).join(", ") + ", and " + watchedSeries[watchedSeries.length - 1];

console.log('Ex2 - Part 1:');
console.log('I watched ' + watchedSeriesLength + ' series: ' + myWatchedSeries);

watchedSeries[watchedSeries.length - 1] = "freinds";
watchedSeries.push("the good doctor");
watchedSeries.splice(0, 1, "breaking bad");

console.log('Ex2 - Part 2:');
console.log(watchedSeries[1][2]);
console.log(watchedSeries);

// Ex3:
console.log('Ex3:');
let cDegree = 20;

console.log (cDegree + "°C is " + (cDegree * 9/5 + 32) + "°F")

// Ex4:
console.log('Ex4:');
let c;
let a = 34;
let b = 21;

console.log(a+b) //first expression
// Prediction: 55 - number + number = sum of numbers
// Actual: 55

a = 2;

console.log(a+b) //second expression
// Prediction: 23 - the last value assigned to 'a' replaced the old value
// Actual: 23

console.log(c)
// Prediction: undefined - declare variable without difine it will give undefined variable
// Actual: undefined

console.log(3 + 4 + '5');
// Prediction: "75" - number + string = string
// Actual: "75"

// Ex5:
console.log('Ex5:');
typeof(15)
console.log(typeof(15))
// Prediction: number
// Actual: number

typeof(5.5)
console.log(typeof(5.5))
// Prediction: number
// Actual: number

typeof(NaN)
console.log(typeof(NaN))
// Prediction: undefined
// Actual: number

console.log(typeof("hello"))
// Prediction: string
// Actual: string

console.log(typeof(true))
// Prediction: boolean
// Actual: boolean

console.log(typeof(1 != 2))
// Prediction: boolean
// Actual: boolean

console.log("hamburger" + "s")
// Prediction: 'hamburgers'
// Actual: 'hamburgers'

console.log("hamburgers" - "s")
// Prediction: NaN
// Actual: NaN

console.log("1" + "3")
// Prediction: '13'
// Actual: '13'

console.log("1" - "3")
// Prediction: -2
// Actual: -2

console.log("johnny" + 5)
// Prediction: 'johnny5'
// Actual: 'johnny5'

console.log("johnny" - 5)
// Prediction: NaN
// Actual: NaN

console.log(99 * "hello")
// Prediction: NaN
// Actual: NaN

console.log(1 != 1)
// Prediction: false
// Actual: false

console.log(1 == "1")
// Prediction: true
// Actual: true

console.log(1 === "1")
// Prediction: false
// Actual: false

// Ex6:
console.log('Ex6:');

console.log(5 + "34")
// Prediction: '534'
// Actual: '534'

console.log(5 - "4")
// Prediction: 1
// Actual: 1

console.log(10 % 5)
// Prediction: 0
// Actual: 0

console.log(5 % 10)
// Prediction: 5
// Actual: 5

console.log("Java" + "Script")
// Prediction: JavaScript
// Actual: JavaScript

console.log(" " + " ")
// Prediction: '  '
// Actual: '  '

console.log(" " + 0)
// Prediction: ' 0'
// Actual: ' 0'

console.log(true + true)
// Prediction: 2
// Actual: 2

console.log(true + false)
// Prediction: 1
// Actual: 1

console.log(false + true)
// Prediction: 1
// Actual: 1

console.log(false - true)
// Prediction: -1
// Actual: -1

console.log(!true)
// Prediction: false
// Actual: false

console.log(3 - 4)
// Prediction: -1
// Actual: -1

console.log("Bob" - "bill")
// Prediction: NaN
// Actual: NaN