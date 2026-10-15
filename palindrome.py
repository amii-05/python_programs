
word=input("Enter the word: ").lower()
if word==word[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")