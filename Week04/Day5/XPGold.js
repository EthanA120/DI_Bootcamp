/* TASK: My Book List
    
    The point of this challenge is to display a list of two books on your browser.
    
    1. In the body of the HTML page, create an empty div:
        <div class="listBooks"></div>

    2. In the js file, create an array called allBooks.
    This is an array of objects. Each object is a book that has 4 keys (ie. 4 properties):
        - title,
        - author,
        - image: a url,
        - alreadyRead: which is a boolean (true or false).

    3. Initiate the array with 2 books of your choice (ie. Add manually 2 books objects in the array)

    4. Requirements: All the instructions below need to be coded in the js file:
        1. Using the DOM, render the books inside an HTML table (the HTML table must be added to the <div> created in part 1).
            For each book:
                - You have to display the book's title and the book's author.
                    Example: Harry Potter written by JKRolling.
                - The width of the image has to be set to 100px.
                - If the book is already read. Set the color of the book's details to red.
*/
/**@type {HTMLElement}*/ let Ex1 = document.querySelector("#Ex1");
Ex1.style.marginBottom = "50px";

let allBooks = [
    {title: "The Giving Tree", author: "Sheldon Alan Silverstein", image: "https://upload.wikimedia.org/wikipedia/he/7/79/The_Giving_Tree.jpg", alreadyRead: true},
    {title: "Don Quixote", author: "Miguel de Cervantes", image: "https://kbimages1-a.akamaihd.net/c1f89dc7-4039-4135-a2fe-af0404183c9a/1200/1200/False/don-quixote-129.jpg", alreadyRead: false},
    {title: "The Alchemist", author: "Paulo Coelho", image: "https://assets.thalia.media/img/artikel/72d4cdeb57c293576e125b02c7fd69d4d66e2238-00-00.jpeg", alreadyRead: true},
];

/**@type {HTMLElement}*/ let listBooks = Ex1.querySelector(".listBooks");
listBooks.style.display = "flex";
allBooks.forEach(() => listBooks.appendChild(document.createElement("div")).setAttribute("class", "book"));

let book = Ex1.querySelectorAll(".book");
book.forEach((/**@type {HTMLElement}*/ item, i) => {
    item.setAttribute("id", allBooks[i].title.replaceAll(" ", ""));
    // item.style.width = "100px";
    item.style.padding = "10px";
    item.style.margin = "10px";
    item.style.border = "1px solid silver";
    item.style.borderRadius = "5px";

    item.appendChild(document.createElement("img")).setAttribute("src", allBooks[i].image);
    item.appendChild(document.createElement("h1")).textContent = allBooks[i].title;
    item.appendChild(document.createElement("p")).textContent = `Written by ${allBooks[i].author}`;
});

let image = Ex1.querySelectorAll("img");
image.forEach((item) => {
    // item.style.width = "100px";
    item.style.height = "500px";
});

let h1 = Ex1.querySelectorAll("h1");
h1.forEach((item, i) => {
    item.style.textAlign = "center";
    item.style.marginTop = "10px";
    item.style.marginBottom = "10px";
    item.style.fontFamily = "'Times New Roman', Times, serif";
    if (allBooks[i].alreadyRead == false) {
        item.style.color = "red";
    }
});

let p = Ex1.querySelectorAll("p");
p.forEach((item, i) => {
    item.style.textAlign = "center";
    item.style.marginTop = "10px";
    item.style.marginBottom = "10px";
    item.style.fontFamily = "'Arial', Times, serif";
    if (allBooks[i].alreadyRead == false) {
        item.style.color = "red";
    }
});


/* TASK: Red table
    
    Copy the code above and write some Javascript code to color all diagonal table cells in red.
*/
let Ex2 = document.querySelector("#Ex2");
let table = Ex2.firstElementChild;
let tr = table.querySelectorAll("tr");
for (const i in tr) {
    for (const j in tr[i].children) {
        if (i == j) {
            console.log(tr[i].children[j].textContent);
            tr[i].children[j].style.backgroundColor = "red";
        }
    }
}