# Case Study 01 (Q1): University Scholarship Allocation
# Assigned Syllabus Only: variables, data types, operators, conditionals,
# loops, strings, lists, nested lists, tuples, tuple operations, and unpacking.

test_cases = [
    (
        "TC-01: Standard Merit & Tie-Breaker Evaluation",
        50,    # Minimum mark required per subject
        75.0,  # Minimum aggregate percentage
        80.0,  # Minimum attendance percentage
        600000,  # Maximum annual family income (INR)
        [
            ("APP101", "Aarav Sharma", [88, 92, 85, 90, 95], 92.0, 420000),
            ("APP102", "Diya Nair", [90, 90, 90, 90, 90], 92.0, 350000),
            ("APP103", "Rohan Verma", [90, 90, 90, 90, 90], 92.0, 500000),
            ("APP104", "Sneha Iyer", [95, 42, 91, 89, 88], 95.0, 300000),
            ("APP105", "Kabir Mehta", [82, 84, 80, 79, 85], 76.0, 400000),
            ("APP106", "Ananya Das", [84, 86, 82, 88, 80], 88.0, 720000),
        ],
    ),
    (
        "TC-02: Boundary & Invalid Record Check",
        40,
        70.0,
        75.0,
        500000,
        [
            ("APP201", "Vikram Rao", [70, 70, 70, 70, 70], 75.0, 500000),
            ("APP202", "Meera Joshi", [105, 80, 75, 82, 88], 90.0, 250000),
            ("APP203", "Arjun Patel", [65, 72, 68, 70, 75], 85.0, 450000),
        ],
    ),
]

print("=" * 78)
print("UNIVERSITY SCHOLARSHIP ALLOCATION SYSTEM".center(78))
print("=" * 78)

for case_title, min_sub, min_agg, min_att, max_inc, applicants in test_cases:
    print("\n" + "-" * 78)
    print(case_title)
    print(
        f"Criteria -> Subject Min: {min_sub} | Aggregate >= {min_agg:.1f}% | "
        f"Attendance >= {min_att:.1f}% | Income <= INR {max_inc}"
    )
    print("-" * 78)

    eligible_list = []
    ineligible_list = []

    for applicant in applicants:
        app_id, name, marks, attendance, income = applicant

        # Validate input ranges
        valid_record = True
        if len(marks) == 0:
            valid_record = False
        for m in marks:
            if m < 0 or m > 100:
                valid_record = False
        if attendance < 0 or attendance > 100 or income < 0:
            valid_record = False

        if not valid_record:
            ineligible_list.append((app_id, name, 0.0, "Invalid marks/attendance/income"))
            continue

        # Calculate total and aggregate percentage
        total_marks = 0
        failed_subject = False
        for m in marks:
            total_marks = total_marks + m
            if m < min_sub:
                failed_subject = True

        aggregate_pct = total_marks / len(marks)

        # Collect all unmet eligibility conditions
        reasons = []
        if failed_subject:
            reasons.append("Subject mark < " + str(min_sub))
        if aggregate_pct < min_agg:
            reasons.append("Aggregate < " + str(min_agg) + "%")
        if attendance < min_att:
            reasons.append("Attendance < " + str(min_att) + "%")
        if income > max_inc:
            reasons.append("Income > " + str(max_inc))

        if len(reasons) == 0:
            eligible_list.append((app_id, name, aggregate_pct, attendance, income))
        else:
            reason_text = ""
            for i in range(len(reasons)):
                if i > 0:
                    reason_text = reason_text + "; "
                reason_text = reason_text + reasons[i]
            ineligible_list.append((app_id, name, aggregate_pct, reason_text))

    # Rank eligible applicants using bubble sort with predefined tie-breakers:
    # 1) Higher aggregate %, 2) Higher attendance %, 3) Lower family income, 4) Smaller ID
    n = len(eligible_list)
    for i in range(n):
        for j in range(0, n - i - 1):
            id_a, name_a, agg_a, att_a, inc_a = eligible_list[j]
            id_b, name_b, agg_b, att_b, inc_b = eligible_list[j + 1]

            swap_needed = False
            if agg_a < agg_b:
                swap_needed = True
            elif agg_a == agg_b:
                if att_a < att_b:
                    swap_needed = True
                elif att_a == att_b:
                    if inc_a > inc_b:
                        swap_needed = True
                    elif inc_a == inc_b and id_a > id_b:
                        swap_needed = True

            if swap_needed:
                temp = eligible_list[j]
                eligible_list[j] = eligible_list[j + 1]
                eligible_list[j + 1] = temp

    print("\nELIGIBLE & RANKED SCHOLARSHIP LIST:")
    if len(eligible_list) == 0:
        print("  No applicants qualified for scholarship.")
    else:
        print(f"  {'Rank':<5} {'ID':<8} {'Name':<16} {'Agg(%)':>8} {'Att(%)':>8} {'Income(INR)':>13}")
        print("  " + "-" * 62)
        rank = 1
        for entry in eligible_list:
            app_id, name, agg_pct, att_pct, inc = entry
            print(f"  {rank:<5} {app_id:<8} {name:<16} {agg_pct:>8.2f} {att_pct:>8.2f} {inc:>13}")
            rank = rank + 1

    print("\nINELIGIBLE / REJECTED APPLICANTS:")
    if len(ineligible_list) == 0:
        print("  None")
    else:
        for item in ineligible_list:
            app_id, name, agg_pct, reason_text = item
            print(f"  {app_id:<8} {name:<16} (Agg: {agg_pct:5.2f}%) -> {reason_text}")
