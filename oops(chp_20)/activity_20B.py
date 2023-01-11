'''#pseudocode algo-1
DECLARE base,height,radius :INTEGER
DECLARE aera: REAL
DECLARE CONSTANT Pi = 3.142
OUTPUT "Please enter base,height and radius"
INPUT base,height,radius
area = base*base
OUTPUT = "Area of square is", area
area = base*height
OUTPUT = "Area of rectangle is", area
area = base*height
OUTPUT = "Area of triangle is", area
area = (base*height)/2
OUTPUT ="area of parallelogram is",area
area = base*height
OUTPUT ="Area of circle is ", area
area = Pi*radius*radius
'''

'''pseudocode-2
DECLARE base, height, radius : INTEGER
DECLARE area : REAL
FUNCTION square (side : INTEGER) RETURNS REAL
 RETURN side * side
ENDFUNCTION
FUNCTION rectangle (side : INTEGER, otherSide) RETURNS REAL
 RETURN side * otherSide
ENDFUNCTION
FUNCTION triangle (triBase : INTEGER, triHeight) RETURNS REAL
 RETURN triBase * triHeight / 2
ENDFUNCTION
FUNCTION parallelogram (parBase : INTEGER, parHeight) RETURNS
REAL
 RETURN parBase * parBase
ENDFUNCTION
FUNCTION circle(circRad : INTEGER) RETURNS REAL
 DECLARE CONSTANT Pi = 3.142
 RETURN circRad * circRad * Pi
ENDFUNCTION
PROCEDURE printArea (shapeName : String : areaToPrint : REAL)
 OUTPUT "Area of ", shapeName, " is ", areaToPrint
ENDPROCEDURE
OUTPUT "Please enter base, height and radius"
INPUT base, height, radius
area = square(base)
printArea ("square", area)
area = rectangle(base, height)
printArea ("rectangle", area)
area = triangle(base, height)
printArea ("triangle", area) 
area = parallelogram(base, height)
printArea ("parallelogram", area)
area = circle(radius)
printArea ("circle", area) 
'''
#main code - 1
Pi = 3.142
base = int(input ("Please enter base "))
height = int(input ("Please enter height "))
radius = int(input ("Please enter radius "))
area = base * base
print ("Area of square is ", area)
area = base * height
print ("Area of rectangle is ", area)
area = base * height / 2
print ("Area of triangle is ", area)
area = base * height
print ("Area of parallelogram is ", area)
area = radius * radius * Pi
print ("Area of circle is ", area)

#areas using prodedures and functions
def square(side):
 return side * side
def rectangle(side, otherSide):
 return side * otherSide
def triangle(triBase, triHeight):
 return triBase * triHeight / 2
def parallelogram(parBase, parHeight):
 return parBase * parHeight
def circle(circRad):
 Pi = 3.142
 return circRad * circRad * Pi
def printArea (shapeName, areaToPrint):
 print ("Area of ", shapeName, " is ", areaToPrint)
base = int(input ("Please enter base "))
height = int(input ("Please enter height "))
radius = int(input ("Please enter radius "))
area = square(base)
printArea ("square", area)
area = rectangle(base, height)
printArea ("rectangle", area)
area = triangle(base, height)
printArea ("triangle", area)
area = parallelogram(base, height)
printArea ("parallelogram", area)
area = circle(radius)
printArea ("circle", area)