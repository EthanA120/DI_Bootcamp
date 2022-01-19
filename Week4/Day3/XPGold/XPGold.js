/* TASK: Calculator
    
    Today we will be creating a fully functional calculator. In order to do this, we must have our HTML and Javascript files interact with each other.
    We will be using Javascript to dynamically calculate the outcome of the buttons that were clicked on the HTML.
    We will be adding an attribute called onclick to each button. The onclick attribute allows us to call a function from our Javascript file when the button is clicked.
    For example, if you click on the number 2 on the calculator (ie. seen below in the assets), the function number(2) will be called. The argument is the value of the button.

    Use HTML CSS for the visual.

    1. Create a HTML file for your calculator and a Js file for the calculator's functionality.
    2. You must create 3 functions in the js file:
        1. number (num)
        2. operator (operator)
        3. equal()
            Hint : you can use the eval() method to help with your calculations.
    3. Before coding, take your time to understand all the parts to the exercise and their process.
        You can write it down somewhere if it helps (recommended).
    4. Bonus: create the RESET and CLEAR buttons.
*/
function number(num) {
    let monitor = document.getElementById("Monitor").value;
    if (monitor == "0" && num != ".") {
        monitor = "";
    }
    
    num = num.toString();
    monitor += num;

    document.getElementById("Monitor").value = monitor;
}


function operator(operator) {
    document.getElementById("Monitor").value += operator;
}


function equal() {
    let monitor = document.getElementById("Monitor").value.replace(/[x]/g, "*");
    document.getElementById("Monitor").value = eval(monitor);
}


function clearMonitor(clearType) {
    let monitor = document.getElementById("Monitor").value;

    if (clearType == "clear") {
        document.getElementById("Monitor").value = "0";
    } else {
        document.getElementById("Monitor").value = monitor.slice(0, monitor.length-1);
    }
}

if (document.getElementById("Monitor").value.length == 0) {
    document.getElementById("Monitor").value = "0";
}
