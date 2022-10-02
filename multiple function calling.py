def func1():
    print(1)
    
    
def func2():
    print(2)
    

def func3():
    print(3)
    
def func4():
    print(4)
    
#using a dictionary to call functions from a users input, for 3.9 and below
    
functions = {"func1" : func1,"func2" : func2,"func3" : func3,"func4" : func4}

func = str(input("enter your fuction> "))

function = functions.get(func)

function()

