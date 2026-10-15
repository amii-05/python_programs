#DICTIONARY (MUTABLE COLLECTION OF KEY VALUE PAIRS, KEY UNIQUE AND VALUES WILL BE REPEAT)

student_1={
    "Name":"Amirtha",
    "age":20,
    "Mark":430,
    "Department":"CSE"
    }
print(student_1)
print(student_1["Name"])
print(student_1["Mark"])
print(student_1["City"])
print(student_1.get("age"))
print(student_1.get("City","Not available"))
student_1["Mark"]=499
print(student_1)
student_1["City"]="Pondy"
print(student_1)
student_1.pop("age")
print(student_1)

for key,value in student_1.items():
    print(key," :",value)
    
#task2

product_name={
    "name":"keyboard",
    "price":500,
    "stock":10
    }
print(product_name)
product_name["price"]=650
print(product_name)
product_name["brand"]="Logitech"
print(product_name)

for key,value in product_name.items():
    print(key," :",value)