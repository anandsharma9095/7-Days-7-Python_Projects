# This is the file which has all the students related operations
# all the functions are listed here
    # student_marks(id)
    # update_father_name(stu_id, new_father_name)
    # update_date_of_birth(stu_id, new_date_of_birth)
    
# functions supposed to be used by teachers
    # update_admission_number(stu_id, admission_number)
    # update_course(stu_id, course_id)
    

import sqlite3
import utils as u



def student_marks(id:int):
    conn = u.db_connection()
    c = conn.cursor()
    
    c.execute('''
              SELECT * FROM marks
              WHERE id = ?
              ''' ,(id,))
    
    marks = c.fetchall()
    conn.close()

    return marks
    
    
def update_father_name( stu_id : int, new_father_name : str):
    conn = u.db_connection()
    c = conn.cursor()
    
    c.execute('''
              UPDATE student
              SET father_name = ?
              WHERE id = ?
              ''' ,(new_father_name,stu_id,))
    
    conn.commit()
    conn.close()
    
def update_date_of_birth(stu_id : int , new_date_of_birth : str):
    conn = u.db_connection()
    c = conn.cursor()
    
    c.execute('''
              UPDATE student
              SET date_of_birth = ?
              WHERE id = ?
              ''' ,(new_date_of_birth,stu_id,))
    
    conn.commit()
    conn.close()
    
    
# Supposed to used by the teachers    

def update_admission_number(stu_id : int, admission_number : str ):
    conn = u.db_connection()
    c = conn.cursor()
    
    c.execute('''
              UPDATE student
              SET admission_number = ?
              WHERE id = ?
              ''' ,(admission_number,stu_id,))
    
    conn.commit()
    conn.close()
    
def update_course(stu_id : int , course_id : int):
    conn = u.db_connection()
    c = conn.cursor()
    
    c.execute('''
              UPDATE student
              SET course_id = ?
              WHERE id = ?
              ''' ,(course_id,stu_id,))
    
    conn.commit()
    conn.close()


