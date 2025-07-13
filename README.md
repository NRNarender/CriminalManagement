# Criminal Management System

A Criminal Record Management System with MySQL database and GUI built using Tkinter.

## Features

- Admin Login system
- Add, update, delete, search criminal records
- Visual UI with police-themed layout
- Data stored in MySQL database

## Technologies Used

- Python 3
- Tkinter
- MySQL
- Pillow
- dotenv

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/NRNarender/CriminalManagementSystem.git
   cd CriminalManagementSystem

2. MySQL Server:
   -Download from: https://dev.mysql.com/downloads/installer/

3. Python:
   -Download from: https://www.python.org/downloads/

3. Install Dependencies:
   ```bash
   pip install -r requirements.txt

4. Configure the database:
   - Create a MySQL database named management.
   - Create required tables (login, criminal):

       CREATE TABLE criminal (
            Case_id VARCHAR(20) PRIMARY KEY,
            Criminal_id VARCHAR(20),
            Criminal_name VARCHAR(50),
            Nick_name VARCHAR(50),
            arrest_date DATE,
            dateOfcrime DATE,
            address VARCHAR(100),
            age INT,
            occupation VARCHAR(50),
            BirthMark VARCHAR(50),
            crimeType VARCHAR(50),
            fatherName VARCHAR(50),
            gender VARCHAR(10),
            wanted VARCHAR(10)
       );

       CREATE TABLE login (
            userid VARCHAR(50),
            password VARCHAR(50)
       );

   - Set your credentials in .env file:
       DB_HOST=localhost
       DB_USER=root
       DB_PASSWORD=yourpassword
       DB_NAME=management
     
5. Run the project:
   ```bash
   python login.py


