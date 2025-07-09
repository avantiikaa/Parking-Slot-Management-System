
# Parking Slot Management System

This project is a simple Python Tkinter + SQLite3 Parking Slot Management System.

## Features
- Admin login
- Add vehicle record
- View vehicle history
- Persistent storage in SQLite database

## Requirements
- Python 3
- tkinter (comes pre-installed)
- sqlite3 (comes pre-installed)

## Setup

1. Clone/download the project folder.
2. Install dependencies (if needed):

pip install pillow

(Only required if you want to display images.)
3. Initialize the database:
```python
from database import create_tables
create_tables()

4. Run the app:

python main.py
Default Admin Credentials
Username: admin

Password: password

Files
database.py: Database creation and operations

main.py: Tkinter application

README.md: Project instructions

Author
Developed as part of a mini-project for Parking Slot Management.
