def stat_calc(numbers):
    """
    Calculates and returns various statistical measures for a list of numbers.

    Args:
        numbers (list): A list of numerical values.

    Returns:
        tuple: A tuple containing (maximum, minimum, mean, variance, range, 3rd moment, 4th moment).
    """
    # Ensure the input list is not empty to avoid errors
    if not numbers:
        raise ValueError("The list of numbers cannot be empty.")
    
    # Calculate maximum and minimum
    max_val = max(numbers)
    min_val = min(numbers)

    # Calculate mean
    mean_val = sum(numbers) / len(numbers)

    # Calculate variance
    variance_val = sum((x - mean_val) ** 2 for x in numbers) / len(numbers)

    # Calculate range
    range_val = max_val - min_val

    # Calculate 3rd moment
    third_moment_val = sum((x - mean_val) ** 3 for x in numbers) / len(numbers)

    # Calculate 4th moment
    fourth_moment_val = sum((x - mean_val) ** 4 for x in numbers) / len(numbers)

    return max_val, min_val, mean_val, variance_val, range_val, third_moment_val, fourth_moment_val

# Example usage:
numbers_list = [10, 20, 15, 30, 25]
max_val, min_val, mean_val, variance_val, range_val, third_moment_val, fourth_moment_val = stat_calc(numbers_list)
print(f"Maximum: {max_val}")
print(f"Minimum: {min_val}")
print(f"Mean: {mean_val:.2f}")
print(f"Variance: {variance_val:.2f}")
print(f"Range: {range_val:.2f}")
print(f"3rd Moment: {third_moment_val:.2f}")
print(f"4th Moment: {fourth_moment_val:.2f}")
