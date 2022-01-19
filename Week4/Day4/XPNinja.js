/* TASK: Hanging Game
    
    Create the “Hangman” game. Your game will run in the console.
    You need to guess a hidden word. Each letter you guess will appear in the console. You have 10 chances before you lose the game. 

    1. Prompt player 1 for a word. The word must have a minimum of 8 letters.
        Present the word in the console with stars (***s****).

    2. At this point continuously prompt player2 for a letter

    3. If the letter is in the word chosen by player 1,
        display the word in stars again but with the correct letter (*****t **).

    4. If the letter appears in the word multiple times,
        make sure it is seen in all the correct places when showing the stars with the correct guesses (***t**t*).

    5. If player 2 guesses incorrectly 10 times display a message in the console saying YOU LOSE

    6. Show a list of all the guesses after each turn.

        In your code prevent player 2 from guessing the same letter twice.
    7. If player 1 wins, display a message that says cONGRATS YOU WIN.

*/
function hangingGame() {
    let user1Word = [];
    let lettersGuessed = [];
    while (user1Word.length < 8) {
        user1Word = prompt("Enter a word with at least 8 letters").toLocaleUpperCase().split('');
    }
    let asterisked = "*".repeat(user1Word.length).split('');

    let counter = 0;
    while (asterisked.includes("*") && counter <= 10) {
        let user2Letter = prompt("Enter a letter").toLocaleUpperCase();
        console.log("Enter a letter:", user2Letter);

        if (user1Word.includes(user2Letter) && !lettersGuessed.includes(user2Letter)) {
            while (user1Word.includes(user2Letter)) {
                let letterIndex = user1Word.indexOf(user2Letter);
                asterisked.splice(letterIndex, 1, user2Letter.toLocaleUpperCase());
                user1Word.splice(letterIndex, 1, "*");
            }
            lettersGuessed.push(user2Letter);

        } else if (lettersGuessed.includes(user2Letter)) {

        } else {
            console.log("Wrong");
            lettersGuessed.push(user2Letter);
            counter++;
        }

        console.log(asterisked.join(""));
        console.log("Already guessed:", lettersGuessed);
    }


    if (counter > 10) {
        alert("YOU LOSE!");
    } else {
        alert("CONGRATS YOU WIN!");
    }
}

hangingGame()