/* TASK: Change the navbar

    <div id="navBar">
        <ul>
            <li><a href="#">Profile</a></li>
            <li><a href="#">Home</a></li>
            <li><a href="#">My Friends</a></li>
            <li><a href="#">Messenger</a></li>
            <li><a href="#">My Pics</a></li>
        </ul>
    </div>

    1. In the <div> above, change the value of the id attribute from navBar to socialNetworkNavigation,
        using the setAttribute method.

    2. We are going to add a new <li> to the <ul>.
        1. First, create a new <li> tag (use the createElement method).
        2. Create a new text node with "Logout" as its specified text.
        3. Append the text node to the newly created list node (li).
        4. Finally, append this updated list node to the unordered list above, using the appendChild method.

    3. Bonus:
        - Use the firstElement Child and the lastElementChild properties to retrieve the first
        and last 1i elements from their parent element (ul). Display the text of each link.
        (Hint: use the textContent property).
*/
let Ex1 = document.querySelector("#Ex1");
let divNewID = Ex1.querySelector("div").setAttribute("id", "socialNetworkNavigation");
let ulSelector = Ex1.querySelector("ul");
let newLI = document.createElement("li");
let newA = document.createElement("a");

aText = document.createTextNode("Logout");
newA.setAttribute("href", "#");
newA.appendChild(aText);
newLI.appendChild(newA);
ulSelector.appendChild(newLI);

let ulFirstChild = ulSelector.firstElementChild.textContent;
let ulLastChild = ulSelector.lastElementChild.textContent;
console.log(ulFirstChild);
console.log(ulLastChild);


/* TASK: Users

    <html>
    <body>
      <div id="container">Users:</div>
      <ul class="list">
        <li>John</li>
        <li>Pete</li>
      </ul>
      <ul class="list">
        <li>David</li>
        <li>Sarah</li>
        <li>Dan</li>
      </ul>
    </body>
    </html>

    1. In the HTML above change the name "Pete" to "Richard".
    2. Change each first name of the two <ul> 's to your name.
    3. At the end of each <ul> add a <li> that says "Hey students".
    4. Delete the name Sarah from the second <ul>.
    5. Bonus:
        - Add a class called student_list to both of the <ul>'s.
        - Add the classes university and attendance to the first <ul>.
*/
let Ex2 = document.querySelector("#Ex2");
let peteToRichard = Ex2.querySelector("ul").lastElementChild;
peteToRichard.textContent = "Richard";

let ul = Ex2.querySelectorAll("ul");
ul.forEach((item) => item.firstElementChild.textContent = "Ethan");

ul.forEach((item) => {
    let newli = document.createElement("li");
    newli.textContent = "Hey students";
    item.appendChild(newli);
});

ul[1].removeChild(ul[1].children[1]);

ul.forEach((item) => item.setAttribute("class", "student_list"));
ul[0].classList.add("university", "attendance");


/* TASK: Users and style
    
    <html>
    <body>
      <div>Users:</div>
      <ul>
        <li>John</li>
        <li>Pete</li>
      </ul>
    </body>
    </html>

    For the following exercise use the HTML presented above

    1. Add a "light blue" background color and some padding to the <div>.
    2. Do not display the first name (John) in the list.
    3. Add a border to the second name (Pete).
    4. Change the font size of the whole body.
    5. Bonus: If the background color of the div is "light blue", alert "Hello x and y"
        (x and y are the users in the div).
*/
let Ex3 = document.querySelector("#Ex3");
let divStyle = Ex3.querySelector("div").style;
divStyle.backgroundColor = "lightblue";
divStyle.padding = "5px";

let john = Ex3.querySelector("ul li:first-child");
john.style.display = "none";

let pete = Ex3.querySelector("ul li:last-child");
pete.style.border = "1px solid black";

let body = document.body;
body.style.fontSize = "15px";

let nameList = [...Ex3.querySelectorAll("ul li")].map(item => item.textContent);
if (divStyle.backgroundColor == "lightblue") {
  alert(`Hello ${nameList.slice(0, nameList.length-1).join(", ")} and ${nameList[nameList.length-1]}`)
}