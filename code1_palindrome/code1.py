# Palindrome number
num = input("Enter the number: ")
rev_num = num[::-1]

if num == rev_num:
    print("True")
else:
    print("False")