CREATE TABLE visited_cafes(
    cafeid varchar(40) NOT NULL PRIMARY KEY,
    photoreference text NOT NULL,
    CONSTRAINT cafe_table
    FOREIGN KEY (cafeid) 
    REFERENCES cafe_table (cafeid)
)

create table photos (cafeid varchar(40) NOT NULL PRIMARY KEY,photoreference text NOT NULL, FOREIGN KEY cafeid REFERENCES cafe_table(cafeid))