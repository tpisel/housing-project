-- Creating the tables for the type of dwelling for which the permit is applied

ALTER TABLE table_name
ADD COLUMN 2021_ASGS_Non_ABS_Structures data_type DEFAULT 
    (CASE 
        WHEN lga_fullname = bayside_vic THEN 'LGA20910'
        WHEN lga_fullname = melbourne_city THEN 'LGA24600'
        WHEN lga_fullname = city_of_port_phillip  THEN 'LGA25900'
     WHEN lga_fullname = greater_dandenong THEN 'LGA22670'
     WHEN lga_fullname = kingston THEN 'LGA23430'
     WHEN lga_fullname = boroondara_city THEN 'LGA21110'
     WHEN lga_fullname = casey THEN 'LGA21610'
     WHEN lga_fullname = frankston_city THEN 'LGA22170'
     WHEN lga_fullname = stonnington THEN 'LGA26350'
     WHEN lga_fullname = darebin THEN 'LGA21890'
     WHEN lga_fullname = hume THEN 'LGA23270'
     WHEN lga_fullname = hobsons_bay THEN 'LGA23110'
     WHEN lga_fullname = knox THEN 'LGA23670'
     WHEN lga_fullname = manningham THEN 'LGA24210'
     WHEN lga_fullname = banyule THEN 'LGA20660'
     WHEN lga_fullname = cardinia THEN 'LGA21450'
     WHEN lga_fullname = brimbank THEN 'LGA21180'
     WHEN lga_fullname = maribyrnong THEN 'LGA24330'
     WHEN lga_fullname = maroondah_city THEN 'LGA24410'
     WHEN lga_fullname = moreland_city THEN 'LGA25250' 
     WHEN lga_fullname = melton THEN 'LGA24650'
     WHEN lga_fullname = monash THEN 'LGA24970'
     WHEN lga_fullname = moonee_valley THEN 'LGA25060'
     WHEN lga_fullname = mornington_peninsula THEN 'LGA25340'
     WHEN lga_fullname = whitehorse THEN 'LGA27070'
     WHEN lga_fullname = wyndham THEN 'LGA27260'
     WHEN lga_fullname = yarra_city THEN 'LGA27070'
     WHEN lga_fullname = yarra_ranges THEN 'LGA27450'
     WHEN lga_fullname = glen_eira THEN 'LGA27070'
     WHEN lga_fullname = nillumbik THEN 'LGA25710'
     WHEN lga_fullname = latrobe THEN 'LGA23810'
     ELSE lga_fullname = lga_fullname
    END);



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