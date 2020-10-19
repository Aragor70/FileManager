import time
import subprocess

# get users

users = []
user = {}

control = {
    'isAuthenticated': False
}


collection = []



def getValue(task):
    value = input(task)

    return value

def showFiles():
    if len(collection) > 0:
        print('File collection: \n')
        for i in collection:
            print(f'{collection.index(i)}. {i}')
            time.sleep(1.5)
    else:
        print("""
            You do not have any files. 
        """)
        time.sleep(1.5)

def register():
    auth = {
        'name': getValue('Enter your name: '),
        'email': getValue('Enter your e-mail: '),
        'password': getValue('Enter your password: '),
        'repPassword': getValue('Enter your password again: ')
    }
    if auth['password'] != auth['repPassword']:
        print('Password are not equal. Please try again.')
        

    user = {
        'name': auth['name'],
        'email': auth['email'],
        'password': auth['password'],
    }
    users.append(user)

while len(user) < 1 or control['isAuthenticated'] == False:

    print('Create new account or log in.')
    print(""" 
        Press 1 - log in
        Press 2 - create account
        Press q - quit
    """)

    value = getValue('')
    if value == "1":
        def login():
            print('Log in:')
        
            login = {
                'email': getValue('Enter your e-mail: '),
                'password': getValue('Enter your password: '),
            }
            
            for i in users:
                if i['email'] == login['email'] and i['password'] == login['password']:
                    
                    print(f'Login successful.')
                    
                    user.update(i)
                    
                    control['isAuthenticated'] = True
                    
                    break

        login()

        if not control['isAuthenticated']:
            print(""" 
                Invalid credentials. Please try again. 
            """)

            time.sleep(1.5)
        
    elif value == "2":
        
            
        register()


    elif value == "q":

        break
    else:
        print('Select one please.')

if not control['isAuthenticated']:
    print('See you next time.')
else:
    print(f'Hello from inside. {user}')


    while control['isAuthenticated'] == True:
        print('Press 1 - show file')
        print('Press 2 - open files')
        print('Press 3 - add new file')
        print('Press 4 - modify your collection')
        print('Press q - quit')

        select = getValue('')

        if select == "1":
                                                    # show files
            
            showFiles()

        elif select == "2":
                                                    # open file
            def openFile(directiory):
                subprocess.call(directiory)

                print("""
                    Program exit. 
                """)
                time.sleep(1.5)
            
            showFiles()
            if len(collection) > 0:
                print('Enter file directory')
                print('Press q - quit')

                choice = getValue('')
                if choice == "q":
                    break 
                else:
                    if choice in collection:
                        openFile(choice)
                    else:
                        print('Wrong file directory.')

            
        elif select == "3":
                                                    # add file
            def addFile(arry):
                print('Add new file.')
                
                newCollection = getValue('Enter filePath: ')

                collection.append(newCollection)

                print(collection)

                time.sleep(1.5)
                
            addFile(collection)
            
        elif select == "4":
                                                    # modify file collection
            print('Modyfy your collection')
            print('Press 1 - remove file / files')
            modifyValue = getValue('')
            if modifyValue == "1":
                showFiles()
                def removeFile(index):
                    collection.pop(index)

                    print("""
                        File deleted successful.
                    """)
                    time.sleep(1.5)

                if len(collection) > 0:
                    print('Enter the number to remove file.')
                    removeIndex = getValue('')
                    for i in range(len(collection)):
                        if removeIndex == str(i):
                            removeFile(int(removeIndex))
                        elif removeIndex == 'q':
                            break
                        else:
                            print('Wrong number.')

            elif modifyValue == "q":
                break
            else:
                print('Select one please.')

        elif select == "q":
            break

        else:
            print('Select one please.')
        