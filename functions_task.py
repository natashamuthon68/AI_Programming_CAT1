from math import pi
def area_of_circle(radius):
# Validate that radius is greater than 0
 if radius<=0:
    return"Radius must be greater than 0"

 area= pi*radius**2   #multiply pi by radius squared

#return rounded to 2 decimal places
 return round(area,2)

# Ask the user for radius
radius_input= float(input("Enter the radius of the circle:"))

# Call the function and input the area
result=area_of_circle(radius_input)

# Display output
print(f"Radius entered:{radius_input}")
print(f"The calculated area is:{result}")