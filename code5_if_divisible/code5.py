# Check number is divisible by ____

number = int(input("Enter the number: "))

if number in range(1,1000):
    if number%3==0 and number%5==0:
        print("ConsultaddTraining")
    elif number%3==0:
        print("Consultadd")
    elif number%5==0:
        print("Training")