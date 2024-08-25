grades = [2.0, 7.5, 8.5, 3.5]

# Tính mean
def calculate_mean(grades):
    total = 0
    for grade in grades:
        total += grade
    mean = total / len(grades)
    return mean

# Tính median
def calculate_median(grades):
    sorted_grades = sorted(grades)
    n = len(sorted_grades)
    mid = n // 2
    if n % 2 == 0:
        median = (sorted_grades[mid - 1] + sorted_grades[mid]) / 2  
    else:
        median = sorted_grades[mid]
    return median

mean = calculate_mean(grades)
median = calculate_median(grades)


print(f"Mean: {mean}")
print(f"Median: {median}")
