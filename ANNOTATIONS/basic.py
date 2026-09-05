"""it a good practice in programming type annotations"""

def calculate(a :int,b:int)->int :
    return a+b

a=9
b=90
print(calculate(a,b))

def greet(sms:str)->str:
    return (f"good morning,{sms}")

name="jitu debnath"
print(greet(name))


