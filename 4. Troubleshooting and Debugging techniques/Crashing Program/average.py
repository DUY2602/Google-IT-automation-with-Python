# Debug using try except (the most common way)

def calculate_average(numbers):
    try:
        return sum(numbers) / len(numbers)
    except ZeroDivisionError:
        print("The list is empty. Cannot calculate the average.")
        return None
    
print(calculate_average([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(calculate_average([]))