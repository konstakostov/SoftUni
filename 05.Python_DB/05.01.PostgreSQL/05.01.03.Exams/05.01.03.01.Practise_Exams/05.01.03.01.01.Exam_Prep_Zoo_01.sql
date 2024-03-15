-- -- -- SECTION 01
-- -- 01. Database Design
DROP TABLE IF EXISTS owners;
CREATE TABLE owners(
    "id" SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    phone_number VARCHAR(50) NOT NULL,
    address VARCHAR(50)
);

DROP TABLE IF EXISTS animal_types;
CREATE TABLE animal_types(
    "id" SERIAL PRIMARY KEY,
    animal_type VARCHAR(50) NOT NULL
);

DROP TABLE IF EXISTS cages;
CREATE TABLE cages(
    "id" SERIAL PRIMARY KEY,
    animal_type_id INT NOT NULL
);


DROP TABLE IF EXISTS animals;
CREATE TABLE animals(
    "id" SERIAL PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    birthdate DATE NOT NULL,
    owner_id INT,
    animal_type_id INT NOT NULL
);

DROP TABLE IF EXISTS volunteers_departments;
CREATE TABLE volunteers_departments(
    "id" SERIAL PRIMARY KEY,
    department_name VARCHAR(30) NOT NULL
);

DROP TABLE IF EXISTS volunteers;
CREATE TABLE volunteers(
    "id" SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    phone_number VARCHAR(15) NOT NULL,
    address VARCHAR(50),
    animal_id INT,
    department_id INT NOT NULL
);

DROP TABLE IF EXISTS animals_cages;
CREATE TABLE animals_cages(
    cage_id INT NOT NULL,
    animal_id INT NOT NULL
);

ALTER TABLE cages
    ADD CONSTRAINT fk_cages_animal_types
        FOREIGN KEY (animal_type_id)
            REFERENCES animal_types(id)
                ON DELETE CASCADE;

ALTER TABLE animals
    ADD CONSTRAINT fk_animals_owners
        FOREIGN  KEY (owner_id)
        REFERENCES owners(id),
    ADD CONSTRAINT fk_animals_animal_types
        FOREIGN KEY (animal_type_id)
            REFERENCES animal_types(id)
                ON DELETE CASCADE;

ALTER TABLE volunteers
    ADD CONSTRAINT fk_volunteers_animals
        FOREIGN KEY (animal_id)
            REFERENCES animals(id),
    ADD CONSTRAINT fk_volunteers_volunteers_departments
        FOREIGN KEY (department_id)
            REFERENCES volunteers_departments(id)
                ON DELETE CASCADE;

ALTER TABLE animals_cages
    ADD CONSTRAINT fk_animals_cages_cages
        FOREIGN KEY (cage_id)
            REFERENCES cages(id),
    ADD CONSTRAINT fk_animals_cages_animals
        FOREIGN KEY (animal_id)
            REFERENCES animals(id)
                ON DELETE CASCADE;


-- -- -- Section 02
-- -- 02. Insert
INSERT INTO
    volunteers(name, phone_number, address, animal_id, department_id)
VALUES
    ('Anita Kostova', '0896365412', 'Sofia, 5 Rosa str.', 15, 1),
    ('Dimitur Stoev', '0877564223', NULL, 42, 4),
    ('Kalina Evtimova', '0896321112', 'Silistra, 21 Breza str.', 9, 7),
    ('Stoyan Tomov', '0898564100', 'Montana, 1 Bor str.', 18, 8),
    ('Boryana Mileva', '0888112233', NULL, 31, 5);

INSERT INTO
    animals(name, birthdate, owner_id, animal_type_id)
VALUES
    ('Giraffe', '2018-09-21', 21, 1),
    ('Harpy Eagle', '2015-04-17', 15, 3),
    ('Hamadryas Baboon', '2017-11-02', NULL, 1),
    ('Tuatara', '2021-06-30', 2, 4);

-- SAMPLE DATA volunteers
--     ('Anita Kostova', '0896365412', 'Sofia, 5 Rosa str.', 15, 1),
--     ('Dimitur Stoev', '0877564223', NULL, 42, 4),
--     ('Kalina Evtimova', '0896321112', 'Silistra, 21 Breza str.', 9, 7),
--     ('Stoyan Tomov', '0898564100', 'Montana, 1 Bor str.', 18, 8),
--     ('Boryana Mileva', '0888112233', NULL, 31, 5);
-- -- SAMPLE DATA animals
--     ('Giraffe', '2018-09-21', 21, 1),
--     ('Harpy Eagle', '2015-04-17', 15, 3),
--     ('Hamadryas Baboon', '2017-11-02', NULL, 1),
--     ('Tuatara', '2021-06-30', 2, 4);


-- -- -- Section 02
-- -- 03. Update
UPDATE
    animals
SET
    owner_id = 4
WHERE
    owner_id IS NULL;


-- -- -- Section 02
-- -- 04. Delete VERSION 01
DELETE FROM
    volunteers
WHERE
    department_id
IN (SELECT
        id
    FROM
        volunteers_departments
    WHERE
        department_name = 'Education program assistant'
    );

DELETE FROM
    volunteers_departments
WHERE
    department_name = 'Education program assistant';

-- -- 04. Delete VERSION 02
DELETE FROM
    volunteers_departments
WHERE
    department_name = 'Education program assistant';


-- -- -- Section 03
-- -- 05. Volunteers
SELECT
    name,
    phone_number,
    address,
    animal_id,
    department_id
FROM
    volunteers
ORDER BY
    name,
    animal_id,
    department_id


-- -- -- Section 03
-- -- 06. Animal Data
SELECT
    a.name,
    at.animal_type,
    TO_CHAR(a.birthdate, 'DD.MM.YYYY') AS birthdate
FROM
    animals AS a
LEFT JOIN
    animal_types AS at
ON
    a.animal_type_id = at.id
ORDER BY
    a.name


-- -- -- Section 03
-- -- 07. Owners and Their Animals
SELECT
    o.name AS "Owner",
    COUNT(a.owner_id) AS "Count of animals"
FROM
    owners AS o
JOIN
    animals AS a
ON
    o.id = a.owner_id
GROUP BY
    o.name
ORDER BY
    "Count of animals" DESC,
    "Owner"
LIMIT
    5;


-- -- -- Section 03
-- -- 08. Owners, Animals and Cages
SELECT
    CONCAT(
    o.name,
    ' - ',
    a.name
    ) AS "Owners - Animals",
    o.phone_number AS "Phone Number",
    ac.cage_id AS "Cage ID"
FROM
    owners AS o
        JOIN animals AS a
            ON o.id = a.owner_id
                JOIN animals_cages AS ac
                    ON a.id = ac.animal_id
                        JOIN animal_types AS at
                            ON a.animal_type_id = at.id
WHERE
    animal_type = 'Mammals'
ORDER BY
    o.name,
    a.name DESC;


-- -- -- Section 03
-- -- 09. Volunteers in Sofia VERSION 01
SELECT
    v.name AS"Volunteers Name",
    v.phone_number AS "Phone Number",
    SUBSTRING(v.address FROM ', (.*)$') AS "Address"
FROM
    volunteers AS v
JOIN
    volunteers_departments AS vd
ON
    v.department_id = vd.id
WHERE
    vd.department_name = 'Education program assistant'
        AND
    v.address ILIKE '%Sofia%'
ORDER BY
    v.name;

-- -- 09. Volunteers in Sofia VERSION 02
SELECT
    v.name AS "Volunteers Name",
    v.phone_number AS "Phone Number",
    TRIM(REPLACE(TRIM(REPLACE(v.address, 'Sofia', '')), ',', '')) AS "Address"
FROM
    volunteers AS v
JOIN
    volunteers_departments AS vd
ON
    vd.id = v.department_id
WHERE
    address LIKE '%Sofia%'
        AND
    department_name = 'Education program assistant'
ORDER BY
    name


-- -- -- Section 03
-- -- 10. Animals for Adoption VERSION 01
SELECT
    a.name AS "Animal Name",
    EXTRACT(YEAR FROM a.birthdate) AS "Birth Year",
    at.animal_type AS "Animal Type"
FROM
    animals AS a
JOIN
    animal_types AS at
ON
    a.animal_type_id = at.id
WHERE
    at.animal_type <> 'Birds'
        AND
    AGE('01/01/2022', a.birthdate) < interval '5 years'
        AND
    a.owner_id IS NULL
ORDER BY
    a.name;

-- -- 10. Animals for Adoption VERSION 02
SELECT
    a.name AS "Animal Name",
    TO_CHAR(a.birthdate, 'YYYY') AS "Birth Year",
    at.animal_type AS "Animal Type"
FROM
    animals as a
LEFT JOIN
    animal_types AS at
ON
    a.animal_type_id = at.id
WHERE
    a.owner_id IS NULL
        AND
    at.animal_type <> 'Birds'
        AND
    AGE('01/01/2022', a.birthdate) < '5 years'
ORDER BY
    a.name;


-- -- -- Section 04
-- -- 11. All Volunteers in a Department VERSION 02
CREATE OR REPLACE FUNCTION fn_get_volunteers_count_from_department(
    searched_volunteers_department VARCHAR(30)
) RETURNS INT
AS
$$
    DECLARE
        volunteers_count INT;
    BEGIN
        SELECT
            COUNT(v.department_id)
        INTO
            volunteers_count
        FROM
            volunteers_departments AS vd
        JOIN
            volunteers AS v
        ON
            vd.id = v.department_id
        WHERE
            vd.department_name = searched_volunteers_department;
        RETURN
            volunteers_count;
    END;
$$
LANGUAGE plpgsql;

SELECT fn_get_volunteers_count_from_department('Education program assistant');
SELECT fn_get_volunteers_count_from_department('Guest engagement');
SELECT fn_get_volunteers_count_from_department('Zoo events');

-- -- 11. All Volunteers in a Department VERSION 02
CREATE OR REPLACE FUNCTION fn_get_volunteers_count_from_department(
    searched_volunteers_department VARCHAR(30)
) RETURNS INT
AS
$$
    DECLARE
        volunteers_counter INT;
    BEGIN
        SELECT
            COUNT(v.id)
        INTO
            volunteers_counter
        FROM
            volunteers AS v
        JOIN
            volunteers_departments AS vd
        ON
            v.department_id = vd.id
        WHERE department_name = searched_volunteers_department;

        RETURN
            volunteers_counter;
    END;
$$
LANGUAGE plpgsql;

SELECT fn_get_volunteers_count_from_department('Education program assistant');
SELECT fn_get_volunteers_count_from_department('Guest engagement');
SELECT fn_get_volunteers_count_from_department('Zoo events');


-- -- -- Section 04
-- -- 12. Animals with Owner or Not VERSION 01
CREATE OR REPLACE PROCEDURE sp_animals_with_owners_or_not(
    IN animal_name VARCHAR(30),
    OUT owner_name VARCHAR(50)
)
AS
$$
    BEGIN
        SELECT
            COALESCE(o.name, 'For adoption')
        INTO
            owner_name
        FROM
            animals AS a
        LEFT JOIN
            owners AS o
        ON
            a.owner_id = o.id
        WHERE
            a.name = animal_name;
    END;
$$
LANGUAGE plpgsql;

-- -- 12. Animals with Owner or Not VERSION 02
CREATE OR REPLACE PROCEDURE sp_animals_with_owners_or_not(
    IN animal_name VARCHAR(30),
    OUT result VARCHAR(30)
)
AS
$$
    BEGIN
        SELECT
            o.name
        FROM
            owners AS o
        LEFT JOIN
            animals AS a
        ON
            o.id = a.owner_id
        WHERE
            a.name = animal_name
        INTO
            result;

        IF result IS NULL THEN
            result := 'For adoption';
        END IF;
        RETURN;
    END;
$$
LANGUAGE plpgsql;

CALL sp_animals_with_owners_or_not('Pumpkinseed Sunfish');
CALL sp_animals_with_owners_or_not('Hippo');
CALL sp_animals_with_owners_or_not('Brown bear');