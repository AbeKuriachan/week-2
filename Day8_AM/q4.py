def classify_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return "Not a triangle"

    # Triangle inequality rule
    if a >= b + c or b >= a + c or c >= a + b:
        return "Not a triangle"
    if a == b == c:
        return "Equilateral"
    elif a == b or b == c or a == c:
        return "Isosceles"
    else:
        return "Scalene"