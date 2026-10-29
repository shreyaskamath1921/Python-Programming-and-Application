robot_name="Alpha"
battery_pct=78.5
is_docked=True
waypoints=12
print("----")
print(type(robot_name))

#-----------------------------------------------------------------------------------------------------

battery = 100
print("start:",battery )
battery = battery - 15
print("after:", battery)
battery -= 15
print("later:",battery)

#-------------------------------------------------------------------------------------------------------

battery = 45
if battery<50:
    print("Battery low, please recharge")
    print("Docking now...")
print("Status check complete")

#-------------------------------------------------------------------------------------------------------
''' Write a Python program with a file name ROBOT_STATE.PY with 4 variables describing a robot of your choice. Print them and then add an if block that prints a warning when the battery is below 50%.'''

robot_name="Beta"
battery_pct=45
docked=False
points=17
print(robot_name,battery_pct,docked,points)
if battery <50:
    print("Battery is low")
    
