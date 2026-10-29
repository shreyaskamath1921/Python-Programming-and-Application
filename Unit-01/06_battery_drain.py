battery=100
minutes=0
while battery > 20:
    battery -= 7
    minutes += 1
print(f"Low battery alert {minutes} minutes ({battery})%")

#--------------------------------------------------------------------------------------------------------------

battery=100
minutes=0
while battery>20:
    battery -= 7
    minutes += 1
    print(f"minute {minutes:2d} -> battery {battery}%")
print("Alert")

#-----------------------------------------------------------------------------------------------------------------

while True:
    test=input("Enter battery %(0-100):")
    value=float(test)
    if 0<= value <=100:
        break
    print("Out of range,try again")
print("Accepted:",value)

#-------------------------------------------------------------------------------------------------------------------

''' Write a Python program in which a loop starts of value 10 and counts down to 1,\n
printing each value of the count and then prints lift off.'''

value=10
while True:
    print(value)
    value-=1
    if value==0:
        break
print("Take off")

'''OR'''

value=10
while value>=1:
    print(value)
    value-=1
print("Take off")

#--------------------------------------------------------------------------------------------------------------------

''' Write a Python program that adds numbers from 1 to 100 and prints the total '''
j=0
i=1
while True:
    j=j+1
    i+=1
    if i==100:
        break
    print(j)