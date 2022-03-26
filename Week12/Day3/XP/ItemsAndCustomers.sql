CREATE TABLE items(
	item_id SERIAL PRIMARY KEY,
	item VARCHAR(50) NOT NULL,
	price SMALLINT NOT NULL
);

INSERT INTO items (item, price)
VALUES('Small Desk', 100), ('Large desk', 300), ('Fan', 80);


CREATE TABLE customers(
	customer_id SERIAL PRIMARY KEY,
	first_name VARCHAR(20) NOT NULL,
	last_name VARCHAR(20) NOT NULL
);

INSERT INTO customers (first_name, last_name)
VALUES('Greg', 'Jones'), ('Sandra', 'Jones'), ('Scott', 'Scott'), ('Trevor', 'Green'), ('Melanie', 'Johnson');

SELECT * FROM items;
SELECT * FROM items WHERE price >= 90;
SELECT * FROM items WHERE price <= 200;

SELECT * FROM customers;
SELECT * FROM customers WHERE last_name = 'Smith';
SELECT * FROM customers WHERE last_name = 'Jones';
SELECT * FROM customers WHERE first_name != 'Scott';
