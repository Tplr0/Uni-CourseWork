import math


def get_diameter():
    while True:
        try:
            diameter = float(input("Enter the diameter of the sphere: "))
            if diameter >= 0.0:
                return diameter
            else:
                print("Please enter a diameter greater than or equal to 0.0.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def calculate_radius(diameter):
    return diameter / 2


def calculate_surface_area(radius):
    return 4 * math.pi * radius ** 2


def calculate_circumference(diameter):
    return math.pi * diameter


def calculate_volume(radius):
    return (4 / 3) * math.pi * radius ** 3


def main():
    diameter = get_diameter()
    radius = calculate_radius(diameter)
    surface_area = calculate_surface_area(radius)
    circumference = calculate_circumference(diameter)
    volume = calculate_volume(radius)

    print("Results:")
    print("Radius (r) = {:.2f}".format(radius))
    print("Surface Area = {:.2f}".format(surface_area))
    print("Circumference = {:.2f}".format(circumference))
    print("Volume = {:.2f}".format(volume))


main()
