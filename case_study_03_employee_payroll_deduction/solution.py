# Case Study 03 (Q4): Employee Payroll and Deduction Analysis
# Assigned Syllabus Only: variables, data types, operators, conditionals,
# loops, strings, lists, tuples, tuple operations, and unpacking.

employees = [
    ("EMP101", "Neha Kulkarni", "Engineering", 45000.0, 10, 400.0, 5000.0),
    ("EMP102", "Suresh Babu", "Operations", 22000.0, 5, 250.0, 1500.0),
    ("EMP103", "Priya Menon", "Finance", 78000.0, 0, 500.0, 8000.0),
    ("EMP104", "Rahul Singh", "Support", -15000.0, 4, 200.0, 1000.0),
]

print("=" * 74)
print("EMPLOYEE PAYROLL AND PROGRESSIVE DEDUCTION STATEMENT".center(74))
print("=" * 74)

total_company_gross = 0.0
total_company_deductions = 0.0
total_company_net = 0.0
processed_count = 0

for emp in employees:
    emp_id, name, dept, basic_pay, ot_hours, ot_rate, incentive = emp

    if basic_pay <= 0 or ot_hours < 0 or ot_rate < 0 or incentive < 0:
        print(f"\n[REJECTED RECORD] {emp_id} ({name}): Invalid negative/zero pay parameter.")
        continue

    # Earnings calculation
    hra = basic_pay * 0.20
    da = basic_pay * 0.15
    overtime_pay = ot_hours * ot_rate
    gross_salary = basic_pay + hra + da + overtime_pay + incentive

    # Deductions calculation
    pf = basic_pay * 0.12
    prof_tax = 200.0 if gross_salary > 25000.0 else 0.0

    # Progressive monthly income tax slabs
    income_tax = 0.0
    if gross_salary <= 30000.0:
        income_tax = 0.0
    elif gross_salary <= 60000.0:
        income_tax = (gross_salary - 30000.0) * 0.10
    elif gross_salary <= 100000.0:
        income_tax = (30000.0 * 0.10) + ((gross_salary - 60000.0) * 0.20)
    else:
        income_tax = (30000.0 * 0.10) + (40000.0 * 0.20) + ((gross_salary - 100000.0) * 0.30)

    total_deductions = pf + prof_tax + income_tax
    net_salary = gross_salary - total_deductions

    total_company_gross = total_company_gross + gross_salary
    total_company_deductions = total_company_deductions + total_deductions
    total_company_net = total_company_net + net_salary
    processed_count = processed_count + 1

    # Formatted salary statement
    print("\n" + "-" * 74)
    print(f"PAYSLIP | ID: {emp_id} | Name: {name} | Department: {dept}")
    print("-" * 74)
    print(f"  {'EARNINGS':<32} | {'DEDUCTIONS':<32}")
    print(f"  {'Basic Pay':<20}{basic_pay:>12.2f} | {'Provident Fund (12%)':<22}{pf:>10.2f}")
    print(f"  {'HRA (20%)':<20}{hra:>12.2f} | {'Professional Tax':<22}{prof_tax:>10.2f}")
    print(f"  {'DA (15%)':<20}{da:>12.2f} | {'Income Tax (Slab)':<22}{income_tax:>10.2f}")
    print(f"  {'Overtime Pay':<20}{overtime_pay:>12.2f} | {'':<32}")
    print(f"  {'Incentives':<20}{incentive:>12.2f} | {'':<32}")
    print("  " + "-" * 67)
    print(f"  {'Gross Salary':<20}{gross_salary:>12.2f} | {'Total Deductions':<22}{total_deductions:>10.2f}")
    print(f"  NET PAYABLE SALARY: INR {net_salary:,.2f}")

print("\n" + "=" * 74)
print("PAYROLL SUMMARY".center(74))
print("=" * 74)
print(f"Processed Employees : {processed_count}")
print(f"Total Gross Payout  : INR {total_company_gross:,.2f}")
print(f"Total Deductions    : INR {total_company_deductions:,.2f}")
print(f"Total Net Payout    : INR {total_company_net:,.2f}")
