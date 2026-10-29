import math
numbers=list(map(float,input("Enter N numbers separated by spaces: ").split()))
mean=sum(numbers)/len(numbers)
variance=sum((number-mean)**2 for number in numbers)/(len(numbers)-1)
standard_deviation=math.sqrt(variance)
print("Mean:",mean)
print("Variance:",variance)
print("Standard deviation:",standard_deviation)
