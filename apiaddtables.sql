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

