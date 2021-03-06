/* TASK: 99 Bottles of Beer

    Have you heard the infamous song “99 Bottles of Beer?”
    In this exercise you need to console.log the lyrics to the song 99 Bottles of Beer.

    1. Prompt the user for a number to begin counting down bottles.

    2. In the song everytime a bottle falls we subtract the bottles by 1
        What your code should do is:
            - instead of subtracting by 1, everytime a bottle drops the subtracted number should go up by 1
            - For example the first time a bottle drops we subtract by 1, the second time we subtract by 2 and so on.

    3. The song should end with "O bottle of beer on the wall" or "no bottle of beer on the wall".

    4. Note: Make sure you get the grammar correct.
        - For 1 bottle, you pass "it" around.
        - For more than one bottle, you pass "them" around.
*/
function bottleFall(number, substract) {
    number = number - substract;
    return number;
}

let userNum = parseInt(prompt("Enter an amount of bottles"));

for (let i = 1; 0 < userNum; i++) {
    console.log(`${userNum} bottles of beer on the wall`);
    console.log(`${userNum} bottles of beer`);
    
    if (userNum < i) {
        i = userNum;
    }

    if (i == 1) {
        console.log(`Take ${i} down, pass it around`);
    } else {
        console.log(`Take ${i} down, pass them around`);
    }

    userNum = bottleFall(userNum, i);
    console.log(`${userNum} bottles of beer on the wall`);
    console.log(" ");
}