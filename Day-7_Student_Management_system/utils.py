# this file is gonna have all the database related queries 
# Getting data by their id's

# all the functions listed here
    # db_connection
    # search_by_name(person,string)
    # update_name(person,new_first_name,new_last_name)
    # update_phone_number(person,id,phone_number)
    # update_email(person,id,email)
    
        
import sqlite3
    

def course_id_course(course_id : int):
    conn = db_connection()
    c = conn.cursor()
    
    c.execute('SELECT name FROM course WHERE id = ?',(course_id,))
    course = c.fetchall()
    conn.close()
    return course[0][0]

def teacher_subject(teacher_id : int):
    conn = db_connection()
    c = conn.cursor()
    
    c.execute('SELECT name FROM subject WHERE teacher_id = ?',(teacher_id,))
    subject = c.fetchall()
    conn.close()
    return subject[0][0]

def db_connection():
    conn = sqlite3.connect('database.db')
    conn.execute('PRAGMA foreign_keys = ON')
    return conn
    
def search_by_name(person:str, name : str):
    conn = db_connection()
    c = conn.cursor()
    
    c.execute(f'''
              SELECT * FROM {person}
              WHERE first_name LIKE ?
              ''' ,('%' + name + '%',))
    
    data = c.fetchall()
    conn.close()
    
    return data
    
def update_name(person:str, id:int, new_first_name:str, new_last_name:str):
    conn = db_connection()
    c = conn.cursor()
    
    c.execute(f'''
              UPDATE {person}
              SET first_name = ?, last_name = ?
              WHERE id = ?
              ''' ,(new_first_name,new_last_name,id,))
    
    conn.commit()
    conn.close()
    
def update_phone_number(person:str, id : int, phone_number : str ):
    conn = db_connection()
    c = conn.cursor()
    
    c.execute(f'''
              UPDATE {person}
              SET phone_number = ?
              WHERE id = ?
              ''' ,(phone_number,id,))
    
    conn.commit()
    conn.close()
    
def update_email(person:str, id : int, new_email : str ):
    conn = db_connection()
    c = conn.cursor()
    
    c.execute(f'''
              UPDATE {person}
              SET email = ?
              WHERE id = ?
              ''' ,(new_email,id,))
    
    conn.commit()
    conn.close()
    
    

    
    