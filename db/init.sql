create database airTravel;
use airTravel;

CREATE TABLE IF NOT EXISTS airTravelImport (
    `id` int AUTO_INCREMENT,
    `Month` VARCHAR(3) CHARACTER SET utf8,
    `Column_1958` INT,
    `Column_1959` INT,
    `Column_1960` INT,
    primary key(id)
);

INSERT INTO airTravelImport (Month, Column_1958, Column_1959, Column_1960) VALUES
    ('JAN',  340,  360,  417),
    ('FEB',  318,  342,  391),
    ('MAR',  362,  406,  419),
    ('APR',  348,  396,  461),
    ('MAY',  363,  420,  472),
    ('JUN',  435,  472,  535),
    ('JUL',  491,  548,  622),
    ('AUG',  505,  559,  606),
    ('SEP',  404,  463,  508),
    ('OCT',  359,  407,  461),
    ('NOV',  310,  362,  390),
    ('DEC',  337,  405,  432);

SELECT * from airTravelImport;