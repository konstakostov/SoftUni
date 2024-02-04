-- -- -- SECTION 01
-- -- 01. Database Design
DROP TABLE IF EXISTS addresses;
CREATE TABLE addresses(
    "id" SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

DROP TABLE IF EXISTS categories;
CREATE TABLE categories(
    "id" SERIAL PRIMARY KEY,
    name VARCHAR(10) NOT NULL
);

DROP TABLE IF EXISTS clients;
CREATE TABLE clients(
    "id" SERIAL PRIMARY KEY,
    full_name VARCHAR(50) NOT NULL,
    phone_number VARCHAR(20) NOT NULL
);

DROP TABLE IF EXISTS drivers;
CREATE TABLE drivers(
    "id" SERIAL PRIMARY KEY,
    first_name VARCHAR(30) NOT NULL,
    last_name VARCHAR(30) NOT NULL,
    age INT CHECK (age > 0) NOT NULL,
    rating NUMERIC(3, 2) DEFAULT 5.5
);

DROP TABLE IF EXISTS cars;
CREATE TABLE cars(
    "id" SERIAL PRIMARY KEY ,
    make VARCHAR(20) NOT NULL ,
    model VARCHAR(20),
    year INT DEFAULT 0 CHECK (year > 0) NOT NULL,
    mileage INT DEFAULT 0 CHECK (mileage > 0),
    condition CHAR(1) NOT NULL,
    category_id INT NOT NULL
);

DROP TABLE IF EXISTS courses;
CREATE TABLE courses(
    "id" SERIAL PRIMARY KEY ,
    from_address_id INT NOT NULL,
    start TIMESTAMP NOT NULL,
    bill NUMERIC(10, 2) DEFAULT 10 CHECK (bill > 0),
    car_id INT NOT NULL,
    client_id INT NOT NULL
);

DROP TABLE IF EXISTS cars_drivers;
CREATE TABLE cars_drivers(
    car_id INT NOT NULL ,
    driver_id INT NOT NULL
);

ALTER TABLE cars
    ADD CONSTRAINT fk_cars_categories
        FOREIGN KEY (category_id)
            REFERENCES categories(id)
                ON UPDATE CASCADE
                ON DELETE CASCADE;

ALTER TABLE courses
    ADD CONSTRAINT fk_courses_addresses
        FOREIGN KEY (from_address_id)
            REFERENCES addresses(id)
                ON UPDATE CASCADE
                ON DELETE CASCADE,
    ADD CONSTRAINT fk_courses_cars
        FOREIGN KEY (car_id)
            REFERENCES cars(id)
                ON UPDATE CASCADE
                ON DELETE CASCADE,
ADD CONSTRAINT fk_courses_clients
        FOREIGN KEY (client_id)
            REFERENCES clients(id)
                ON UPDATE CASCADE
                ON DELETE CASCADE;

ALTER TABLE cars_drivers
    ADD CONSTRAINT fk_cars_drivers_cars
        FOREIGN KEY (car_id)
            REFERENCES cars(id)
                ON UPDATE CASCADE
                ON DELETE CASCADE,
    ADD CONSTRAINT fk_cars_drivers_drivers
        FOREIGN KEY (driver_id)
            REFERENCES drivers(id)
                ON UPDATE CASCADE
                ON DELETE CASCADE;


-- -- -- Section 02
-- -- 02. Insert
INSERT INTO
    clients(full_name, phone_number)
SELECT
    CONCAT_WS(
    ' ',
    first_name,
    last_name
    ) AS full_name,
    '(088) 9999' || drivers.id * 2 AS phone_number
FROM
    drivers
WHERE
    id BETWEEN 10 AND 20;


-- -- -- Section 02
-- -- 03. Update
UPDATE
    cars
SET
    condition = 'C'
WHERE
    (mileage > 800000 OR mileage IS NULL)
        AND
    year <= 2010
        AND
    make <> 'Mercedes-Benz'


-- -- -- Section 02
-- -- 04. Delete
DELETE FROM
    clients
WHERE
    id NOT IN (SELECT client_id FROM courses)
        AND
    LENGTH(full_name) > 3;


-- -- -- Section 03
-- -- 05. Cars
SELECT
    d.first_name,
    d.last_name,
    c.make,
    c.model,
    c.mileage
FROM
    drivers AS d
JOIN
    cars_drivers AS cd
ON
    d.id = cd.driver_id
JOIN
    cars AS c
ON
    cd.car_id = c.id
WHERE
    c.mileage IS NOT NULL
ORDER BY
    mileage DESC ,
    first_name;


-- -- -- Section 03
-- -- 06. Drivers and Cars
SELECT
    ca.id AS car_id,
    ca.make AS make,
    ca.mileage AS mileage,
    COUNT(co.car_id) AS count_of_courses,
    ROUND(AVG(co.bill), 2) AS average_bill
FROM
    cars AS ca
LEFT JOIN
    courses AS co
ON
    ca.id = co.car_id
GROUP BY
    ca.id
HAVING
    COUNT(co.id) <> 2
ORDER by
    count_of_courses DESC,
    ca.id


-- -- -- Section 03
-- -- 07.Number of Courses for Each Car
SELECT
    ca.id AS car_id,
    ca.make AS make,
    ca.mileage AS mileage,
    COUNT(co.car_id) AS count_of_courses,
    ROUND(AVG(co.bill), 2) AS average_bill
FROM
    cars AS ca
LEFT JOIN
    courses AS co
ON
    ca.id = co.car_id
GROUP BY
    ca.id
HAVING
    COUNT(co.id) <> 2
ORDER by
    count_of_courses DESC,
    ca.id


-- -- -- Section 03
-- -- 08. Regular Clients
SELECT
    cl.full_name,
    COUNT(car_id) AS count_of_cars,
    SUM(co.bill) AS total_sum
FROM
    clients AS cl
JOIN
    courses AS co
ON
    cl.id = co.client_id
WHERE
    SUBSTRING(cl.full_name FROM 2 FOR 1) = 'a'
GROUP BY
    cl.full_name
HAVING
    COUNT(co.car_id) > 1
ORDER BY
    full_name;


-- -- -- Section 03
-- -- 09. Full Information of Courses
SELECT
    ad.name AS address,
    CASE
        WHEN EXTRACT(HOUR FROM co.start) BETWEEN 6 AND 20 THEN 'Day'
        ELSE 'Night'
    END AS day_time,
    co.bill,
    cl.full_name,
    ca.make,
    ca.model,
    ct.name
FROM
    courses AS co
JOIN
    addresses AS ad
ON
    co.from_address_id = ad.id
JOIN
    clients AS cl
ON
    co.client_id = cl.id
JOIN
    cars AS ca
ON
    co.car_id = ca.id
JOIN
    categories AS ct
ON
    ca.category_id = ct.id
ORDER BY
    co.id


-- -- -- Section 04
-- -- 10. Find all Courses by Client’s Phone Number
CREATE OR REPLACE FUNCTION fn_courses_by_client(
    phone_num VARCHAR(20)
) RETURNS INT
AS
$$
    DECLARE
        courses_counter INT;
    BEGIN
        SELECT
            COUNT(client_id)
        INTO
            courses_counter
        FROM
            clients AS cl
        JOIN
            courses AS co
        ON
            cl.id = co.client_id
        WHERE
            phone_num = cl.phone_number;

        RETURN
            courses_counter;
    END;
$$
LANGUAGE plpgsql;

SELECT fn_courses_by_client('(803) 6386812');
SELECT fn_courses_by_client('(831) 1391236');
SELECT fn_courses_by_client('(704) 2502909');


-- -- -- Section 04
-- -- 11. Full Info for Address
CREATE TABLE search_results(
    id SERIAL PRIMARY KEY,
    address_name VARCHAR(50),
    full_name VARCHAR(100),
    level_of_bill VARCHAR(20),
    make VARCHAR(30),
    condition CHAR(1),
    category_name VARCHAR(50)
);


CREATE OR REPLACE PROCEDURE sp_courses_by_address(
    address_name VARCHAR(100)
)
AS
$$
    BEGIN
        TRUNCATE search_results;

        INSERT INTO search_results(
            address_name,
            full_name,
            level_of_bill,
            make,
            condition,
            category_name
        )
        SELECT
            ad.name,
            cl.full_name,
            CASE
                WHEN co.bill <= 20 THEN 'Low'
                WHEN co.bill <= 30 THEN 'Medium'
                ELSE 'High'
            END,
            ca.make,
            ca.condition,
            ct.name
        FROM
            courses AS co
        JOIN
            clients AS cl
        ON
            cl.id = co.client_id
        JOIN
            cars AS ca
        ON
            co.car_id = ca.id
        JOIN
            addresses AS ad
        ON
            co.from_address_id = ad.id
        JOIN
            categories AS ct
        ON
            ca.category_id = ct.id
        WHERE
            ad.name = address_name
        ORDER BY
            make,
            full_name;
    END;
$$
LANGUAGE plpgsql;


CALL sp_courses_by_address('700 Monterey Avenue');
SELECT * FROM search_results;

CALL sp_courses_by_address('66 Thompson Drive');
SELECT * FROM search_results;


