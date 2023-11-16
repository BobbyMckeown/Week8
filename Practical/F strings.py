# TASK: Write some code that uses an f-string to calculate
# then display a message stating “The area of a rectangle
# with a width of 104.32 and a height of 15.654 is ….”.
# Showing the correct answer at the end of the message.
width = 104.32
height = 15.654
print(f"The area of a rectangle is {width * height}\n")

# TASK: Rewrite your earlier code that displayed the area
# of a rectangle, but include a format specifier that limits the displayed result to three decimal places.

print(f"The area of a rectangle is {width * height:.3f}\n")

# TASK: Try setting the name and age variables to different
# values and executing the above print() statement multiple
# times. Notice the alignment and column width enforced due
# to the print specifier.

name = "Bobby"
age = 18
print(f"{name:25} - {age:30}")

# TASK: Write a print() statement that displays the name and
# age values, with a column width of 20 for each, both right
# aligned, and with the age being shown to two decimal places.
# The fill character should be a dollar symbol $.

print(f"{name:->20} $ {age:->20.2f}")

# TASK: Write some code that uses the str.format() method to
# display the area of a circle with a radius specified by the
# variable r. Use a keyword replacement field called area to
# identify the calculated area and refer to this when passing
# the value to the str.format() method. The output should look
# like the following, in the case where r is set to 52.

print("The radius is {radius} so the area is {area}".format(radius = 52, area = 8494.86654))


#TASK: Convert the f-string based statement below into an
# equivalent that uses the str.format() method to generate the same output.

print("{:@^15} - {:#^10}".format(name, age))
