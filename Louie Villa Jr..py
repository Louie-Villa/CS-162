#Function 1
# Returns Area of Rectangle
def rect_area():
    return length*width

#Function 2
# Returns Surface Area of Rectangular Solid
def rect_surface_area(length,width,height):
    side_1 = rect_area()
    side_2 = rect_area()
    side_3 = rect_area()
    total_area = 2 * (side_1 + side_2 + side_3)
    return total_area

# Request the dimension of a solid rectangular object

length = int(input("Enter the length of the the object as a integer: "))
width = int(input("Enter the width of the the object as a integer: "))
height = int(input("Enter the height of the the object as a integer: "))

print("Length = ", length, "Width = ", width, "Height = ", height)
print("Total Surface Area = ", str(rect_surface_area(length, width, height)))
print("Area of the rectangle: " + str(rect_area()))