-- database: UniqueMealDB.db
DROP TABLE IF EXISTS memberrs;


CREATE TABLE IF NOT EXISTS memberrs (
    MembershipID TEXT PRIMARY KEY,
    FirstName TEXT NOT NULL,
    LastName TEXT NOT NULL,
    Age INTEGER,
    Gender TEXT,
    Weight REAL,
    Street TEXT,
    HouseNumber TEXT,
    ZipCode TEXT,
    City TEXT,
    Email TEXT,
    PhoneNumber TEXT,
    RegistrationDate TEXT
);

INSERT INTO memberrs (MembershipID, FirstName, LastName, Age, Gender, Weight, Street, HouseNumber, ZipCode, City, Email, PhoneNumber, RegistrationDate)
VALUES ("24103458375","getgwtrst2", "Lagewtgrtjhgb2", 38," Female", 90.53633251740735, "Street2", "79", "1234AB", "City2", "email2@example.com", "4625758628", "2024-06-12 08:30:11.781341");

SELECT * FROM memberrs
WHERE MembershipID LIKE "%03%";