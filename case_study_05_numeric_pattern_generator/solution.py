# Case Study 05 (Q27): Advanced Numeric Pattern Generator
# Assigned Syllabus Only: variables, data types, operators, conditionals,
# loops, strings, pattern generation, lists, tuples, and unpacking.

test_requests = [
    ("HOLLOW_DIAMOND", 5),
    ("HOLLOW_DIAMOND", 7),
    ("SYMMETRIC_PYRAMID", 5),
    ("HOLLOW_DIAMOND", 4),     # Invalid: even dimension
    ("SYMMETRIC_PYRAMID", 0),  # Invalid: non-positive
    ("HOLLOW_DIAMOND", 11),    # Invalid: exceeds single-digit alignment limit (>9)
]

print("=" * 70)
print("ADVANCED NUMERIC PATTERN GENERATOR".center(70))
print("=" * 70)

for request in test_requests:
    pattern_type, rows = request
    print(f"\nRequest -> Pattern: {pattern_type} | Dimension (n): {rows}")
    print("-" * 70)

    if pattern_type == "HOLLOW_DIAMOND":
        if rows < 3 or rows > 9 or rows % 2 == 0:
            print("  [VALIDATION ERROR] Hollow diamond requires an odd integer between 3 and 9.")
            continue

        mid = (rows // 2) + 1

        # Upper half (including middle row)
        for i in range(1, mid + 1):
            leading_spaces = "  " * (mid - i)
            if i == 1:
                print(leading_spaces + str(i))
            else:
                inner_spaces = " " * ((4 * i) - 5)
                print(leading_spaces + str(i) + inner_spaces + str(i))

        # Lower half
        for i in range(mid - 1, 0, -1):
            leading_spaces = "  " * (mid - i)
            if i == 1:
                print(leading_spaces + str(i))
            else:
                inner_spaces = " " * ((4 * i) - 5)
                print(leading_spaces + str(i) + inner_spaces + str(i))

    elif pattern_type == "SYMMETRIC_PYRAMID":
        if rows < 1 or rows > 9:
            print("  [VALIDATION ERROR] Symmetric pyramid requires an integer between 1 and 9.")
            continue

        for i in range(1, rows + 1):
            line = "  " * (rows - i)
            # Ascending digits
            for num in range(1, i + 1):
                line = line + str(num) + " "
            # Descending digits
            for num in range(i - 1, 0, -1):
                line = line + str(num) + " "
            print(line.rstrip())

    else:
        print("  [VALIDATION ERROR] Unsupported pattern type.")
