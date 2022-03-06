/* TASK: Play a guessing game
    
Explanation of the game: the point of the game is to guess the number that the computer has in “mind”.

PART: First Part:
    1. Create a JS file and link it to the index.html file.

    2. Take a look at your html file, you should have a button with an “onclick” event.
        This event is equal to the function playTheGame().
        It means that when you will click on the button, the function playTheGame() will be called.
        We will learn more about events next week ;)

    Now let’s create the function:
    3. In the JS file, create a function called playTheGame() that takes no parameter.
        1. In the function, start by asking the user if they would like to play the game (Hint: use the built-in confirm() function).
            1. If the answer is false, alert “No problem, Goodbye”.
            2. If his answer is true, follow these steps:
                1. Ask the user to enter a number between 0 and 10 (Hint: use the built-in prompt() function).
                    You then have to check the validity of the user’s number :

                    - If the user didn’t enter a number (ie. if he entered another data type) alert “Sorry Not a number, Goodbye”.
                    - If the user didn’t enter a number between 0 and 10 alert “Sorry it’s not a good number, Goodbye”.
                    - Else (ie. he entered a number between 0 and 10), create a variable named computerNumber where the value is a random number between 0 and 10 (Hint: Use the built-in Math.random() function).
                        Make sure that the number is rounded.

PART: Second Part:
    1. Outside of the playThe Game() function, create a new function named test(userNumber,computerNumber) that takes 2 parameters: userNumber and computerNumber
    2. The point of this function is to check if the userNumber is the same as the computerNumber
        1. If userNumber is equal to computerNumber, alert "WINNER" and stop the game.
        2. If userNumber is bigger than computerNumber, alert "Your number is bigger then the computer's, guess again"
            Hint: use the built-in prompt () function to ask the user for a new number.
        3. If userNumber is lower than computerNumber, alert "Your number is smaller then the computer's, guess again"
            Hint: use the built-in prompt () function to ask the user for a new number.
        4. If the user guessed more than 3 times, alert "out of chances" and exit the function.

PART: Bonus
    In the First Part, instead of stopping the process if the user didn’t enter a valid number.
    Continue asking for a number until the user enters a valid number.

*/
function test(userNumber,computerNumber) {
    
    if (userNumber == computerNumber) {
        alert("WINNER!");
        console.log("WINNER!");
        return false;

    } else if (computerNumber < userNumber) {
        alert("Your number is bigger then the computer's, guess again");
        console.log("Your number is bigger than the computer's, guess again");
        return true;

    } else {
        alert("Your number is smaller then the computer's, guess again");
        console.log("Your number is smaller than the computer's, guess again");
        return true;
        
    }
}

function validNumber(userNumber) {
    if (isNaN(userNumber)) {
        alert("Sorry Not a number, Goodbye");
        console.log("Sorry Not a number, Goodbye");
        return true;
        
    } else if (userNumber != /[0-10]/ && (userNumber < 0 || userNumber > 10)) {
        alert("Sorry it's not a good number, Goodbye");
        console.log("Sorry it's not a good number, Goodbye");
        return true;

    } else {
        let computerNumber = Math.floor(Math.random() * 2);
        console.log("Computer Number:", computerNumber);
        return test(userNumber, computerNumber);
    }
}

function playTheGame() {
    let userConfirm = confirm("Would you like to play the game?");
    let flag = true;
    let counter = 0;

    if (userConfirm == true) {
        while (flag) {            
            let userNumber = parseInt(prompt("Enter a number from 0 to 10"));
            console.log("Enter a number from 0 to 10");
            counter++;
            flag = validNumber(userNumber);
            
            if (counter > 1 && flag == true) {
                alert("Out of chances");
                console.log("Out of chances");
                flag = false;

            } else {
                console.log("counter:", counter);
            }
        }

    } else {
        alert("No problem, Goodbye");
    }
}