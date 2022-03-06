/* TASK: Todo list
    
    In the js file, you must add the following functionalities:
        1. Create an empty array let listTasks = [];

        2. Create a function called addTask(). As soon as the user clicks on the button:
        - check that the input is not empty,
        - then add it to the array (ie. add the text of the task)
        - then add it to the DOM, below the form (in the <div class="listTasks"></div> )
        - Each new task added should have (starting from left to right - check out the image at the top of the page)
            - a "X" button. Use font awesome for the "X" button.
            - an input type="checkbox". The label of the input is the task added by the user.

        3. BONUS I (not mandatory):
            1. Change the variable listTasks to an array of task objects.
            2. Each new task added to the array should have the properties:
                task_ id, text and done (a boolean false by default).
            3. Every new task object should have a task_id, starting from 0,
                and a data-task-id attribute, which value is the same as the task_ id.
                Check out data-" attributes here: https://www.w3schools.com/tags/att_data-.asp
            4. Create a function named doneTask(), that as soon as the user clicks on the "checkbox" input,
                the done property should change from false to true in the object,
                and from black to crossed out red in the DOM.

        4. BONUS Il (not mandatory):
            Create a function named deleteTask (),
            that as soon as the user clicks on the "X" button,
            delete that specific task from the array listTasks.
*/
let listTasks = {};
let inputAddItem = document.querySelector("input[type=text]");
let buttonAddItem = document.querySelector("input[type=button]");
let divListTasks = document.querySelector(".listTasks");
let labelClear = document.querySelector("#Clear");

let counter = 0;
function addTask() {
    if (inputAddItem.value.length > 0) {
        let toDoItem = document.createElement("div");
        let buttonRemove = document.createElement("i");
        let label = document.createElement("label");
        let checkbox = document.createElement("input");
        let span = document.createElement("span");
        let classCounter = "A" + counter;

        toDoItem.id = classCounter;
        toDoItem.className = classCounter + " toDoItem";
        buttonRemove.className = classCounter + " fas fa-times";
        label.setAttribute("for", classCounter);
        checkbox.type = "checkbox";
        checkbox.className = classCounter;
        span.textContent = inputAddItem.value;
        span.className = classCounter;

        toDoItem.appendChild(buttonRemove);
        toDoItem.appendChild(label);
        label.appendChild(checkbox);
        label.appendChild(span);
        
        divListTasks.insertBefore(toDoItem, labelClear);
        divListTasks.insertBefore(document.createElement("hr"), labelClear);

        listTasks[toDoItem.id] = toDoItem;
        counter++;
        buttonRemove.addEventListener("click", deleteTask);
        checkbox.addEventListener("click", doneTask);
    }
}

function doneTask(e) {
    if (!listTasks[e.target.className].children[1].className.includes("done")) {
        listTasks[e.target.className].children[1].className += "done";
    } else {
        listTasks[e.target.className].children[1].classList.remove("done");
    }
}

function deleteTask(e) {
    listTasks[e.target.classList[0]].nextElementSibling.remove();
    listTasks[e.target.classList[0]].remove();
    delete listTasks[e.target.classList[0]];
}

function clearAll() {
    for (const item in listTasks) {
        listTasks[item].nextElementSibling.remove();
        listTasks[item].remove();
    }

    listTasks = {};
    counter = 0;
}

buttonAddItem.addEventListener("click", addTask);
labelClear.addEventListener("click", clearAll);