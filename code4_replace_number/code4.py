# Replace vovels
string = input("Enter the string: ")
character = input("Enter the character: ")

l = ['a', 'e', 'i', 'o', 'u']

for i in string.lower():
    if i in l:
        string = string.replace(i, character)
print(string)