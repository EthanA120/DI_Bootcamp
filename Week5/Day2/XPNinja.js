/* TASK: Calculate the tip
    
    In this exercise you will calculate how much your tip would be after eating in a restaurant.
    
    PART: 1st

    Create a js file name main.js and create a function called calculateTip() that takes no parameter.
    
        1. Create a variable called billAmount that fetches the value of the input,
            which id is billAmt (check the HTML file) -> It's the amount of the bil.

        2. Create a variable called serviceQuality that fetches the value of the input,
            which id is serviceQual (check the HTML ile) -> It's the quality of the service.

        3. Createa variable called numberOfPeople that fetches the value of the input,
            which id is numOfPeople (check the HTML file) -> It's the number of people sitting at the table.

        4. Create a condition If serviceQuality is equal to zero,
            or billAmount is empty, alert the user to enter these values.

        5. Create another condition after the first one:
            If the input numberofPeople is empty or is smaller than 1,
            set a default value of 1 to numberofFPeople and make sure that the tag which id is each,
            is not displayed (check the end of the HTML file).

        6. Create a variable named total:
            the value should be (billAmount * serviceQuality) / numberofPeople (the outcome is the average tip each person should pay)

        7. Use the toFixed method to round total to two decimal points.

        8. Add the CSS property "display:block" to the tag which id is totalTip.

        9. Display the variable total in the tag which id is tip.


    PART: 2nd

    1. To avoid displaying the total if the function calculateTip() is not called,
        add the CSS property “display: none” to the tag which id is totalTip.

    2. Call the function calculateTip() when the tag which id is calculate is clicked.
        Hint: use the method onclick.
*/
let totalTip = document.querySelector("#totalTip");
totalTip.style.display = "none";

function calculateTip() {
    let billAmount = document.querySelector("#billamt").value;
    let serviceQuality = document.querySelector("#serviceQual").value;
    let numberOfPeople = document.querySelector("#peopleamt").value;


    if (serviceQuality == 0 || billAmount == "") {
        alert("Error: Please enter Bill Amount and tell how was the service!");
    }

    if (numberOfPeople == "" || numberOfPeople < 1) {
        numberOfPeople = "1";
    }

    let each = document.querySelector("#each");
    numberOfPeople > 1 ? each.style.display = "inline" : each.style.display = "none";

    let total = (billAmount * serviceQuality / numberOfPeople).toFixed("2");

    totalTip.style.display = "block";

    let tip = document.querySelector("#tip");
    tip.textContent = total;
}


let calculate = document.querySelector("#calculate");
calculate.addEventListener("click", calculateTip);


/* TASK: Validate the email
    
    We will create a form that ask the user for their email.
    Then, using a function we will check the validity of the user’s input.

    1. Add an input that has a type="email" to your form.

    2. Write your own javascript validation function to check if the entered value is a valid email address.
        The address should contain some valid characters,and the @ sign,
        more characters then a . (period) and some more characters.

    3. On "submit", the validation function should run and validate the email address.
        Try to do this exercise twice: with and without regex.
*/
let Ex2 = document.createElement("form");
let emailInput = Ex2.appendChild(document.createElement("input"));
let submitInput = Ex2.appendChild(document.createElement("input"));

function validEmail() {
    let emailValue = emailInput.value;
    let flag = true;

    if (emailValue.length >= 5
        && emailValue.includes("@") && emailValue.split("@").length - 1 == 1
        && emailValue.includes(".") && emailValue.split(".").length - 1 == 1
        && emailValue.indexOf("@") < emailValue.indexOf(".")) {
        alert("Email is valid due to regular check");
        flag = false;
    }
    try {
        if (emailValue.match(/@/g).length == 1 && emailValue.match(/\./g).length == 1
            && emailValue.indexOf("@") < emailValue.indexOf(".")) {
            alert("Email is valid due to regex check");
            flag = false;
        }
    } catch (error) {
        console.log("No match for regex, array is empty!");
    }

    if (flag) {
        alert("Email is not valid");
    }
}


Ex2.setAttribute("id", "Ex2");
Ex2.style.marginTop = "50px";

emailInput.type = "email";
emailInput.placeholder = "Email";

submitInput.type = "button";
submitInput.value = "Confirm";
submitInput.addEventListener("click", validEmail)

document.body.appendChild(Ex2);


/* TASK: Get the user’s geolocation coordinates
    
    Hint/tip

    - Use HTML5 and Javascript for this exercise.
    - Use everything we learned in class, and use all the resources linked in the course.
    - This exercise is a bit tricky, search Google how to work with HTML5 and the navigator’s geolocation.
    - Create a button

    For example, after the user clicks on the button, the output of your code should be as seen below:
        Latitude: 32.179346699999996
        Longitude: 34.871555

*/
let Ex3 = document.createElement("button");
Ex3.textContent = "Click Me!";
Ex3.style.marginTop = "50px";
document.body.appendChild(Ex3);
Ex3.addEventListener("click", Ex3Click => {
    alert(`Latitude: ${Ex3Click.clientX}\nLongitude: ${Ex3Click.clientY}`);
})
