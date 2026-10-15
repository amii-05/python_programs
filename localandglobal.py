# LOCAL VARIABLE AND GLOBAL VARIABLE

def show():
    message="Hello" #local variable
    print(message)
show()

text="Ami"  #global variable
def greet():
    print("Hello",text)

greet()
print("Hi",text)