import databse_utilities as db

# List of all the functions imported from the db
    # add_contact
    # add_phone
    # add_email
    # show_all_contacts
    # search_contact_by_name
    # get_groups
    
def main():
    
    while True:
        print()
        print('----------Contacts Manager-----------')
        print()
        
        print('(v) - View all Contacts\n(s) - Search Contact By Name\n(a) - Add Contact)\n(q) - Quit')
        user_input = input(':')
        
        if user_input == 'v':         
            contacts = db.show_all_contacts()
            
            # getting the data in the form of dictionary so had to use for loop
            
            for c in contacts:
                print()
                print(f"Name: {c['name']}")
                print(f"Birthdate: {c['birthdate']}")
                print(f"Address: {c['address']}")
                print(f"Notes: {c['notes']}")
                print("Phones:")
                
                for phone, ptype in c["phones"]:
                    print(f"  {phone} ({ptype})")
                    
                print("Emails:")
                
                for email, etype in c["emails"]:
                    print(f"  {email} ({etype})")
                print("-" * 20)
                    
        elif user_input == 's':
            print()
            user_input = input('Enter the Name you wanna search : ')
                    
            contacts = db.search_contact_by_name(user_input)
            for c in contacts:
                print()
                print(f"Name: {c['name']}")
                print(f"Birthdate: {c['birthdate']}")
                print(f"Address: {c['address']}")
                print(f"Notes: {c['notes']}")
                print("Phones:")
                for phone, ptype in c["phones"]:
                    print(f"  {phone} ({ptype})")
                print("Emails:")
                for email, etype in c["emails"]:
                    print(f"  {email} ({etype})")
                print("-" * 20)
                    
        elif user_input == 'a':
            
            print()
            print('Enter the group you wanna add your contact to \n')
            
            groups = db.get_groups()
            print("Available Groups:")
            for gid, gname in groups:
                print(f"({gid}) - {gname}")

            group_id = int(input("Enter Group ID: "))

            print('Enter Details')
            name = input('Name : ')
            birthdate = input('Birth Date : ')
            address = input('Address : ')
            notes = input('Note : ')
            
            contact_id = db.add_contact(name, birthdate, address, notes, group_id)
            
            while True:
                print()
                print('Enter (q) When done adding all the numbers')
                phone = input('Phone Number : ')
                if phone == 'q':
                    break
                phone_type = input('Phone Number Desc : ')   
                db.add_phone(contact_id,phone,phone_type) 

            while True:
                print()
                print('Enter (q) When done adding all the Email')
                email = input('Email : ')
                if email == 'q':
                    break
                email_type = input('Email Desc : ')
                db.add_email(contact_id,email,email_type)  
                
        elif user_input == 'q':
            quit()
        else:
            print('Invalid.........')
            print('Enter The values from the brackets')                 
main()
