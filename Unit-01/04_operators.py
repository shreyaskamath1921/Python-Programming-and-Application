heading=359
turn=5
print("Wrong:",heading+turn)
print("Right:",(heading+turn)%360)
print("Negative:",(-30)%360)

#-------------------------------------------------------------------------------------------------------------------------

distance=8.0
limit=10
print(distance<limit)
print(distance==limit)
print(0<=distance<limit)
battery = 45
print(distance>5 and battery>20)
print(distance>5 or battery>90)
print(distance>5)

#--------------------------------------------------------------------------------------------------------------------

''' Write a Python program with single expression that is true only when the robot \n
is safe to move: distance>10, battery>20, not currently docked'''

distance=35
battery=50
docked=True
print(distance>10 and battery>20 and docked)