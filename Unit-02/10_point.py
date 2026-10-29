class Point:
    def __init__(self,x, y):
        self.x, self.y=x, y

    def __str__(self):
        return f"({self.x},{self.y})"

p=Point(2, 3)
print(p)
print(f"Robot is a {p}")

 
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import math


class Point:
    def __init__(self,x,y):
        self.x,self.y=x,y
    def dist_to(self,other):
        return math.hypot(self.x-other.x,self.y-other.y)  #we can link a single class to multiple objetcs ,here this class needs 2 objects to run

    def __str__(self):
        return f"({self.x},{self.y})"

    
robot=Point(2,3)
dock=Point(5,7)
print(f" robot {robot}-> dock {dock}")
print("distance :",robot.dist_to(dock))
#-----------------------------------------------------------------------------------------
#------------------------------------------------------------------------
import math

class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def dist_to(self, other):
        return math.hypot(self.x - other.x, self.y - other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"
robot = Point(2, 3)
dock = Point(5, 7)
print(f"robot {robot} -> dock {dock}")
print("distance:", robot.dist_to(dock))