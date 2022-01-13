/* TASK: Checking the BMI

    - You must use functions to complete this exercise, to do so take a look at tomorrow's lesson.
    1. Create two objects, each object should hold a person's details. Here are the details:
        1. FullName
        2. Mass
        3. Height
    
    2. Each object should also have a key which value is a function (ie. A method),
        that calculates the Body Mass Index (BMI) of each person

    3. Outside of the objects, create a JS function that compares the BMI of both objects.

    4. Display the name of the person who has the largest BMI.
*/
let hanz = {fullName: "Hanz", mass: 65, height: 1.75, bmi: function(mass, height){return mass / height ** 2;}};
let ganz = {fullName: "Ganz", mass: 69, height: 1.73, bmi: function(mass, height){return mass / height ** 2;}};

function bmiCompare(a, b){
    if (a.bmi(a.mass, a.height) > b.bmi(b.mass, b.height)) {
        return a.fullName;
    } else {
        return b.fullName;
    }
}

comparement = bmiCompare(hanz, ganz);
console.log(comparement);


/* TASK: Grade Average
    
    Hint:
    - This Exercise is trickier then the others. You have to think about its structure before you start coding.
    - You must use functions to complete this exercise, to do so take a look at tomorrow’s lesson.
    
    In this exercise we will be creating a function which takes an array of grades as an argument and will console.log the average.

    1. Createa function called findAvg (grades List) that takes an argument called gradesList.
    2. Your function must calculate and console.log the average.
    3. If the average is above 65 let the user know they passed
    4. If the average is below 65 let the user know they failed and must repeat the course.
        - Bonus Try and split parts 1,2 and 3,4 of this exercise to two separate functions.
        - Hint One function must call the other.
*/
function checkAvg(averageGrade){
    if (averageGrade > 65) {
        console.log("Congratulations! you have passed the course");
    } else {
        console.log("You have failed, unfortunately you must repeat the course");
    }
}

function findAvg(gradesList){
    let sumOfGrades = 0;
    for (let grade of gradesList) {
        sumOfGrades += grade;
    }

    let averageGrade = sumOfGrades / gradesList.length;
    console.log(averageGrade);
    checkAvg(averageGrade);
}

let gradesList = [23, 57, 95, 80, 79, 92, 100, 64];
findAvg(gradesList);