def calculate_average(numbers):
    if not numbers:  # Handle empty list case
        return 0  # Or raise an exception: raise ValueError("List cannot be empty")
    return sum(numbers) / len(numbers)

my_list = []
result = calculate_average(my_list)
print(f"The average is: {result}")