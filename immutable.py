# IMMUTABLE COLLECTIONS OF CHARACTER

name="Arun"
course='python'
print(name)
print(course)
print(type(name))
print(type(course))
print(course[0])
print(course[1])
print(course[-1])

print(course[0:3])       #pyt
print(course[2:1])       #thon
print(course[0:4])       #pyth
print(course[::-1])      #nohtyp

text="python"
text="J"+text[1:]
print(text)

print(len(text))

for value in text:
    print(value,end=" ")
print()

text_1="Hello Python"
print(text_1.upper())
print(text_1.lower())
print(text_1.replace("Python","Java"))
print(text_1)
print(text_1.count("o"))
print(text_1.find("Python"))
print(text_1.find("Java"))
print(text_1.startswith("Hello"))
print(text_1.endswith("Python"))

text_2="        AMIRTHA ESWARI      "
print(text_2.strip())

text_3="c c++ Java Python"
print(text_3)
courses=text_3.split()
print(courses)

text_4=["C","C++","Java","Pyhton"]
text_5=",".join(text_4)
print(text_5)


