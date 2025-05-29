""" Calculates the average of a list 'nums' """


def calculate_average(numbers):
    """Average calculation function"""
    total = sum(nums)
    count = len(numbers)
    average = total / count
    return average


nums = [10, 15, 20]
result = calculate_average(nums)
print("The average is:", result)
