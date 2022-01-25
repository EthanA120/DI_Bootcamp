/* TASK: Change the article
    
    1. Using a DOM property, retrieve the h1 and console.log it.
    2. Using DOM methods, remove the last paragraph in the <article> tag.
    3. Add a event listener which will change the background color of the h2 to red, when it's clicked on.
    4. Add an event listener which will hide the h3 when it's clicked on (use the display:none property).
    5. Add a <button> to the HTML file, that when clicked on, should make the text of all the paragraphs, bold.
    6. BONUS: When you hover on the hl, set the font size to a random pixel size between O to 100.(Check out this documentation)
    7. BONUS: When you hover on the 2nd paragraph, it should fade out (Check out "fade css animation" on Google)
*/
/**@type {HTMLElement}*/ let h1 = document.querySelector("article h1");
console.log(h1);

document.querySelector("article p:last-child").remove();

let h2 = document.querySelector("article h2");
h2.addEventListener("click", (h2Click) => h2Click.target.style.background = "red");

let h3 = document.querySelector("article h3");
h3.addEventListener("click", (h3Click) => h3Click.target.style.display = "none");

let article = document.querySelector("article");
let button = article.appendChild(document.createElement("button"));
button.textContent = "Make Paragraphs Bold";
button.addEventListener("click", () => document.querySelectorAll("article p").forEach((item) => item.style.fontWeight = "bold"));

h1.addEventListener("mouseover", (h1Click) => h1Click.target.style.fontSize = Math.floor(Math.random() * 100).toString() + "px");


function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

let p2nd = document.querySelector("article p:first-of-type + p");
p2nd.addEventListener("mouseover", (p2ndClick) => {
    let p2ndKeyframes = new KeyframeEffect(
        p2ndClick.target,
        [
          { opacity: '1' },
          { opacity: '0' }
        ],
        { duration: 2000 }
      );

      let p2ndAnimation = new Animation(p2ndKeyframes, document.timeline);
      p2ndAnimation.play();
});


/* TASK: Work with forms
    
    1. Retrieve the form and console.log it.
    2. Retrieve the inputs by their id and console.log them.
    3. Retrieve the inputs by their name attribute and console.log them.
    4. When the user submits the form (ie. submit event listener)
        - get the values of the input tags,
        - make sure that they are not empty,
        - create an li per input value,
        - then append them to a the <ul class="usersAnswer"> </ul>, below the form.

    The output should be:
    <ul class="usersAnswer" style="margin-bottom: 50px;">
        <li>first name of the user</li>
        <li>last name of the user</li>
    </ul>
*/
let form = document.querySelector("form");
console.log(form);

let inputById = [];
inputById.push(document.getElementById("fname"));
inputById.push(document.getElementById("lname"));
console.log(inputById[0], inputById[1]);

let fnameByName = document.getElementsByName("fname");
let lnameByName = document.getElementsByName("lname");
console.log(fnameByName[0], lnameByName[0]);

let ul = document.querySelector("form + ul");
let li = [];
inputById[0].required = true;
inputById[1].required = true;
form.addEventListener("submit", (formSubmit) => {
    for (let i = 0; i < 2; i++) {
        if (li.length < 2) {
            li[i] = ul.appendChild(document.createElement("li"));
            li[i].appendChild(document.createTextNode(inputById[i].value));
        } else {
            li[i].textContent = inputById[i].value;
        }
    }
    formSubmit.preventDefault();
});


/* TASK: Transform the sentence
    
    In the JS file:
    1. Create a global variable named allBoldItems.
    
    2. Create a function called getBold_items () that takes no parameter.
        This function should collect all the bold items inside the paragraph and assign them to the allBoldItems variable.
        
    3. Create a function called highlight() that changes the color of all the bold text to blue.
    
    4. Create a function called return_normal ) that changes the color of all the bold text back to black.
    
    5. Call the function highlight () onmouseover (ie. when the mouse pointer is moved onto the paragraph),
        and the function return_normal () onmouseout (ie. when the mouse pointer is moved out of the paragraph).
        Look at this example
*/
let allBoldItems;

function getBold_items() {
    allBoldItems = document.querySelectorAll("strong");
}
getBold_items();

function highlight() {
    for (const item of allBoldItems) {
        item.style.color = "blue";
    }
}

function return_normal() {
    for (const item of allBoldItems) {
        item.style.color = "black";
    }
}

let p = document.querySelector("body > p");
p.addEventListener("mouseover", highlight);
p.addEventListener("mouseout", return_normal);


/* TASK: Volume of a sphere
    
    Write a JavaScript program to calculate the volume of a sphere.
*/
let Ex4 = document.getElementById("Ex4");
let formEx4 = document.querySelector("#Ex4 form");

let radius = document.getElementById("radius");
radius.required = true;
let volume = document.getElementById("volume");
volume.disabled = true;

formEx4.addEventListener("submit", (formSubmit) => {
    volume.value = 4/3*Math.PI*radius.value**3;
    volume.style.color = "black";
    formSubmit.preventDefault();
});