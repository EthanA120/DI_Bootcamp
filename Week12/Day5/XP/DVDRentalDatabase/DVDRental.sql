SELECT * FROM customer;

SELECT concat(first_name, ' ', last_name) AS full_name FROM customer;

SELECT create_date FROM customer GROUP BY create_date;

SELECT * FROM customer ORDER BY first_name DESC;

SELECT film_id, title, description, release_year, rental_rate FROM film ORDER BY rental_rate;

SELECT address.address, phone FROM address WHERE district = 'Texas';

SELECT * FROM film WHERE film_id IN (15, 150);

SELECT film_id, title, description, length, rental_rate FROM film WHERE title = 'Alien Center';

SELECT film_id, title, description, length, rental_rate FROM film WHERE title LIKE 'Al%';

SELECT * FROM film ORDER BY rental_rate LIMIT 10;

SELECT * FROM film ORDER BY rental_rate OFFSET 10 FETCH FIRST 10 ROWS ONLY;

SELECT amount, payment_date FROM customer JOIN payment ON customer.customer_id = payment.customer_id;

SELECT * FROM film LEFT JOIN inventory ON film.film_id = inventory.film_id WHERE inventory.film_id IS NULL;

SELECT city, district FROM address JOIN city ON address.city_id = city.city_id GROUP BY city.city, district;