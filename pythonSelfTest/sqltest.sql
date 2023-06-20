CREATE DATABASE msfbd
-- Customer_Profile table
CREATE TABLE Customer_Profile (
    User_Name VARCHAR(20),
    Email VARCHAR(30),
    Pin INT,
    Contact_Number VARCHAR(11),
    Address VARCHAR(50),
    NID_Number BIGINT(18),
    Date_of_Birth DATE,
    Virtual_ID VARCHAR(30),
    PRIMARY KEY (User_Name)
);

-- Transaction_Records table
CREATE TABLE Transaction_Records (
    Transaction_ID VARCHAR(5),
    Transaction_Amount INT,
    Transaction_Type VARCHAR(10),
    Transaction_Date DATETIME,
    PRIMARY KEY (Transaction_ID)
);

-- Account table
CREATE TABLE Account (
    Account_Number VARCHAR(20),
    Account_Balance INT,
    PRIMARY KEY (Account_Number)
);

-- Performing_Transaction table
CREATE TABLE Performing_Transaction (
    Virtual_ID VARCHAR(30),
    Pin INT,
    Transaction_Amount INT,
    Transaction_Type CHAR(10),
    PRIMARY KEY (Virtual_ID)
);

INSERT INTO Customer_Profile (User_Name, Email, Pin, Contact_Number, Address, NID_Number, Date_of_Birth, Virtual_ID)
VALUES ('JohnDoe', 'johndoe@example.com', 1234, '1234567890', '123 Main Street', 123456789012345678, '1990-01-01', 'virtual123');

INSERT INTO Customer_Profile (User_Name, Email, Pin, Contact_Number, Address, NID_Number, Date_of_Birth, Virtual_ID)
VALUES ('JaneSmith', 'janesmith@example.com', 5678, '9876543210', '456 Elm Street', 987654321098765432, '1995-05-15', 'virtual456');

INSERT INTO Account (Account_Number, Account_Balance)
VALUES ('12345678901234567890', 1000);

INSERT INTO Account (Account_Number, Account_Balance)
VALUES ('98765432109876543210', 500);

INSERT INTO Performing_Transaction (Virtual_ID, Pin, Transaction_Amount, Transaction_Type)
VALUES ('virtual123', 1234, 100, 'Credit');

INSERT INTO Performing_Transaction (Virtual_ID, Pin, Transaction_Amount, Transaction_Type)
VALUES ('virtual456', 5678, 50, 'Debit');



INSERT INTO Transaction_Records (Transaction_ID, Transaction_Amount, Transaction_Type, Transaction_Date)
VALUES ('001', 100, 'Credit', '2023-06-20 10:00:00');

INSERT INTO Transaction_Records (Transaction_ID, Transaction_Amount, Transaction_Type, Transaction_Date)
VALUES ('002', 50, 'Debit', '2023-06-21 15:30:00');



