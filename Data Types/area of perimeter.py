# Program to calculate area and perimeter of a rectangle

def rectangle_area(length, width):
    return length * width

def rectangle_perimeter(length, width):
    return 2 * (length + width)

if __name__ == "__main__":
    print("Calculate area and perimeter of a rectangle")
    length = float(input("Enter the length: "))
    width = float(input("Enter the width: "))

    area = rectangle_area(length, width)
    perimeter = rectangle_perimeter(length, width)
    print(f"Length: {length}")
    print(f"Width: {width}")

    print(f"Area: {area}")
    print(f"Perimeter: {perimeter}")