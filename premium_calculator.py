def calculate_premium(age, car_type, accident_count):
    base = 50000

    if age < 26:
        base += 30000

    if car_type == "sports":
        base += 50000

    base += accident_count * 20000

    return base


print("Estimated Premium:",
      calculate_premium(25, "sports", 1))
