### Exercise 1 : Items and customers
Instructions

We will work on the *public* database that we created yesterday.

**Part I**

1. Use SQL to get the following from the database:
   1. All items, ordered by price (lowest to highest).
   2. Items with a price above 80 (80 included), ordered by price (highest to lowest).
   3. The first 3 customers in alphabetical order of the first name (A-Z) – exclude the primary key column from the results.
   4. All last names (no other columns!), in reverse alphabetical order (Z-A)


2. Create a table named purchases. It should have 3 columns :
   - id : the primary key of the table
   - customer_id : this column references the table customers
   - item_id : this column references the table items
   - quantity_purchased : this column is the quantity of items purchased by a certain customer


3. Insert purchases for the customers, use subqueries:
    - Scott Scott bought one fan
    - Melanie Johnson bought ten large desks
    - Greg Jones bougth two small desks


The table purchases should look like this:
<table>
    <thead>
    <tr>
        <th>id</th>
        <th>customer_id</th>
        <th>item_id</th>
        <th>quantity_purchased</th>
    </tr>
    </thead>
    <tbody>
    <tr>
        <td>1</td>
        <td>3</td>
        <td>3</td>
        <td>1</td>
    </tr>
    <tr>
        <td>2</td>
        <td>5</td>
        <td>2</td>
        <td>10</td>
    </tr>
    <tr>
        <td>3</td>
        <td>1</td>
        <td>1</td>
        <td>2</td>
    </tr>
    </tbody>
</table>


<u>Here is the explanation of the first row:</u>
- id = 1, this is the auto-incrementing primary key
- customer_id = 3, because the id of Scott Scott in the customers table is 3
- item_id = 3, because the id of a fan in the items table is 3
- quantity_purchased = 1, because Scott Scott bought one fan


**Part II**

1. Use SQL to get the following from the database:
   1. All purchases. Is this information useful to us?
   2. All purchases, joining with the customers table.
   3. Purchases of the customer with the ID equal to 5.
   4. Purchases for a large desk AND a small desk


2. Use SQL to show all the customers who have made a purchase. Show the following fields/columns:
   1. Customer first name
   2. Customer last name
   3. Item name


3. Add a row which references a customer by ID, but does not reference an item by ID (leave it blank). Does this work? Why/why not?
