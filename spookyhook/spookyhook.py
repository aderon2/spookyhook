import time
import getpass

def arbitraryExecute():
    print('!!!Arbitrary Code Execution!!!')
    with open(str(time.time()).split('.')[0], 'w') as file:
        file.write('File Created By User: ')
        try:
            file.write(getpass.getuser())
        except:
            file.write('Unable to determine user')

arbitraryExecute()
