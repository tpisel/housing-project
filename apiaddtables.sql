-- Creating the tables for the type of dwelling for which the permit is applied

CREATE TABLE double_storeys AS
SELECT id, description, lat, lng, lga_fullname
FROM planning_application
WHERE description ~ 'double storey|two storey|2\) storey'
AND description ~ 'dwelling|residential';

CREATE TABLE three_storeys AS
SELECT id, description, lat, lng, lga_fullname
FROM planning_application
WHERE description ~ 'three storey|three storey|3\) storey'
AND description ~ 'dwelling|residential';

CREATE TABLE four_storeys AS
SELECT id, description, lat, lng, lga_fullname
FROM planning_application
WHERE description ~ 'four storey|4\) storey'
AND description ~ 'dwelling|residential';

CREATE TABLE five_storeys AS
SELECT id, description, lat, lng, lga_fullname
FROM planning_application
WHERE description ~ 'five storey|5\) storey'
AND description ~ 'dwelling|residential';

CREATE TABLE apartments AS
SELECT id, description, lat, lng, lga_fullname
FROM planning_application
WHERE description ~ 'apartment'
AND description ~ 'dwelling|residential';

CREATE TABLE single_storey AS
SELECT id, description, lat, lng, lga_fullname
FROM planning_application
WHERE description ~ 'single storey|one storey|1\) storey'
AND description ~ 'dwelling|residential'
AND description ~ 'development';

-- Adding in an additional column to mark the dwelling type

ALTER TABLE five_storeys ADD COLUMN storey INT DEFAULT 5;
ALTER TABLE four_storeys ADD COLUMN storey INT DEFAULT 4;
ALTER TABLE three_storeys ADD COLUMN storey INT DEFAULT 3;
ALTER TABLE double_storeys ADD COLUMN storey INT DEFAULT 2;
ALTER TABLE single_storey ADD COLUMN storey INT DEFAULT 1;
ALTER TABLE apartments ADD COLUMN storey INT DEFAULT 6;

-- Combining the tables via UNION, for a single table for the API

INSERT INTO single_storey (id, description, lat, lng, lga_fullname, storey)
SELECT id, description, lat, lng, lga_fullname, storey
FROM double_storeys
UNION
SELECT id, description, lat, lng, lga_fullname, storey
FROM three_storeys
UNION
SELECT id, description, lat, lng, lga_fullname, storey
FROM four_storeys
UNION
SELECT id, description, lat, lng, lga_fullname, storey
FROM five_storeys
UNION
SELECT id, description, lat, lng, lga_fullname, storey
FROM apartments;