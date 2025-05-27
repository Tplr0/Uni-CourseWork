
def get_numbers():
    numbers = []
    attempt = 1
    while len(numbers) < 3:
        try:
            number = int(input(f"Attempt {len(numbers) + 1}: Enter a non-negative integer: "))
            numbers.append(number)
            #if
        except ValueError:
            attempt += 1
            print(f"Attempt {(attempt)}: Enter a non-negative integer: ")
    return numbers

def calculate_statistics(numbers):
    mean = sum(numbers) / len(numbers)
    range_of_numbers = max(numbers) - min(numbers)
    sum_of_largest_two = sum(sorted(numbers)[-2:])
    return mean, range_of_numbers, sum_of_largest_two

def main():
    numbers = get_numbers()
    mean, range_of_numbers, sum_of_largest_two = calculate_statistics(numbers)
    print(f"The numbers are {numbers[0]} {numbers[1]} {numbers[2]}")
    print(f"The mean is {mean}")
    print(f"The range is {range_of_numbers}")
    print(f"The sum of the largest two numbers is {sum_of_largest_two}")

if __name__ == "__main__":
    main()