-- Active: 1727229083863@@127.0.0.1@3306
CREATE TABLE IF NOT EXISTS 'pets' (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    type TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS 'people' (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age INTEGER NOT NULL,
    pet_id INTEGER,
    FOREIGN KEY (pet_id) REFERENCES pets (id)
);

INSERT INTO pets (name, type)
VALUES
    ("cobra", "snake"),
    ("cao", "dog"),
    ("gato", "cat"),
    ("jorgin", "hamster"),
    ("burro", "donkey"),
    ("shrek", "ogro"),
    ("belinha", "dog");
