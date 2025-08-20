# this file is to create database for the contacts manager app


#ONLY RUN THIS FILE IF YOU WANT TO CREATE A DATABASE

import sqlite3

def create_tables():
    conn = sqlite3.connect("database.db")
    conn.execute("PRAGMA foreign_keys = ON;") # have to enforce foreign keys idk why
    
    cursor = conn.cursor()

    # creating groups table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS groups (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        group_name TEXT NOT NULL UNIQUE
    )
    """)

    # creating contacts table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS contacts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        birthdate TEXT,
        address TEXT,
        notes TEXT,
        group_id INTEGER,
        FOREIGN KEY (group_id) REFERENCES groups(id) ON DELETE SET NULL
    )
    """)

    # creating phones table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS phones (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        contact_id INTEGER NOT NULL,
        phone TEXT NOT NULL,
        type TEXT,
        FOREIGN KEY (contact_id) REFERENCES contacts(id) ON DELETE CASCADE
    )
    """)

    # creating emails table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS emails (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        contact_id INTEGER NOT NULL,
        email TEXT NOT NULL,
        type TEXT,
        FOREIGN KEY (contact_id) REFERENCES contacts(id) ON DELETE CASCADE
    )
    """)

    conn.commit()
    conn.close()
    print("Database and tables created successfully!")

# wanted to add an add group functionality but ended up dropping it and just hard coded the data manually 

def insert_default_groups():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    default_groups = ["Family", "Friends", "Work"]

    for group in default_groups:
        try:
            cursor.execute("INSERT INTO groups (group_name) VALUES (?)", (group,))
        except sqlite3.IntegrityError:
            pass

    conn.commit()
    conn.close()
    print("Default groups inserted (if not already present).")


# recently learned these dunder functions and these are very cool so thought of using this here. why?. just for fun
if __name__ == "__main__":
    create_tables()
    insert_default_groups()
