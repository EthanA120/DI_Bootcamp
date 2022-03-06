/* TASK: Show only the letters
    
    

    1. Create an input type text that takes/shows only letters.
    (ie. numbers and special characters won’t be accepted)

    2. Hint: use one of the following events to remove any character that is not a letter
        - keyup event
        - or keypress event
        - or keydown event
        - or input event

    3. Hint: Check out keycodes in Javascript or Regular Expressions
*/
let input = document.querySelector("input");

function onlyLetters(e) {
    if (!/[a-z]/.test(e.data)) {
        console.log(input.value[input.value.length - 1]);
        input.value = input.value.slice(0, input.value.length - 1);
    }
}

input.addEventListener("input", onlyLetters);