def calculate_average(numbers):
    if not numbers:
        raise ValueError("List cannot be empty")  # Raise a ValueError for better error handling
    return sum(numbers) / len(numbers)

try:
    my_list = []
    result = calculate_average(my_list)
    print(f"The average is: {result}")
except ValueError as e:
    print(f"Error: {e}")

my_list = [10, 20, 30]
result = calculate_average(my_list)
print(f"The average is: {result}") 