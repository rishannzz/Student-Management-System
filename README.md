🎓 Student Management System
A robust, modular Command Line Interface (CLI) application built with Python and MySQL. This system allows users to seamlessly perform CRUD (Create, Read, Update, Delete) operations on student records, demonstrating core database integration and software architecture principles.

✨ Features
Add Students: Register new students with their name, email, and enrolled course.

View Records: Display a formatted table of all students currently in the system.

Update Courses: Modify a student's enrolled course using their unique Student ID.

Delete Records: Remove students from the database securely.

Data Persistence: All information is stored permanently using a MySQL backend.

🛠️ Technologies Used
Python 3.x: Core application logic and user interface.

MySQL: Relational database management system.

mysql-connector-python: Driver to bridge the Python application and MySQL server.

📂 Project Structure
Plaintext
student-management-system/
│
├── db_config.py             # Handles secure MySQL database connection
├── student_operations.py    # Contains all CRUD backend logic (SQL queries)
├── main.py                  # CLI user interface and application entry point
├── setup.sql                # Database schema creation script
└── README.md                # Project documentation
