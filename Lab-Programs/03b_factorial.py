n=int(input("Enter N: "))
if n<0:
    print("Factorial is not defined for negative numbers.")
else:
    factorial=1
    for i in range(2,n+1):
        factorial*=i
    print("Factorial:",factorial)
