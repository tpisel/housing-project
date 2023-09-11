-- table schema for the database


CREATE TABLE G02
(
    LGA_CODE_2021 VARCHAR(16) NOT NULL,
    category TEXT UNIQUE NOT NULL,
    CONSTRAINT pk_category
        PRIMARY KEY (category_id)
);
