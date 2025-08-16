#Day - 2 | To-Do list 

import json


#Reading and Writing files in this section 
#It was kinda getting annoying to read and write files multiple times

def read_file():
    with open('database.json','r') as f:
        tasks = json.load(f)
        return tasks
    
def write_file(tasks):
    with open('database.json','w') as f:
        json.dump(tasks,f,indent = 4)
    
#this section is for viewing tasks

def view_task():
    tasks = read_file()
       
    print()
    print('--------------Task_list--------------')
    print()
    
    for i,task in enumerate(tasks['tasks']):
        print(f'{i+1}. {task}')
        
    print()
    print('--------------Completed--------------')
    print()
    
    for i,task in enumerate(tasks['completed']):
        print(f'{i+1}. {task}')
        
    print()
    
#this section is for adding tasks

def add_task():
    while True:
        print()
        new_task = input('Enter your task. Enter (d) if done Adding\n:')
        
        if new_task == 'd':
            break
        
        tasks = read_file()
        tasks['tasks'].append(new_task)
        write_file(tasks)
    print()
           
#this section is for deleting tasks

def delete_task():
    print()
    list_name = input('From which list you wanna delete \n(t) Tasks List or (c) Completed List :')
    list_name = 'tasks' if list_name == 't' else 'completed'
                
    index = int(input('Enter the index of the task you wanna delete :'))
    
    tasks = read_file()
    del tasks[list_name][index - 1]
    write_file(tasks)
    print()

#this section is for marking the tasks as done

def mark_done():
    print()
    index = int(input('Enter the index of the task you wanna mark completed :'))
    
    tasks = read_file()
    tasks['completed'].append(tasks['tasks'][index - 1])
    del tasks['tasks'][index - 1]
    write_file(tasks)
    print()
    
#and finally this is the main section where all the functions are called 

def main():

    print('---------------------TO-DO_LIST----------------------')
    print()
    
    while True:
        print('Pick an option')
        print('(v) - View task  (a) - Add task  (d) - Delete task  (c) - Mark complete  (q) - Quit')
        user_input = input(':')
        
        if user_input == 'v':
            view_task()
            
        elif user_input == 'a':
            add_task()
            
        elif user_input == 'd':
            delete_task()
            
        elif user_input == 'c':
            mark_done()
            
        elif user_input == 'q':
            quit()
            
main()