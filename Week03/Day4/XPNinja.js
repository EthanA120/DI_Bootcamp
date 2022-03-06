/* TASK: Age difference
    
    Given the years two people were born, find the date when the younger one is exactly half the age of the older.
    Notes: The dates are given in the format YYYY
*/
let year = 2021;
let date1 = 1993;
let age1 = year - date1;
let age2 = year - 0.5*age1;

console.log(age2);

/* TASK: Zip codes
    
    Hint: This exercise has 2 parts. First, do this exercise without Regular Expressions, then do it using Regular Expressions

    1. While working in a Post Office you must have the clients’ zip code in order to send them their letters.
    2. Ask the client for their zip code and console.log “success” or “error” based on the following rules.
        1. Zip codes consists of 5 numbers
        2. Must only contain numbers
        3. Must not contain any whitespace (spaces)
        4. Must not be greater than 5 digits in length
*/
// Part 1:
let zip = prompt("Enter a ZIP code");

if (zip.length == 5 && !isNaN(zip) && zip.indexOf(' ') == -1) {
    console.log("Success");
} else {
    console.log("Error");
}

// Part 2:
if (/^[0-9]{5}$/.test(zip) && !/\D/.test(zip) && !/\s/.test(zip)) {
    console.log("Success");
} else {
    console.log("Error");
}

/* TASK: Secret word
    
    Hint: Use Regular Expressions
    1. Prompt the user for a word and save it to a variable.
    2. Delete all the vowels of the word and console.log the result.
    3. Bonus: Replace the vowels with another character and console.log the result
        a = 1
        e = 2
        i = 3
        o = 4
        u = 5
*/
let aWord = prompt("Enter a word");
let chars = {'a':'1', 'e':'2', 'i':'3', 'o':'4', 'u':'5'};

console.log(aWord.replace(/[aeiou]/g, ""));
console.log(aWord.replace(/[aeiou]/g, m => chars[m]));