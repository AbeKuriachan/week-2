while True:
    income = float(input("Enter annual income: "))

    standard_deduction = 75000
    taxable_income = max(0, income - standard_deduction)

    slabs = [
        (300000, 0.00),
        (700000, 0.05),
        (1000000, 0.10),
        (1200000, 0.15),
        (1500000, 0.20),
        (float('inf'), 0.30)
    ]

    prev_limit = 0
    total_tax = 0

    print("\nTax Breakdown")
    print("---------------------------")

    for limit, rate in slabs:
        if taxable_income > prev_limit:
            slab_income = min(taxable_income, limit) - prev_limit
            tax = slab_income * rate
            total_tax += tax

            print(f"Income ₹{slab_income:,.0f} taxed at {rate*100:.0f}% → Tax ₹{tax:,.0f}")

            prev_limit = limit
        else:
            break

    effective_rate = (total_tax / income) * 100 if income > 0 else 0

    print("---------------------------")
    print(f"Taxable Income: ₹{taxable_income:,.0f}")
    print(f"Total Tax: ₹{total_tax:,.0f}")
    print(f"Effective Tax Rate: {effective_rate:.2f}%\n")

