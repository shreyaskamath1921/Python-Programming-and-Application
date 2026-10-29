def locate_point(x,y):
    if x==0 and y==0:
        return "Origin"
    if x==0:
        return "Y-axis"
    if y==0:
        return "X-axis"
    if x>0 and y>0:
        return "First quadrant"
    if x<0 and y>0:
        return "Second quadrant"
    if x<0 and y<0:
        return "Third quadrant"
    return "Fourth quadrant"
x=float(input("Enter x-coordinate: "))
y=float(input("Enter y-coordinate: "))
print(locate_point(x,y))
