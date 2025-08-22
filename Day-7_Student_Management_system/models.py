# This is the file with which i created the database for the student management system

# RUN THIS IF THERE IS NO DATABASE CREATED BEFORE OR YOU DELETE THE DATABASE BEFORE RUNNING

import sqlite3

conn = sqlite3.connect('database.db')
conn.execute('PRAGMA foreign_keys = ON;')

c = conn.cursor()


c.execute('''
          CREATE TABLE IF NOT EXISTS course(
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              name TEXT NOT NULL
          )
          ''')

c.execute('''
         CREATE TABLE IF NOT EXISTS teacher(
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             first_name TEXT NOT NULL,
             last_name TEXT NOT NULL,
             phone_number TEXT NOT NULL UNIQUE,
             email TEXT
         )
         ''')

c.execute('''
          CREATE TABLE IF NOT EXISTS subject(
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              name TEXT NOT NULL,
              teacher_id INTEGER,
              FOREIGN KEY (teacher_id) REFERENCES teacher(id) ON DELETE SET NULL
          )
          ''')
c.execute('''
          CREATE TABLE IF NOT EXISTS student(
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              first_name TEXT NOT NULL,
              last_name TEXT NOT NULL,
              father_name TEXT,
              date_of_birth TEXT NOT NULL,
              admission_number TEXT NOT NULL,
              phone_number TEXT NOT NULL UNIQUE,
              email TEXT UNIQUE,
              course_id INTEGER,
              FOREIGN KEY (course_id) REFERENCES course(id) ON DELETE SET NULL
          )
          ''')


c.execute('''
          CREATE TABLE IF NOT EXISTS marks(
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              marks INTEGER NOT NULL CHECK(mark >= 0 AND mark <= 100),
              exam_name TEXT NOT NULL,
              subject_id INTEGER ,
              student_id INTEGER ,
              FOREIGN KEY (subject_id) REFERENCES subject(id) ON DELETE SET NULL,
              FOREIGN KEY (student_id) REFERENCES student(id) ON DELETE CASCADE
          )
          ''')
c.execute('''
          CREATE TABLE IF NOT EXISTS course_subject(
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              subject_id INTEGER,
              course_id INTEGER,
              FOREIGN KEY (subject_id) REFERENCES subject(id) ON DELETE CASCADE,
              FOREIGN KEY (course_id) REFERENCES course(id) ON DELETE CASCADE
              )''')

conn.commit()
conn.close()
print("Database and tables created successfully!")
