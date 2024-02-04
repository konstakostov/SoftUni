-- -- 01. Mountains and Peaks
-- CREATE TABLE mountains(
--     id SERIAL PRIMARY KEY,
--     name VARCHAR(50)
-- );
--
-- CREATE TABLE peaks(
--     id SERIAL PRIMARY KEY,
--     name VARCHAR(50),
--     mountain_id INT,
--         CONSTRAINT fk_peaks_mountains
--             FOREIGN KEY (mountain_id)
--                 REFERENCES mountains(id)
-- );


-- -- 02. Trip Organization
-- SELECT
--     v.driver_id,
--     v.vehicle_type,
--     CONCAT_WS(
--         ' ',
--         c.first_name,
--         c.last_name) AS driver_name
-- FROM
--     vehicles AS v JOIN
--         campers AS c ON
--         v.driver_id = c.id;


-- -- 03. SoftUni Hiking
-- SELECT
--     r.start_point,
--     r.end_point,
--     r.leader_id,
--     CONCAT_WS(
--         ' ',
--         c.first_name,
--         c.last_name
--         ) AS leader_name
-- FROM
--     routes AS r
--         JOIN
--         campers AS c
--             ON
--             r.leader_id = c.id;


-- 04. Delete Mountains



-- 05. Project Management DB*


