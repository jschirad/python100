import math
def paint_calc(height, width, cover):
    """
    Calculate the number of panels that will be painted.
    """
    result = (height * width) / coverage
    result = math.ceil(result)
    print("The number of panels that will be painted is: " + str(result))
    
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

