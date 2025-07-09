import sqlite3

def create_tables():
    conn = sqlite3.connect("parking.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS vehicles (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        mobile TEXT,
        vehicle_no TEXT,
        vehicle_type TEXT,
        entry_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)
    conn.commit()
    conn.close()

def insert_vehicle(name, mobile, vehicle_no, vehicle_type):
    conn = sqlite3.connect("parking.db")
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO vehicles (name, mobile, vehicle_no, vehicle_type)
    VALUES (?, ?, ?, ?)
    """, (name, mobile, vehicle_no, vehicle_type))
    conn.commit()
    conn.close()

def fetch_vehicles():
    conn = sqlite3.connect("parking.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM vehicles")
    rows = cursor.fetchall()
    conn.close()
    return rows
