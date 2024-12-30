
def triangle_area(base, height):
    return 0.5 * base * height


def rectangle_area(length, width):
    return length * width


def trapezoid_area(base1, base2, height):
    return 0.5 * (base1 + base2) * height

def triangle_area_by_sides(a, b, c):
    s = (a+b+c)/2
    return ((s*(s-a)*(s-b)*(s-c))**0.5)
'''
print("Triangle Area:", triangle_area())


print("Rectangle Area:", rectangle_area())


print("Trapezoid Area:", trapezoid_area())

'''
a, b, c = map(float, input("Enter three sides of the triangle: ").split())
print("Triangle Area:", triangle_area_by_sides(a,b,c))