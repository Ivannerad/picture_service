CREATE TABLE extension (
    id serial PRIMARY KEY,
    name varchar(6)
);

CREATE TABLE images (
    extension_id int,
    name varchar(100),
    CONSTRAINT fk_extension
      FOREIGN KEY(extension_id) 
	  REFERENCES extension(id)
	  ON DELETE CASCADE
);