/* TASK: Select a kind of Music
    
    <select id="genres">
        <option value="rock">Rock</option>
        <option value="blues" selected>Blues</option>
    </select>

    1. Display the value of the selected option.
    2. Add an additional option to the select tag:
        <option value="classic">Classic</option>
    3. The newly added option should be selected by default.
*/
let selectedOption = document.querySelector("option[selected]");
console.log(selectedOption);

let select = document.querySelector("#genres");
let classic = document.createElement("option");
let classicText = classic.appendChild(document.createTextNode("Classic"));

classic.value = "classic";
select.appendChild(classic);

selectedOption.removeAttribute("selected");
classic.setAttribute("selected", "");


/* TASK: Delete colors

    <form>
        <select id="colorSelect">
            <option>Red</option>
            <option>Green</option>
            <option>White</option>
            <option>Black</option>
        </select>
        <input type="button" value="Select and Remove">
    </form>

    Add a click event listener to the <input type="button">.
    When clicked on, it should call a function named removecolor() that removes the selected color from the dropdown list.
*/
function removecolor(buttonClick) {
    let colorSelect = document.querySelector("#colorSelect");
    let options = [...colorSelect.querySelectorAll("option")];
    options.forEach(item => item.setAttribute("id", item.textContent));
    if (options.length > 0) {
        colorSelect.removeChild(document.querySelector(`#${colorSelect.value}`));
    } else {
        console.log("Error: No options left!");
    }
}

let button = document.querySelector("input");
button.addEventListener("click", removecolor);


/* TASK: Create a shopping list
    
    For this exercise, you need to work on your js file.
    The one and only element on your HTML file should be:
        
        <div id="root"></div>

    In your js file:
        1. Create an empty array. For example let shoppingList=[].

        2. Create a form containing : a text input field and an "Addltem" button. Add this form to the DOM.

        3. Type what you need to buy in the text input field,
            then add the new item to the array as soon as you click on the "Addltem" button
            Hint: create a function named addItem().

        4. Add a "ClearAll" button to the DOM, that when clicked on, should call the clearAll () function (see below).

        5. Create a function named clearAl1 () that should clear out all the items in the shopping list.
*/
let shoppingList = [];

function addItem(addItemClick) {
    shoppingList.push(input.value);
    console.log(shoppingList);
    addItemClick.preventDefault();
}

function clearAll(addItemClick) {
    shoppingList = [];
    console.log(shoppingList);
    addItemClick.preventDefault();
}

let root = document.querySelector("#root");
let form = document.createElement("form");
let input = form.appendChild(document.createElement("input"));
let buttonAddItem = form.appendChild(document.createElement("button"));
let buttonClearAll = form.appendChild(document.createElement("button"));

input.setAttribute("placeholder", "Add Item");
buttonAddItem.textContent = "Add Item";
buttonAddItem.addEventListener("click", addItem);

buttonClearAll.textContent = "Clear All";
buttonClearAll.addEventListener("click", clearAll);

root.appendChild(form);