# Sum of array without using predefined functions

li = [] 
cosum = 0
rang = int(input("limit of array: "))

for i in range(rang):
    linp = int(input())
    if linp in li:
        continue
    li.append(linp)
    
for i in range(len(li)):
    cosum = cosum + li[i]
    
print(cosum)