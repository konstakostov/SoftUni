-- -- 01.	Booked for Nights
-- SELECT
--     CONCAT_WS(
--     ' ',
--     a.address,
--     a.address_2
--     ) AS "Apartment Address",
--     b.booked_for AS "Nights"
-- FROM
--     apartments AS a
-- JOIN
--     bookings as b
-- USING
--     (booking_id)
-- ORDER BY
--     a.apartment_id;


-- -- 02.	First 10 Apartments Booked At
-- SELECT
--     a.name AS "Name",
--     a.country AS "Country",
--     b.booked_at::date AS "Booked at"
-- FROM
--     apartments AS a
-- LEFT JOIN
--     bookings as b
-- USING
--     (booking_id)
-- LIMIT
--     10


-- -- 03.	First 10 Customers with Bookings
-- SELECT
--     b.booking_id AS "Booking ID",
--     b.starts_at::DATE AS "Start Date",
--     b.apartment_id AS "Apartment ID",
--     CONCAT_WS(
--     ' ',
--     c.first_name,
--     c.last_name
--     ) AS "Customer Name"
-- FROM
--     bookings as b
-- RIGHT JOIN
--     customers as c
-- USING
--     (customer_id)
-- ORDER BY
--     "Customer Name"
-- LIMIT
--     10


-- -- 04.	Booking Information
-- SELECT
--     b.booking_id AS "Booking ID",
--     a.name AS "Apartment Owner",
--     a.apartment_id AS "Apartment ID",
--     CONCAT_WS(
--     ' ',
--     c.first_name,
--     c.last_name
--     ) AS "Customer Name"
-- FROM
--     apartments AS a
-- FULL JOIN
--     bookings AS b
-- USING
--     (booking_id)
-- FULL JOIN
--     customers as c
-- USING
--     (customer_id)
-- ORDER BY
--     "Booking ID",
--     "Apartment Owner",
--     "Customer Name"


-- -- 05. Multiplication of Information**
-- SELECT
--     b.booking_id AS "Booking ID",
--     c.first_name AS customer_name
-- FROM
--     bookings AS b
-- CROSS JOIN
--     customers as c
-- ORDER BY
--     customer_name;


-- -- 06. Unassigned Apartments
-- SELECT
--     b.booking_id,
--     b.apartment_id,
--     c.companion_full_name
-- FROM
--     bookings AS b
-- JOIN
--     customers as c
-- USING
--     (customer_id)
-- WHERE
--     b.apartment_id IS NULL;


-- -- 07. Bookings Made by Lead
-- SELECT
--     b.apartment_id,
--     b.booked_for,
--     c.first_name,
--     c.country
-- FROM
--     bookings AS b
-- INNER JOIN
--     customers as c
-- USING
--     (customer_id)
-- WHERE
--     c.job_type = 'Lead';


-- -- 08. Hahn's Bookings
-- SELECT
--     count(*)
-- FROM
--     bookings as b
-- JOIN
--     customers AS c
-- USING
--     (customer_id)
-- WHERE
--     c.last_name = 'Hahn';


-- -- 09. Total Sum of Nights
-- SELECT
--     a.name,
--     SUM(b.booked_for)
-- FROM
--     apartments AS a
-- JOIN
--     bookings as b
-- USING
--     (apartment_id)
-- GROUP BY
--     a.name
-- ORDER BY
--     a.name;


-- -- 10. Popular Vacation Destination
-- SELECT
--     a.country,
--     COUNT(b.booking_id) AS booking_count
-- FROM
--     bookings AS b
-- JOIN
--     apartments as a
-- USING
--     (apartment_id)
-- WHERE
--     b.booked_at > '2021-05-18 07:52:09.904+03'
--         AND
--     b.booked_at < '2021-09-17 19:48:02.147+03'
-- GROUP BY
--     a.country
-- ORDER BY
--     booking_count DESC;


-- -- 11. Bulgaria's Peaks Higher than 2835 Meters
-- SELECT
--     mc.country_code,
--     m.mountain_range,
--     p.peak_name,
--     p.elevation
-- FROM
--     mountains_countries AS mc
-- JOIN
--     mountains AS m
-- ON
--     m.id = mc.mountain_id
-- JOIN
--     peaks AS p
-- ON
--     m.id = p.mountain_id
-- WHERE
--     p.elevation > 2835
--         AND
--     mc.country_code = 'BG'
-- ORDER BY
--     p.elevation DESC;


-- -- 12. Count Mountain Ranges
-- SELECT
--     mc.country_code,
--     COUNT(m.mountain_range) AS mountain_range_count
-- FROM
--     mountains_countries AS mc
-- JOIN
--         mountains AS m
-- ON
--     mc.mountain_id = m.id
-- WHERE
--     mc.country_code IN ('US', 'RU', 'BG')
-- GROUP BY
--     mc.country_code
-- ORDER BY
--     mc.country_code;


-- -- 13. Rivers in Africa
-- SELECT
--     c.country_name,
--     r.river_name
-- FROM
--     countries as c
-- LEFT JOIN
--     countries_rivers AS cr
-- USING
--     (country_code)
-- LEFT JOIN
--     rivers AS r
-- ON
--     cr.river_id = r.id
-- WHERE
--     c.continent_code = 'AF'
-- ORDER BY
--     c.country_name
-- LIMIT
--     5;


-- -- 14. Minimum Average Area Across Continents
-- SELECT
--     MIN(average)
-- FROM
--     (
--     SELECT
--         AVG(area_in_sq_km) AS average
--     FROM
--         countries
--     GROUP BY
--         continent_code
--     ) AS min_average_area


-- -- 15. Countries Without Any Mountains
-- SELECT
--     COUNT(*)
-- FROM
--     countries AS c
-- LEFT JOIN
--     mountains_countries AS mc
-- USING
--     (country_code)
-- WHERE
--     mc.mountain_id IS NULL;


-- -- 16. * Monasteries by Country
-- CREATE TABLE monasteries(
--     "id" SERIAL PRIMARY KEY,
--     monastery_name VARCHAR(255),
--     country_code CHAR(2)
-- );
--
-- INSERT INTO
--     monasteries(monastery_name, country_code)
-- VALUES
--     ('Rila Monastery "St. Ivan of Rila"', 'BG'),
--     ('Bachkovo Monastery "Virgin Mary"', 'BG'),
--     ('Troyan Monastery "Holy Mother''s Assumption"', 'BG'),
--     ('Kopan Monastery', 'NP'),
--     ('Thrangu Tashi Yangtse Monastery', 'NP'),
--     ('Shechen Tennyi Dargyeling Monastery', 'NP'),
--     ('Benchen Monastery', 'NP'),
--     ('Southern Shaolin Monastery', 'CN'),
--     ('Dabei Monastery', 'CN'),
--     ('Wa Sau Toi', 'CN'),
--     ('Lhunshigyia Monastery', 'CN'),
--     ('Rakya Monastery', 'CN'),
--     ('Monasteries of Meteora', 'GR'),
--     ('The Holy Monastery of Stavronikita', 'GR'),
--     ('Taung Kalat Monastery', 'MM'),
--     ('Pa-Auk Forest Monastery', 'MM'),
--     ('Taktsang Palphug Monastery', 'BT'),
--     ('Sümela Monastery', 'TR');
--
-- ALTER TABLE
--     countries
-- ADD COLUMN
--     three_rivers BOOLEAN DEFAULT FALSE;
--
-- UPDATE
--     countries
-- SET
--     three_rivers = (
--         SELECT
--             COUNT(*) >= 3
--         FROM
--             countries_rivers AS cr
--         WHERE
--             cr.country_code = countries.country_code
--         );
--
-- SELECT
--     m.monastery_name AS "Monastery",
--     c.country_name AS "Country"
-- FROM
--     monasteries AS m
-- JOIN
--     countries AS c
-- USING
--     (country_code)
-- WHERE
--     NOT three_rivers
-- ORDER BY
--     monastery_name;


-- 17. * Monasteries by Continents and Countries



-- -- 18. Retrieving Information about Indexes
-- SELECT
--     tablename,
--     indexname,
--     indexdef
-- FROM
--     pg_indexes
-- WHERE
--     schemaname = 'public'
-- ORDER BY
--     tablename,
--     indexname;


-- 19. * Continents and Currencies



-- 20. * The Highest Peak in Each Country


