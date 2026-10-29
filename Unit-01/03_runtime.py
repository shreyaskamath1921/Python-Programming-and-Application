battery=int(input("Enter battery percentage: "))
print(battery+10)

name="Alpha"
battery=78.56
print("Robot",name,"at",battery,"%")
print(f"Robot {name} at {battery}%")
print(f"Robot {name} at {battery:.1f}%")
print(f"{name: <10} | {battery:>3.2f}%")

#-----------------------------------------------------------------------------------------------------------------------

''' Write a Python file with name runtime.py that reads a battery capacity in mAh and a current in mA.\n
Predict the estimated runtime in hours to 2 decimal places.'''

battery_capacity = eval(input("Enter battery capacity(mAh): "))
current_drawn = eval(input("Enter the current drawn by the battery (mA): "))
runtime = battery_capacity/current_drawn
print(f"Estimated runtime: {runtime: 2f} hours")
