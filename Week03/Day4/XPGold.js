/* TASK: The World Translator
    
    1. Ask the user which language they speak.
    2. Convert the user’s answer to lowercase,
        so that all the user’s inputs will be accepted in the if statement.
        For example “english” or “English” or “ENGlish” ect…”
    3. Create a few conditions :
    4. If the user speaks French : display “Bonjour”
    5. If the user speaks English : display “Hello”
    6. If the user speaks Hebrew : display “Shalom”
    7. If the user doesn’t speak any of these 3 languages: display ‘01110011 01101111 01110010 01110010 01111001’
*/
let userInput = prompt("Enter your language").toLowerCase();

if (userInput == "hebrew") {
    console.log("Shalom");
} else if(userInput == "french") {
    console.log("Bonjour");
} else if(userInput == "english") {
    console.log("Hello");
} else {
    console.log("01110011 01101111 01110010 01110010 01111001");
}

/* TASK: The Grade Assigner
    
    1. Ask the user for their grade.
    2. If the grade is bigger than 90, console.log "A"
    3. If the grade is between 80 and 90 (included), console. log "B"
    4. If the grade is between 70(included) and 80 (included), console.log "C"
    5. If the grade is lower than 70, console.log "D"
*/
let grade = parseInt(prompt("Enter your grade:"));

if (90 < grade) {
    console.log("A");

} else if(80 < grade && grade <= 90) {
    console.log("B");

} else if(70 <= grade && grade <= 80) {
    console.log("C");

} else if(grade < 70) {
    console.log("D");
}

/* TASK: Verbing
    
    1. Prompt the user for a string. It must be a verb.
    2. If the length of the string is at least 3 and the string doesn't end with "ing", add 'ing' to the end of the string
    3. If the length of the string is at least 3 and the string ends with "ing" add "ly" to it's end.
    4. If the length of the string is less than 3, leave it unchanged.
    
    Example:
        The string is: "swim" , your program should console . log "swimming"
        The string is: "swimming", your program should console. log "swimmingly"
        The string is: "go" your program should console . log "go"
*/
let verb = prompt("Enter a verb:");

if (verb.length >= 3 && !verb.endsWith("ing")) {
    verb += "ing";
} else if (verb.length >= 3 && verb.endsWith("ing")) {
    verb += "ly";
}

console.log(verb);