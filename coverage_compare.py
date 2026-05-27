plans = {
    "Basic": 30000,
    "Standard": 50000,
    "Premium": 80000
}

print("Insurance Plan Comparison")
print("--------------------------")

for plan, price in plans.items():
    print(f"{plan}: {price} KRW/month")
