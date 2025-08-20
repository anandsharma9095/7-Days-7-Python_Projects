# This file is gonna have all the utilities and functions related to the sqlite DB

# List of all the functions 
    # add_contact
    # add_phone
    # add_email
    # show_all_contacts
    # search_contact_by_name

import sqlite3

# adding data to contact table in db
def add_contact(name: str, birthdate: str = None, address: str = None, notes: str = None, group_id: int = None):
    conn = sqlite3.connect('database.db')
    conn.execute("PRAGMA foreign_keys = ON;")   # have to enforce foreign keys idk why
    cursor = conn.cursor()
    
    cursor.execute(
        "INSERT INTO contacts (name, birthdate, address, notes, group_id) VALUES (?, ?, ?, ?, ?)",
        (name, birthdate, address, notes, group_id)
    )
    
    Contact_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return Contact_id

# adding data to contact table in db

def add_phone(contact_id: int, phone: str, type: str = None):
    conn = sqlite3.connect('database.db')
    conn.execute("PRAGMA foreign_keys = ON;")   # have to enforce foreign keys idk why
    cursor = conn.cursor()
    
    cursor.execute(
        "INSERT INTO phones (contact_id, phone, type) VALUES (?, ?, ?)",
        (contact_id, phone, type)
    )
    
    conn.commit()
    conn.close()

# adding data to email table in db

def add_email(contact_id: int, email: str, type: str = None):
    conn = sqlite3.connect('database.db')
    conn.execute("PRAGMA foreign_keys = ON;")  # have to enforce foreign keys idk why
    cursor = conn.cursor()
    
    cursor.execute(
        "INSERT INTO emails (contact_id, email, type) VALUES (?, ?, ?)",
        (contact_id, email, type)
    )
    
    conn.commit()
    conn.close()
    
# to send all the data from all the tables 
def show_all_contacts():
    conn = sqlite3.connect('database.db')
    conn.execute("PRAGMA foreign_keys = ON;")   # have to enforce foreign keys idk why
    cursor = conn.cursor()

    # Getting all contacts
    cursor.execute("""
        SELECT rowid, name, birthdate, address, notes, group_id
        FROM contacts
    """)
    contacts = cursor.fetchall()

    results = []

    for contact in contacts:
        contact_id = contact[0]

        # getting phone number
        cursor.execute("SELECT phone, type FROM phones WHERE contact_id = ?", (contact_id,))
        phones = cursor.fetchall()

        # getting email address
        cursor.execute("SELECT email, type FROM emails WHERE contact_id = ?", (contact_id,))
        emails = cursor.fetchall()

        # Appending dict
        results.append({
            "id": contact_id,
            "name": contact[1],
            "birthdate": contact[2],
            "address": contact[3],
            "notes": contact[4],
            "group_id": contact[5],
            "phones": phones,
            "emails": emails
        })

    conn.close()
    return results

# this is  a cool one searching contacts by their name 
# even if you type partial name it will get the result

def search_contact_by_name(name: str):
    conn = sqlite3.connect('database.db')
    conn.execute("PRAGMA foreign_keys = ON;")   # have to enforce foreign keys idk why
    cursor = conn.cursor()

    # First find matching contacts
    cursor.execute("""
        SELECT rowid, name, birthdate, address, notes, group_id
        FROM contacts
        WHERE name LIKE ?
    """, ('%' + name + '%',))
    contacts = cursor.fetchall()

    results = []

    for contact in contacts:
        contact_id = contact[0]

        # Get phone number for this contact
        cursor.execute("SELECT phone, type FROM phones WHERE contact_id = ?", (contact_id,))
        phones = cursor.fetchall()

        # Get email address for this contact
        cursor.execute("SELECT email, type FROM emails WHERE contact_id = ?", (contact_id,))
        emails = cursor.fetchall()

        # adding all the data in dict and returning it easier to read 
        results.append({
            "id": contact_id,
            "name": contact[1],
            "birthdate": contact[2],
            "address": contact[3],
            "notes": contact[4],
            "group_id": contact[5],
            "phones": phones,
            "emails": emails
        })

    conn.close()
    return results

# to get all the groups hardcoded into the db
def get_groups():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT rowid, group_name FROM groups")
    groups = cursor.fetchall()
    conn.close()
    return groups


# this is for adding group functionality in the end i droped the idea of adding the group 
# i just hardcoded the groups into db

# def add_group(group_name: str):
#     conn = sqlite3.connect('database.db')
#     conn.execute("PRAGMA foreign_keys = ON;")  # have to enforce foreign keys idk why
#     cursor = conn.cursor()
    
#     cursor.execute("INSERT INTO groups (group_name) VALUES (?)", (group_name,))
    
#     group_id = cursor.lastrowid
#     conn.commit()
#     conn.close()
#     return group_id

