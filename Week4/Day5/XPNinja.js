/* TASK: Calendar
    
    1. Create a function called createCalendar (year, month)
    2. The function should create a calendar for the given year/month.
    3. The calendar should be a table, where a week is <tr>, and a day is <td.
        The table top should be <th> with weekday names: the first day should be Monday, and so on until Sunday.
        
        Hint: There shouldn't be any code in the HTML file. The table should be created from the JS file using the DOM.
*/
function createCalendar(year, month) {
    
    let tableBorder = "1px solid silver";
    let tileWidth = "150px";
    let tileHeight = "50px";

    const daysOfWeek = {6: "Sunday", 0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday", 5: "Saturday"};
    const monthsOfYear = {0: "January", 1: "February", 2: "March", 3: "April", 4: "May", 5: "June", 6: "July", 7: "August", 8: "September", 9: "October", 10: "November", 11: "December"};

    if ((/\d/.test(month) && 1 <= month && month <= 12)) {
        month = monthsOfYear[month-1];
    }

    document.body.style.fontFamily = "gotham-rounded, helvetica neue, helvetica";
    let table = document.body.appendChild(document.createElement("table"));
    table.style.fontSize = "1.5em";
    table.style.border = tableBorder;
    table.style.borderCollapse = "collapse";
    table.style.textAlign = "center";

    let trMonth = table.appendChild(document.createElement("tr"));
    trMonth.setAttribute("id", "Month");
    trMonth.style.height = tileHeight;

    let trMonthName = trMonth.appendChild(document.createElement("th"));
    trMonthName.innerHTML = `${month} ${year}`;
    trMonthName.colSpan = "7";
    trMonthName.style.fontSize = "1.3em";

    let trDaysOfWeek = table.appendChild(document.createElement("tr"));
    trDaysOfWeek.setAttribute("id", "daysOfWeekRow");
    
    let thDaysOfWeek = [];
    for (let i = 0; i < 7; i++) {
        thDaysOfWeek.push(trDaysOfWeek.appendChild(document.createElement("th")));
        thDaysOfWeek[i].setAttribute("class", "dayOfWeek");
        thDaysOfWeek[i].textContent = daysOfWeek[i];
        thDaysOfWeek[i].style.width = tileWidth;
        thDaysOfWeek[i].style.height = tileHeight;
        thDaysOfWeek[i].style.border = tableBorder;
    }

    let trWeeksOfMonth = [];
    for (let i = 0; i < 6; i++) {
        trWeeksOfMonth.push(table.appendChild(document.createElement("tr")));
        trWeeksOfMonth[i].setAttribute("class", "weekOfMonth");
        trWeeksOfMonth[i].style.height = tileHeight;
        trWeeksOfMonth[i].style.border = tableBorder;
    }

    let tdDaysOfMonth = [];
    for (let i = 0; i < trWeeksOfMonth.length; i++) {
        tdDaysOfMonth.push([]);
        for (let j = 0; j < 7; j++) {
            tdDaysOfMonth[i].push(trWeeksOfMonth[i].appendChild(document.createElement("td")));
            tdDaysOfMonth[i][j].setAttribute("class", "dayOfMonth");
            tdDaysOfMonth[i][j].classList.add(daysOfWeek[j]);
            tdDaysOfMonth[i][j].textContent = ".";
            tdDaysOfMonth[i][j].style.width = tileWidth;
            tdDaysOfMonth[i][j].style.height = tileHeight;
            tdDaysOfMonth[i][j].style.border = tableBorder;
        }
    }
    
    const mondayOffset = {0:6, 1:0, 2:1, 3:2, 4:3, 5:4, 6:5};
    let date = [];
    let k = 0;
    for (let i = 0; i < tdDaysOfMonth.length; i++) {
        for (let j = 0; j < tdDaysOfMonth[i].length; j++) {
            date.push(new Date(`${month}/${k+1}/${year}`));

            if (tdDaysOfMonth[i][j].getAttribute("class").split(" ")[1] == daysOfWeek[mondayOffset[date[k].getDay()]] && monthsOfYear[date[k].getMonth()] == month) {
                tdDaysOfMonth[i][j].textContent = date[k].getDate();
                k++;

            } else {
                date.splice(k,1);
            }
        }
    }
}

createCalendar(2022, "1");
createCalendar(2021, "January");