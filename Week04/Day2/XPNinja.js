/* TASK: Random Number
    
    1. Get a random number between 1 and 100.
    2. Console.log all even numbers from 0 to the random number.
*/
function randomNumber() {
    
    let randInt = Math.floor(Math.random() * 101);
    let evenNums = [];
    
    for (let i = 0; i < randInt; i++) {
        if (i % 2 == 0) {
            evenNums.push(i);
        }
    }
    return evenNums;
}

console.log(randomNumber());


/* TASK: Capitalized letters
    
    1. Createa function that takes a string as an argument.
    2. Have the function return:
        1. The string but all letters in even indexes should be capitalized.
        2. The string but all letters in odd indexes should be capitalized.

    Note:
        - Index 0 will be considered even.
        - The argument of the function should be a lowercase string with no spaces.

    For example:
        capitalize("abcdef") will return ['AbCdEf', 'aBcDeF']
*/
function capitalize(someString) {
    
    let evenCapital = "";
    let oddCapital = "";

    for (let i = 0; i < someString.length; i++) {
        if (i == 0 || i % 2 == 0) {
            evenCapital += someString[i].toUpperCase();
            oddCapital += someString[i];
        } else {
            evenCapital += someString[i];
            oddCapital += someString[i].toUpperCase();
        }
    }

    return [evenCapital, oddCapital];
}

console.log(capitalize("abcdef"));


/* TASK: Is palindrome?
    
    
    Write a JavaScript function that checks whether a string is a palindrome or not.
    Note A palindrome is a word, phrase or sequence that is spelled the same both backwards and forward, e.g., madam, bob or kayak.
*/
function isPalindrome(someString) {
    
    someString = someString.toLowerCase();

    if (someString == someString.split("").reverse().join("")) {
        return true;
    } else {
        return false;
    }
}

console.log(isPalindrome("Madam"));
console.log(isPalindrome("palindrome"));


/* TASK: Biggest Number
    
    1. Create a function called biggestNumberInArray(arrayNumber) that takes an array as a parameter and returns the biggest number.
        Note : This function should work with any array; 

    Example:
        const array = [-1,0,3,100, 99, 2, 99] ;// should return 100 
        const array2 = ['a', 3, 4, 2]; // should return 4 
        const array3 = []; // should return 0
*/
function biggestNumberInArray(arrayNumber) {
    
    let longest;
    if (arrayNumber.length > 0 && arrayNumber[0] == /^[0-9]/) {
        longest = arrayNumber[0];
    } else {
        longest = 0;
    }

    for (let i = 1; i < arrayNumber.length; i++) {
        if (arrayNumber[i] > longest) {
        longest = arrayNumber[i];
        }
    }

    return longest
}

console.log(biggestNumberInArray([-1,0,3,100, 99, 2, 99]));
console.log(biggestNumberInArray(['a', 3, 4, 2]));
console.log(biggestNumberInArray([]));


/* TASK: Unique Elements
    
    Write a JS function that takes an array and returns a new array with only unique elements.
    Example list=[1,2,3,3,3,3,4,5] newList = [1,2,3,4,5]

*/
function uniqueElements(someArray) {
    
    let uniqueArray = [];

    for (let element of someArray) {
        if (!uniqueArray.includes(element)) {
            uniqueArray.push(element);
        }
    }
    return uniqueArray;
}

console.log(uniqueElements([1,2,3,3,3,3,4,5]));