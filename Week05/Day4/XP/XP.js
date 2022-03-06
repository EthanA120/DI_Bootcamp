/* TASK: Move the box
    
    Move the box from left to right
    Tip: use setInterval
*/
let buttonMyMove = document.querySelector("p > button");
let animate = document.getElementById("animate");
let XYLocation = 0;

// buttonMyMove.addEventListener("click", MyMove);

function myMove() {
    let x = setInterval(() => {
        XYLocation += 1;
        animate.style.top = XYLocation + "px";
        animate.style.left = XYLocation + "px";

        if (XYLocation >= 350) {
            clearInterval(x);
            XYLocation = 0;
        }
    }, 1);
}


/* TASK: Drag & Drop
    
    Tip : Check out this video on drag and drop: https://www.youtube.com/watch?v=C22hQKE_32c

    Create a draggable square/box element in your HTML file.
    In your javascript file add the functionality which will allow you to drag the square/box and drop it into a larger box.
*/
let fill = document.querySelector('.fill');
let empties = document.querySelectorAll('.empty');

let narrow = document.getElementById('Narrow');
let wide = document.getElementById('Wide');
let currentXRelPos;

// Fill listeners
fill.addEventListener('dragstart', dragStart);
fill.addEventListener('dragend', dragEnd);

// Loop through empty boxes and add listeners
for (let empty of empties) {
    empty.addEventListener('dragover', dragOver);
    empty.addEventListener('dragenter', dragEnter);
    empty.addEventListener('dragleave', dragLeave);
    empty.addEventListener('drop', dragDrop);
}

// Drag Functions
function dragStart(e) {
    e.target.className += ' hold';
    setTimeout(() => (e.target.className = 'invisible'), 0);
}

function dragEnd(e) {
    e.target.className = 'fill';
}

function dragOver(e) {
    currentXRelPos = e.pageX - e.target.offsetLeft;
    if (e.currentTarget == wide && currentXRelPos > (900-145)) {
        currentXRelPos = (900-145);
    } else if (e.currentTarget == narrow && currentXRelPos > (150-145)) {
        currentXRelPos = (150-145);
    } else if (currentXRelPos < 5) {
        currentXRelPos = 5;
    }
    console.log(currentXRelPos);
    e.preventDefault();
}

function dragEnter(e) {
    e.preventDefault();
    e.currentTarget.className += ' hovered';
}

function dragLeave(e) {
    e.currentTarget.className = 'empty';
}

function dragDrop(e) {
    e.currentTarget.className = 'empty';
    fill.style.left = currentXRelPos + "px";
    e.currentTarget.append(fill);
}