## First task (importing math for pi)

import math
radius = float(input("Enter the radius of circle : "))

def calculate_area(radius):
 area = math.pi*radius**2
 return area

print("The area of the circle :",calculate_area(radius))


## second task(extension name of the file)

file_name = input("Enter the file name : ")
def file_extension(file_name):
 x = file_name.split('.')
 extension = x[-1]
 return extension

if file_extension(file_name) == "py" :
 print("Extension of the file : python file")
elif file_extension(file_name) == "java" :
 print("Extension of the file : java file")
elif file_extension(file_name) == "txt" :
 print("Extension of the file : text file")
else:
 print("There is no extension file")
