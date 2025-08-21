from cryptography.fernet import Fernet

#This is used to create a fernet key for the encryption
    # def write_key():
    #     key = Fernet.generate_key()
    #     with open('key.key', "wb") as key_file:
    #         key_file.write(key)

    # print('Started Creating......')
    # write_key()
    # print('Done........')

def load_key():
    file = open('key.key', "rb")
    key = file.read()
    file.close()
    return key

key = load_key()
fer = Fernet(key)

def add():
    name = input('User Name : ')
    pwd = input('Password  : ')
    print()
    
    with open('password.txt', 'a') as f:
        f.write(name + '|' + fer.encrypt(pwd.encode()).decode() + "\n")
        
def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user , passw = data.split("|")
            print('------------------------------------')
            print('Username : ', user , '\n' + 'Password : ' , fer.decrypt(passw.encode()).decode() +'\n')
            print('------------------------------------')


while True:
    print('Enter \n(v) - to view password\n(a) - To add password')
    mode = input('(q) - To Quit enter : ').lower()
    print()
    
    if mode == 'q':
        break
    if mode == 'v':
        view()
    elif mode == 'a':
        add()
    else: 
        print()
        print('Invalid mode')
        