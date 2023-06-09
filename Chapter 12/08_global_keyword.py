a = 54 #global variable
def func1():
    global a
    print(f'Print Statement 1: {a}')
    a = 8 #Local variabale if global keyword is not used
    print(f'Print Statement 2: {a}')

func1()
print(f'Print Statement 3: {a}')  