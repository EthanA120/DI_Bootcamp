/* TASK: Coloring Game
    
    You can see the working project here: https://devtlv.github.io/coloring_squares/

    Project Brief:
        Your task is to build a coloring game similar to the working project above.
        You will need to use HTML, CSS and JS to accomplish this task.
        
    A few things to think about:
        HTML, CSS:
            - How will you make the grid of colors?
            - How will you make the grid of blank squares?
            - Hint… GRID
    
        JS:
            - How does a user choose a color?
            - How does drawing work? How can you tell when the user is clicking and dragging?
            - Hint, look at the JS events mousedown, mouseup, and mouseover.
*/
let color;
let clearButton = document.querySelector("button");
let colors = [...document.querySelectorAll("#Sidebar > div")];
let tiles = [...document.querySelectorAll("#Main > div")];

let mouseDown = 0;
document.body.onmousedown = function() { 
  ++mouseDown;
}
document.body.onmouseup = function() {
  --mouseDown;
}

clearButton.addEventListener("click", () => {
    for (const tile of tiles) {
      tile.style.backgroundColor = "white";
    }
});

colors.forEach(item => item.addEventListener("click", (event) => {
    color = event.target.style.backgroundColor;
}));


tiles.forEach(item => item.addEventListener("mousedown", (event) => {
    if (color != null) event.target.style.backgroundColor = color;
}));


tiles.forEach(item => item.addEventListener("mouseover", (event) => {
    if (mouseDown && color != null) event.target.style.backgroundColor = color;
}));