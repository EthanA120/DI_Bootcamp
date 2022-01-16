/* TASK: is_Blank
    
    Write a program to check whether a string is blank or not.

    console.log(isBlank('')); --> true
    console.log(isBlank('abc')); --> false
*/
function isBlank(someString) {
    if (someString.length == 0) {
        return true
    } else {
        return false
    }
}

console.log(isBlank(''));
console.log(isBlank('abc'));


/* TASK: Abbrev_name
    
    Write a JavaScript function to convert a string into an abbreviated form.

    console.log(abbrevName("Robin Singh")); --> "Robin S."
*/
function abbrevName(fullName) {
    
    let fullNameArray = fullName.split(" ");
    return `${fullNameArray[0]} ${fullNameArray[1][0]}.`;
}

console.log(abbrevName("Robin Singh"));


/* TASK: SwapCase
    
    Write a JavaScript function which takes a string as an argument and swaps the case of each character.
    For example :
        if you input 'The Quick Brown Fox' 
        the output should be 'tHE qUICK bROWN fOX'.

*/
function swapCase(someString) {
    
    let swappedString = "";
    
    for (let char of someString) {
        if (char == char.toUpperCase()) {
            swappedString += char.toLowerCase();
    } else if (char == char.toLowerCase()) {
            swappedString += char.toUpperCase();
        }
    }
    
    return swappedString;
}

console.log(swapCase('The Quick Brown Fox'));


/* TASK: Omnipresent value
    
    1. Create a function that determines whether an argument is omnipresent for a given array.
        A value is omnipresent if it exists in every subarray inside the main array.

    To illustrate:
        [[3, 4], [8, 3, 2], [3], [9, 3], [5, 3], [4, 3]]
        // 3 exists in every element inside this array, so is omnipresent.

    Examples:
        isOmnipresent([[1, 1], [1, 3], [5, 1], [6, 1]], 1) ➞ true
        isOmnipresent([[1, 1], [1, 3], [5, 1], [6, 1]], 6) ➞ false
*/
function isOmnipresent(someArray, toCheck) {
    
    let checkArray = [];
    for (let subarray of someArray) {
        if (subarray.includes(toCheck)) {
            checkArray.push(true);
        } else {
            checkArray.push(false);
        }
    }
    
    let checkIfTrue = checkArray.every(function(a){return a == true});
    console.log(checkIfTrue);
}

isOmnipresent([[1, 1], [1, 3], [5, 1], [6, 1]], 1);
isOmnipresent([[1, 1], [1, 3], [5, 1], [6, 1]], 6);