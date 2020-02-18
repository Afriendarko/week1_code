# Armstrong number
import numpy as np
num1 = input("Enter the number: ")
numi = int(num1)

l = []
for i in range(len(num1)):
    l.append(int(num1[i]))
    
arr = np.array(l)

arr = arr**3
arm = sum(arr)

if numi == arm:
    print("True")
else:
    print("False")