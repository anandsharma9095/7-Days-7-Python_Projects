#Day-3 | Expense Tracker

import csv

#this section is to add the expenses in the list
def add_expense():
    print()
    print('Enter the Expense you wanna add')
    print()
    
    print('dd/mm/yyyy')
    date = input('Date     : ')
    
    print('(f)Food, (t)Travel, (c)Clothing, (s)Shopping, (d)Donations, (m)Miscellaneous')    
    category = input('Category : ').lower()
    
    if category == 'f':
        category = 'food'
    elif category == 't':
        category = 'travel'
    elif category == 'c':
        category = 'clothing'
    elif category == 's':
        category = 'shopping'
    elif category == 'd':
        category = 'donations'
    elif category == 'm':
        category = 'miscellaneous'
    else :
        category = category
        
    while True:
        amount = input('amount   : ')
        if amount.isdigit():
            break
        else:
            print('Enter a valid amount without spaces')
        
    note = input('Note     : ')
        
    with open('expenses.csv','a',newline= "") as f:
        data = csv.writer(f)
        data.writerow([date,category,amount,note])
        
#this section is to view the data from the csv file
    
def view_expense():
    print()
    print('-----------Expenses-----------')
    print()
    
    with open('expenses.csv','r') as f:
        data = csv.reader(f)
        for row in data:
            print(f'Date : {row[0]} \nCategory : {row[1]}\nAmount : {row[2]}\nNote : {row[3]}')
            print()
        
#this section is to summarize all the data from the csv file
        
def summarize():
    with open('expenses.csv','r') as f:
            data = csv.reader(f)
            
            total_category = {
                'food' : 0,
                'travel' : 0,
                'clothing' : 0,
                'shopping' : 0,
                'donations' : 0,
                'miscellaneous' : 0,
                'total' : 0,
                'max_spend' : 0
            }

            for row in data:         #basically saying it to add all the amounts in different categories
                if row[1] == 'food': # row[1] is talking about categories
                    total_category['food'] += int(row[2])    #the data was in string format had to parse it in string
                elif row[1] == 'travel':
                    total_category['travel'] += int(row[2]) #row[2] is talking about amount
                elif row[1] == 'clothing':
                    total_category['clothing'] += int(row[2])
                elif row[1] == 'shopping':
                    total_category['shopping'] += int(row[2])
                elif row[1] == 'donations':
                    total_category['donations'] += int(row[2])
                else:
                    total_category['miscellaneous'] += int(row[2])
                
                total_category['total'] += int(row[2])
                total_category['max_spend'] = max(int(row[2]),total_category['max_spend']) #once again it was string had to convert it to int 
                
            print()
            print(f' Food Expenses : {total_category['food']}')
            print(f' Travel Expenses : {total_category['travel']}')
            print(f' Clothing Expenses : {total_category['clothing']}')
            print(f' Shopping Expenses : {total_category['shopping']}')
            print(f' Donations Expenses : {total_category['donations']}')
            print(f' Miscellaneous Expenses : {total_category['miscellaneous']}')
            print()
            print(f' Total Expenses : {total_category['total']}')
            print()
            print(f'Highest Spend till now is : {total_category['max_spend']}')
            print()
                
def main():
    print()
    print('------------------Expense_Tracker------------------')
    
    while True:
        print()    
        print('Pick an option')
        user_input = input('(a) - Add Expense   (v) - View expense   \n(s) - Summarize expenses   (q) - Quit \n:')
        user_input = user_input.lower()
        
        if user_input == 'a':
            add_expense()
        elif user_input == 'v':
            view_expense()
        elif user_input == 's':
            summarize()
        elif user_input == 'q':
            quit()
        else:
            print('Enter a valid option and without spaces')
    
main()