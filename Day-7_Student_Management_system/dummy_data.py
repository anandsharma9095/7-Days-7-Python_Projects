
import sqlite3

def insert_default_course():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    default_courses = ["MPC", "BiPC", "CEC","MEC", "HEC"]

    for course in default_courses:
        try:
            cursor.execute("INSERT INTO course (name) VALUES (?)", (course,))
        except sqlite3.IntegrityError:
            pass
        
    conn.commit()
    conn.close()
    
    print("Default Courses inserted (if not already present).")
    

def insert_default_teacher():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    default_teacher = [
        ('Ravi','kumar','9876543210','ravi@kumar.com'),
        ('Jyothi','Shastri','9999999999','jyothi@shastri.com'),
        ('krishna','chand','8888888888','krishna@chand.com'),
        ('Naresh','kumar','7777777777','naresh@kumar.com'),
        ('Kiran','Devi','6666666666','ravi@kumar.com'),
        ('swathi','bannerjii','9878787898','swathi@banerjii.com'),
        ('Sultan','Ail','9919191919','sultan@ali.com'),
        ('Abhishek','Trivedi','9871234650','abhishek@trivedi.com')
    ]

    for teacher in default_teacher:
        try:
            cursor.execute("INSERT INTO teacher (first_name, last_name, phone_number, email) VALUES (?,?,?,?)", teacher)
        except sqlite3.IntegrityError:
            pass
        
    conn.commit()
    conn.close()
    
    print("Default teachers inserted (if not already present).")
    


def insert_default_subject():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    default_subject = [
        ('English',1),
        ('Physics',2),
        ('Maths',3),
        ('Economics',4),
        ('Commerce',5),
        ('Chemistry',6),
        ('Civics',7),
        ('History',8)
    ]

    for subject in default_subject:
        try:
            cursor.execute("INSERT INTO subject (name,teacher_id) VALUES (?,?)", subject)
        except sqlite3.IntegrityError:
            pass
        
    conn.commit()
    conn.close()
    print("Default teachers inserted (if not already present).")
    
def insert_default_student():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    default_student = [
        ('Ram','Jha','Shiva Jha','11/12/2004','111111','9988776655','ram@jha.com',1),
        ('Shyam','Trivedi','Manish Trivedi','10/11/2004','222222','9911223344','shyam@trivedi.com',2),
        ('Shiva','Chaturvedi','Manoj Chaturvedi','12/06/2005','333333','8899776655','shiva@charturvedi.com',4),
        ('Radhe','Shyam','Akash Shyam','14/01/2004','444444','6611223344','radhe@shyam.com',2),
        ('Satyam','Sharma','Praveen Sharma','17/04/2004','555555','7788113355','satyam@sharma.com',2),
        ('Ayush','Banerjee','Ankit Banerjee','13/06/2004','666666','9977336611','aayush@banerjee.com',3),
        ('Avinash','Kumar','Rishi Kumar','09/10/2003','777777','7711990033','avinash@kumar.com',3),
        ('Tina','Shastri','Harish Shastri','19/03/2004','888888','7733115522','tina@shastri.com',5),
        ('Manisha','Mishra','Ramesh Mishra','01/09/2002','99999','9088776655','manish@mishra.com',1),
        ('Kirti','Mistry','Suresh Mistry','15/07/2004','000000','6655223344','kirti@mistry.com',5)
  
    ]

    for student in default_student:
        try:
            cursor.execute("INSERT INTO student (first_name, last_name, father_name , date_of_birth, admission_number,phone_number,email,course_id) VALUES (?,?,?,?,?,?,?,?)", student)
        except sqlite3.IntegrityError:
            pass
        
    conn.commit()
    conn.close()
    
    print("Default students inserted (if not already present).")
    
    


insert_default_course()
insert_default_teacher()
insert_default_subject()
insert_default_student()

