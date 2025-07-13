# Criminal Management System

A desktop-based Criminal Record Management System with MySQL database and GUI built using Tkinter.

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
   git clone https://github.com/your-username/CriminalManagementSystem.git
   cd CriminalManagementSystem
2. Install Dependencies:
   ```bash
   pip install -r requirements.txt
3. Configure the database:
   - Create a MySQL database named management.
   - Create required tables (login, criminal).
   - Set your credentials in .env file:
       DB_HOST=localhost
       DB_USER=root
       DB_PASSWORD=yourpassword
       DB_NAME=management
     
4. Run the project:
   ```bash
   python login.py


