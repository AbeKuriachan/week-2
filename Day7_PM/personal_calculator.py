"""
Personal Finance Calculator
Collects employee salary details and produces a financial breakdown.
"""


def format_inr(amount):
    """Format amount in Indian locale (e.g., ₹1,23,456.78)."""
    is_negative = amount < 0
    amount = abs(amount)
    integer_part, _, decimal_part = f"{amount:.2f}".partition(".")

    # Indian grouping: last 3 digits, then groups of 2
    if len(integer_part) > 3:
        last_three = integer_part[-3:]
        rest = integer_part[:-3]
        # Group remaining digits in pairs from the right
        groups = []
        while len(rest) > 2:
            groups.append(rest[-2:])
            rest = rest[:-2]
        if rest:
            groups.append(rest)
        groups.reverse()
        formatted = ",".join(groups) + "," + last_three
    else:
        formatted = integer_part

    result = f"₹{formatted}.{decimal_part}"
    return f"-{result}" if is_negative else result


def get_employee_data():
    """Collect and validate employee financial inputs."""
    name = input("Enter employee name: ").strip()

    # Annual salary
    annual_salary = float(input("Enter annual salary (₹): "))
    if annual_salary <= 0:
        raise ValueError("Annual salary must be greater than 0.")

    # Tax bracket
    tax_percent = float(input("Enter tax bracket percentage (0-50): "))
    if not (0 <= tax_percent <= 50):
        raise ValueError("Tax percentage must be between 0 and 50.")

    # Monthly rent
    monthly_rent = float(input("Enter monthly rent (₹): "))
    if monthly_rent <= 0:
        raise ValueError("Monthly rent must be greater than 0.")

    # Savings goal
    savings_percent = float(input("Enter savings goal percentage (0-100): "))
    if not (0 <= savings_percent <= 100):
        raise ValueError("Savings percentage must be between 0 and 100.")

    return name, annual_salary, tax_percent, monthly_rent, savings_percent


def calculate_finances(annual_salary, tax_percent, monthly_rent, savings_percent):
    """Perform financial calculations based on inputs."""
    monthly_salary = annual_salary / 12
    tax_deduction = monthly_salary * (tax_percent / 100)
    net_salary = monthly_salary - tax_deduction
    rent_ratio = (monthly_rent / net_salary) * 100
    savings_amount = net_salary * (savings_percent / 100)
    disposable_income = net_salary - monthly_rent - savings_amount

    # Annual projections
    total_tax = tax_deduction * 12
    total_savings = savings_amount * 12
    total_rent = monthly_rent * 12

    return {
        "monthly_salary": monthly_salary,
        "tax_deduction": tax_deduction,
        "net_salary": net_salary,
        "rent_ratio": rent_ratio,
        "savings_amount": savings_amount,
        "disposable_income": disposable_income,
        "total_tax": total_tax,
        "total_savings": total_savings,
        "total_rent": total_rent
    }


def generate_report(name, annual_salary, tax_percent, savings_percent, monthly_rent, finances):
    """Generate a formatted financial summary report."""
    print("════════════════════════════════════════════")
    print("EMPLOYEE FINANCIAL SUMMARY")
    print("════════════════════════════════════════════")
    print(f"Employee      : {name}")
    print(f"Annual Salary : {format_inr(annual_salary)}")
    print("────────────────────────────────────────────")
    print("Monthly Breakdown:")
    print(f"Gross Salary  : {format_inr(finances['monthly_salary'])}")
    print(f"Tax ({tax_percent:.1f}%)     : {format_inr(finances['tax_deduction'])}")
    print(f"Net Salary    : {format_inr(finances['net_salary'])}")
    print(f"Rent          : {format_inr(monthly_rent)} ({finances['rent_ratio']:.1f}% of net)")
    print(f"Savings ({savings_percent:.1f}%) : {format_inr(finances['savings_amount'])}")
    print(f"Disposable    : {format_inr(finances['disposable_income'])}")
    print("────────────────────────────────────────────")
    print("Annual Projection:")
    print(f"Total Tax     : {format_inr(finances['total_tax'])}")
    print(f"Total Savings : {format_inr(finances['total_savings'])}")
    print(f"Total Rent    : {format_inr(finances['total_rent'])}")
    print("────────────────────────────────────────────")
    score = financial_health_score(finances, savings_percent)
    if score >= 80:
        rating = "Excellent 🟢"
    elif score >= 60:
        rating = "Good 🟡"
    elif score >= 40:
        rating = "Fair 🟠"
    else:
        rating = "Poor 🔴"
    print(f"Health Score  : {score}/100 ({rating})")
    print("════════════════════════════════════════════")


def main():
    """Main function to run the finance calculator."""
    try:
        name, annual_salary, tax_percent, monthly_rent, savings_percent = get_employee_data()
        finances = calculate_finances(annual_salary, tax_percent, monthly_rent, savings_percent)
        generate_report(name, annual_salary, tax_percent, savings_percent, monthly_rent, finances)
    except ValueError as e:
        print(f"Input Error: {e}")


def financial_health_score(finances, savings_percent):
    """Calculate financial health score (0-100)."""
    score = 0

    # Rent ratio contribution (max 30 points)
    if finances['rent_ratio'] <= 30:
        score += 30
    elif finances['rent_ratio'] <= 40:
        score += 20
    else:
        score += 10

    # Savings contribution (max 40 points)
    if savings_percent >= 20:
        score += 40
    elif savings_percent >= 10:
        score += 25
    else:
        score += 10

    disposable_ratio = (finances['disposable_income'] / finances['net_salary']) * 100
    if disposable_ratio >= 40:
        score += 30
    elif disposable_ratio >= 20:
        score += 20
    else:
        score += 10

    return score


if __name__ == "__main__":
    main()