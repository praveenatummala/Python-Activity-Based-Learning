# Case Study 08 (Q42): Student Marks Matrix Analysis
# Assigned Syllabus Only: variables, data types, operators, conditionals,
# loops, strings, lists, nested lists, tuples, tuple operations, and unpacking.

subjects = ["Math", "Physics", "Chemistry", "Python", "English"]
students = ["Ananya", "Bhargav", "Chitra", "Deepak", "Esha"]

# 2D Nested List: rows = students, columns = subjects
marks_matrix = [
    [92, 85, 78, 96, 89],
    [76, 58, 52, 84, 70],
    [95, 88, 64, 93, 91],
    [60, 49, 44, 72, 65],
    [88, 74, 59, 95, 85],
]

PASS_MARK = 40
LOW_SUBJECT_AVG_THRESHOLD = 65.0

print("=" * 78)
print("STUDENT MARKS MATRIX ANALYSIS".center(78))
print("=" * 78)

# Validate matrix structure and mark bounds
num_students = len(students)
num_subjects = len(subjects)
matrix_valid = True

if len(marks_matrix) != num_students:
    matrix_valid = False
else:
    for row in marks_matrix:
        if len(row) != num_subjects:
            matrix_valid = False
            break
        for val in row:
            if val < 0 or val > 100:
                matrix_valid = False
                break

if not matrix_valid:
    print("ERROR: Matrix dimensions or mark values (0-100) are invalid.")
else:
    # 1. Row-wise (Student-wise) statistics
    print("\n1. STUDENT-WISE PERFORMANCE (ROW-WISE STATISTICS)")
    print("-" * 78)
    print(f"{'Student':<12} {'Total':>7} {'Average':>9} {'Min':>6} {'Max':>6}  {'Subject Marks'}")
    print("-" * 78)

    student_totals = []
    highest_total = -1

    for i in range(num_students):
        row = marks_matrix[i]
        total = 0
        row_min = row[0]
        row_max = row[0]
        marks_str = ""

        for j in range(num_subjects):
            val = row[j]
            total = total + val
            if val < row_min:
                row_min = val
            if val > row_max:
                row_max = val
            if j > 0:
                marks_str = marks_str + ", "
            marks_str = marks_str + str(val)

        avg = total / num_subjects
        student_totals.append((students[i], total, avg))
        if total > highest_total:
            highest_total = total

        print(f"{students[i]:<12} {total:>7} {avg:>9.2f} {row_min:>6} {row_max:>6}  [{marks_str}]")

    # Identify top performers
    top_performers = []
    for s_name, s_total, s_avg in student_totals:
        if s_total == highest_total:
            top_performers.append((s_name, s_total, s_avg))

    print("\nTop Performer(s):")
    for s_name, s_total, s_avg in top_performers:
        print(f"  * {s_name} -> Total: {s_total}/{num_subjects * 100} (Average: {s_avg:.2f}%)")

    # 2. Column-wise (Subject-wise) statistics
    print("\n2. SUBJECT-WISE PERFORMANCE (COLUMN-WISE STATISTICS)")
    print("-" * 78)
    print(f"{'Subject':<12} {'Average':>9} {'Min':>6} {'Max':>6} {'Pass Count':>12}  {'Status'}")
    print("-" * 78)

    low_avg_subjects = []
    for j in range(num_subjects):
        col_total = 0
        col_min = marks_matrix[0][j]
        col_max = marks_matrix[0][j]
        pass_cnt = 0

        for i in range(num_students):
            val = marks_matrix[i][j]
            col_total = col_total + val
            if val < col_min:
                col_min = val
            if val > col_max:
                col_max = val
            if val >= PASS_MARK:
                pass_cnt = pass_cnt + 1

        col_avg = col_total / num_students
        sub_status = "Healthy"
        if col_avg < LOW_SUBJECT_AVG_THRESHOLD:
            sub_status = "LOW AVERAGE"
            low_avg_subjects.append((subjects[j], col_avg))

        print(f"{subjects[j]:<12} {col_avg:>9.2f} {col_min:>6} {col_max:>6} {pass_cnt:>7}/{num_students:<4}  {sub_status}")

    print("\nSubjects Below Threshold (< " + str(LOW_SUBJECT_AVG_THRESHOLD) + "):")
    if len(low_avg_subjects) == 0:
        print("  None")
    else:
        for sub_name, sub_avg in low_avg_subjects:
            print(f"  * {sub_name}: Average = {sub_avg:.2f}")
