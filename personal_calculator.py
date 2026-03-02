"""
Personal Finance Calculator
Collects employee salary details and produces a financial breakdown.
"""


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
    print(f"Employee : {name}")
    print(f"Annual Salary : ₹{annual_salary:,.2f}")
    print("────────────────────────────────────────────")
    print("Monthly Breakdown:")
    print(f"Gross Salary : ₹ {finances['monthly_salary']:,.2f}")
    print(f"Tax ({tax_percent:.1f}%) : ₹ {finances['tax_deduction']:,.2f}")
    print(f"Net Salary : ₹ {finances['net_salary']:,.2f}")
    print(f"Rent : ₹ {monthly_rent:,.2f} ({finances['rent_ratio']:.1f}% of net)")
    print(f"Savings ({savings_percent:.1f}%) : ₹ {finances['savings_amount']:,.2f}")
    print(f"Disposable : ₹ {finances['disposable_income']:,.2f}")
    print("────────────────────────────────────────────")
    print("Annual Projection:")
    print(f"Total Tax : ₹ {finances['total_tax']:,.2f}")
    print(f"Total Savings : ₹ {finances['total_savings']:,.2f}")
    print(f"Total Rent : ₹ {finances['total_rent']:,.2f}")
    print("════════════════════════════════════════════")


def main():
    """Main function to run the finance calculator."""
    try:
        name, annual_salary, tax_percent, monthly_rent, savings_percent = get_employee_data()
        finances = calculate_finances(annual_salary, tax_percent, monthly_rent, savings_percent)
        generate_report(name, annual_salary, tax_percent, savings_percent, monthly_rent, finances)
    except ValueError as e:
        print(f"Input Error: {e}")


if __name__ == "__main__":
    main()