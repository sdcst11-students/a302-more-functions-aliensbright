#!python3
"""
##### Problem 2
Create a function that determines if a triangle is scalene, right or obtuse.  
3 input parameters:  
float: one side  
float: another side  
float: 3rd side  

return:
0 : triangle does not exist
1 : if the triangle is acute
2 : if the triangle is right
3 : if the triangle is obtuse

Sample assertions:  
assert triangle(12,5,13) == 2     
assert triangle(5,3,3) == 3  
assert triangle(5,15,12) == 3  
assert triangle(1,1,4) == 0  
(2 points)
"""

def triangle(x,y,z):
    length = [x,y,z]
    length.sort()
    a=length[0]
    b=length[1]
    c=length[2]
    if c<a+b:
        if a**2+b**2>c**2: # Acute
            triType = 1

        elif a**2+b**2==c**2: # Right Angle
            triType = 2

        elif a**2+b**2<c**2: # Obtuse
            triType = 3
    else:
        triType = 0
    return triType

def tests():
    
    assert triangle(12,5,13) == 2     
    assert triangle(5,3,3) == 3  
    assert triangle(5,15,12) == 3  
    assert triangle(1,1,4) == 0  


if __name__== "__main__":
    tests()
