/* TASK: Words in the stars
    
    1. Prompt the user for several words (separated by commas).
    2. Put the words into an array.
    3. Console.log the words one per line, in a rectangular frame as seen below.
    4. Check out the Hints and Requirements below.

    For example, if the user gives you:
    Hello, World, in, a, frame
    you will transform it to : ["Hello", "World", "in", "a", "frame"];

    Hint: The number of stars that wraps the sentence, must depend on the length of the longest word.

    Requirements: To do this challenge you only need Javascript(No HTML and no CSS)

*/
function wordsInTheStars() {
    
    let userWords = "Hello, World, in, a, frame".replace(/\s/g, ""); // FIXME: prompt("Enter words seperated with ','").replace(" ", "");
    let userWordsArray = userWords.split(",");

    // Find out what is the length of the longest string in the array
    let maxLength = 0;
    for (let i = 0; i < userWordsArray.length; i++) {
        if (userWordsArray[i].length > maxLength) {
        maxLength = userWordsArray[i].length;
        }
    }

    let framedWords = ["*".repeat(maxLength + 4)];
    for (let word of userWordsArray) {
        framedWords.push(`* ${word + " ".repeat(maxLength - word.length)} *`);
    }
    framedWords.push(framedWords[0]);
    
    console.log(framedWords.join("\n"));
}

wordsInTheStars()