SELECT * FROM items ORDER BY price;
SELECT * FROM items WHERE price >= 80 ORDER BY price DESC;
SELECT first_name, last_name FROM customers ORDER BY first_name LIMIT 3;
SELECT last_name FROM customers ORDER BY last_name DESC;

CREATE TABLE purchases(
    purchase_id SERIAL PRIMARY KEY,
    customer_id SMALLINT NOT NULL,
    item_id SMALLINT NOT NULL,
    quantity_purchased SMALLINT NOT NULL
);

INSERT INTO purchases (customer_id, item_id, quantity_purchased)
VALUES (
        (SELECT customer_id FROM customers WHERE first_name='Scott' AND last_name='Scott'),
        (SELECT item_id FROM items WHERE item = 'Fan'), 1
        ),
       (
        (SELECT customer_id FROM customers WHERE first_name='Melanie' AND last_name='Johnson'),
        (SELECT item_id FROM items WHERE item = 'Large Desk'), 10
        ),
       (
        (SELECT customer_id FROM customers WHERE first_name='Greg' AND last_name='Jones'),
        (SELECT item_id FROM items WHERE item = 'Small Desk'), 2
        );

-- Useful to know who bought what.
SELECT * FROM purchases;
SELECT * FROM purchases JOIN customers ON purchases.customer_id = customers.customer_id;
SELECT * FROM purchases WHERE customer_id = 5;
 SELECT * FROM purchases WHERE item_id = (SELECT item_id FROM items WHERE item = 'Large Desk') OR item_id = (SELECT item_id FROM items WHERE item = 'Small Desk');

SELECT first_name FROM customers;
SELECT last_name FROM customers;
SELECT item FROM items;

INSERT INTO purchases (customer_id, item_id, quantity_purchased)
VALUES (
        (SELECT customer_id FROM customers WHERE first_name='Scott' AND last_name='Scott'), , 1
        );
-- Value set to NOT NULL so it can't be NULL.