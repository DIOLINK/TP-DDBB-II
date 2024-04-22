# Ecommerce Project with Django, MySQL, and React

This project is a full-stack ecommerce solution built using Django for the backend, MySQL for the database, and React for the frontend. It provides a robust and scalable platform for managing products, processing transactions, and delivering a modern user experience.

## Database Schema

Below is the SQL script for creating the database tables:

```sql
-- Users table
CREATE TABLE IF NOT EXISTS Users (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    First_Name VARCHAR(50) NULL,
    Last_Name VARCHAR(50) NULL,
    Email VARCHAR(100) NULL,
    Password VARCHAR(100) NULL,
    Address VARCHAR(255) NULL,
    City VARCHAR(100) NULL,
    Country VARCHAR(100) NULL,
    Phone VARCHAR(20) NULL,
    Registration_Date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Courses table
CREATE TABLE IF NOT EXISTS Courses (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Course_Name VARCHAR(100) NULL,
    Description TEXT NULL,
    Price DECIMAL(10, 2) NULL,
    Duration INT NULL,
    Difficulty_Level VARCHAR(50) NULL,
    Category VARCHAR(50) NULL
);

-- Purchases table
CREATE TABLE IF NOT EXISTS Purchases (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    User_ID INT NOT NULL,
    Course_ID INT NOT NULL,
    Purchase_Date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    Payment_Method VARCHAR(50) NULL,
    Purchase_Status VARCHAR(50) NULL,
    FOREIGN KEY (User_ID) REFERENCES Users(ID),
    FOREIGN KEY (Course_ID) REFERENCES Courses(ID)
);

-- Transactions table
CREATE TABLE IF NOT EXISTS Transactions (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Purchase_ID INT NOT NULL,
    Amount DECIMAL(10, 2) NULL,
    Transaction_Date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    Details TEXT NULL,
    FOREIGN KEY (Purchase_ID) REFERENCES Purchases(ID)
);

-- Shopping Cart table
CREATE TABLE IF NOT EXISTS Shopping_Cart (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    User_ID INT NOT NULL,
    Course_ID INT NOT NULL,
    Quantity INT NULL,
    Unit_Price DECIMAL(10, 2) NULL,
    FOREIGN KEY (User_ID) REFERENCES Users(ID),
    FOREIGN KEY (Course_ID) REFERENCES Courses(ID)
);


![img]("./assets/TP-DDBB-II.png")
