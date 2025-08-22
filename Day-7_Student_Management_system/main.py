
import students as s
import utils as u

def student_operations():
    person = 'student'
    user_name = input('Enter First name : ').capitalize()
    
    data = u.search_by_name(person,user_name)

    # [(1, 'Ram', 'Jha', 'Shiva Jha', '11/12/2004', '111111', '9988776655', 'ram@jha.com', 1)] - data example
    
    student_id = data[0][0]
    course_id = data[0][8]
    course = u.course_id_course(course_id)
    
    print()
    print('------------Student Credentials--------------')
    print()
    print('Name : '+ data[0][1] +' '+  data[0][2])
    print('Father Name : ' + data[0][3])
    print('Date Of Birth : ' + data[0][4])
    print('Admission Number : ' + data[0][5])
    print('Phone Number : ' + data[0][6])
    print('Email Address : ' + data[0][7])
    print('Course : ',course)
    print()
    
    user_input = input('Would You Like to (u) - Update Credentials (q) - Quit: ')

    if user_input == 'u':
        print()
        print('What would you like to update ?')
        user_input = input('(n) - Name (f) - Father Name(d) - Date of Birth  \n(p) - Phone Number (e) - Email (q) - Quit : ')
        print()
        
        if user_input == 'n':
            new_first_name = input('Enter New First Name : ')
            new_last_name = input('Enter New Last Name : ')
            
            u.update_name(person,student_id, new_first_name, new_last_name)
            print(f'Name Has been Updated from {data[0][1] +' '+  data[0][2]} to {new_first_name} {new_last_name}')
            
        elif user_input == 'f':
            new_father_name = input('Enter New Father\'s Name : ')
            
            s.update_father_name(student_id,new_father_name)
            print(f'Father\'s Name Has been Updated from {data[0][3]} to {new_father_name}')
            
        elif user_input == 'd':
            print('dd/mm/yyyy')
            new_date_of_birth = input('Enter Correct Date Of Birth : ')
            
            s.update_date_of_birth(student_id,new_date_of_birth)
            print(f'Date of Birth Has been Updated from {data[0][4]} to {new_date_of_birth}')

        elif user_input == 'p':
            new_phone_number = input('Enter New Phone Number : ')
            
            u.update_phone_number(person,student_id,new_phone_number)
            print(f'Phone Number Has Been Updated From {data[0][6]} to {new_phone_number}')
            
        elif user_input == 'e':
            new_email = input('Enter New Email Address : ')
            
            u.update_email(person, student_id, new_email)
        
        elif user_input == 'q':
            return
        
    elif user_input == 'q':
        quit()
        
    else:
        print('Enter a Valid Answer')

while True:
    print()
    print('----------STUDENT MANAGEMENT------------')
    print()

    user = input('Are you a (t) - teacher or a (s) - student : ').lower()
    if user == 't':
        person = 'teacher'
        user_name = input('Enter your name : ').capitalize()
        
        while True:
            data = u.search_by_name(person,user_name)
            
            # [(1, 'Ravi', 'kumar', '9876543210', 'ravi@kumar.com')] - data example
            teacher_id = data[0][0]
            subject = u.teacher_subject(teacher_id)
            print()
            print('------------Your Credentials--------------')
            print()
            print('Name : '+ data[0][1] +' '+ data[0][2])
            print('Phone Number : '+ data[0][3])
            print('Email Address : '+ data[0][4])
            print('Subject : ',subject)
            print()
            
            user_input = input('Would You Like to (v) - View Student Details (q) - Quit: ')
            
            if user_input == 'v':
                student_operations()

            elif user_input == 'q':
                quit()
            else:
                print('Enter a valid option')
            
        
    elif user == 's':
       student_operations()
        
    elif user == 'q':
        quit()
        
    else : 
        print()
        print('Enter a Valid option ')

