/* TASK:  Bubble Sort
    
    const numbers = [5,0,9,1,7,4,2,6,3,8];

    1. Using the .toString () method convert the array to a string.
    2. Using the .join() method convert the array to a string. Try passing different values into the join.
        Eg join("+"), join(" "), join(")
    3. Bonus: To do this Bonus look up how to work with nested for loops Sort the numbers array in descending order, do so using for loops (Not using built-in sort methods).
    The output should be: [9,8,7,6,5,4,3,2,1,0]
        Hint: The algorithm is called “Bubble Sort”
            - Use a temporary variable to swap values in the array.
            - Use 2 “nested” for loops (Nested means one inside the other).
            - Add comments and console.log the result for each step, this will help you understand.
                Requirement: Don’t copy paste solutions from Google
*/
const numbers = [5,0,9,1,7,4,2,6,3,8];

let toStringNums = numbers.toString();
console.log(toStringNums);

let joinNums = numbers.join(", ");
console.log(joinNums);

let numbersCopy = numbers.slice();
let sortedNumbers = [];

for (let i = 0; i < numbers.length; i++) {
    var highest = [numbersCopy[0], 0];
    for (let j = 1; j < numbersCopy.length; j++) {
        if (highest[0] < numbersCopy[j]) {
            highest[0] = numbersCopy[j];
            highest[1] = j;
        }
    }
    sortedNumbers[i] = highest[0];
    numbersCopy.splice(highest[1],1);
}
console.log(sortedNumbers);