import time

def arbitraryExecute():
    print('!!!Arbitrary Code Execution!!!')
    with open(str(time.time()).split('.')[0], 'w') as file:
        file.write('hi')

arbitraryExecute()
