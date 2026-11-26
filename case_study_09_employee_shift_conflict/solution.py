# Case Study 09 (Q48): Tuple-Based Employee Shift Conflict Detection
# Assigned Syllabus Only: variables, data types, operators, conditionals,
# loops, strings, lists, tuples, tuple operations, and unpacking.

# Shift tuple format: (shift_id, emp_id, emp_name, day, start_hhmm, end_hhmm)
shifts = [
    ("SH01", "E101", "Arjun Nair", "Monday", "09:00", "13:00"),
    ("SH02", "E101", "Arjun Nair", "Monday", "12:00", "16:00"),     # Overlaps SH01 (60 min)
    ("SH03", "E101", "Arjun Nair", "Tuesday", "09:00", "13:00"),    # Different day (no overlap)
    ("SH04", "E102", "Kavya Rao", "Monday", "08:00", "12:00"),
    ("SH05", "E102", "Kavya Rao", "Monday", "12:00", "16:00"),      # Back-to-back (no overlap)
    ("SH06", "E103", "Manoj Verma", "Wednesday", "10:00", "14:00"),
    ("SH07", "E103", "Manoj Verma", "Wednesday", "11:00", "13:00"), # Nested overlap (120 min)
    ("SH08", "E104", "Pooja Iyer", "Thursday", "18:00", "15:00"),   # Invalid: end <= start
]

print("=" * 82)
print("TUPLE-BASED EMPLOYEE SHIFT CONFLICT DETECTION".center(82))
print("=" * 82)

valid_shifts = []
invalid_shifts = []

# Step 1: Parse and validate each shift tuple
for shift in shifts:
    shift_id, emp_id, emp_name, day, start_str, end_str = shift

    start_parts = start_str.split(":")
    end_parts = end_str.split(":")
    valid = True

    if len(start_parts) != 2 or len(end_parts) != 2:
        valid = False
    elif not (start_parts[0].isdigit() and start_parts[1].isdigit() and end_parts[0].isdigit() and end_parts[1].isdigit()):
        valid = False

    if valid:
        sh = int(start_parts[0])
        sm = int(start_parts[1])
        eh = int(end_parts[0])
        em = int(end_parts[1])
        if sh < 0 or sh > 23 or sm < 0 or sm > 59 or eh < 0 or eh > 23 or em < 0 or em > 59:
            valid = False
        else:
            start_min = (sh * 60) + sm
            end_min = (eh * 60) + em
            if end_min <= start_min:
                valid = False

    if valid:
        valid_shifts.append((shift_id, emp_id, emp_name, day, start_str, end_str, start_min, end_min))
    else:
        invalid_shifts.append((shift_id, emp_id, emp_name, day, start_str, end_str))

print(f"Total Input Shifts: {len(shifts)} | Valid Shifts: {len(valid_shifts)} | Invalid Shifts: {len(invalid_shifts)}")
if len(invalid_shifts) > 0:
    print("\nINVALID SHIFT RECORDS:")
    for inv in invalid_shifts:
        s_id, e_id, e_name, d, st, en = inv
        print(f"  - {s_id} ({e_id} {e_name}, {d} {st}-{en}): End time must be after start time (HH:MM)")

# Step 2: Pairwise comparison for overlapping intervals on same employee & day
conflicts = []
conflicting_employees = []

for i in range(len(valid_shifts)):
    s1_id, e1_id, e1_name, d1, st1, en1, s1_min, e1_min = valid_shifts[i]
    for j in range(i + 1, len(valid_shifts)):
        s2_id, e2_id, e2_name, d2, st2, en2, s2_min, e2_min = valid_shifts[j]

        if e1_id == e2_id and d1.lower() == d2.lower():
            # Overlap condition for half-open intervals [start, end)
            if s1_min < e2_min and s2_min < e1_min:
                overlap_start = s1_min if s1_min > s2_min else s2_min
                overlap_end = e1_min if e1_min < e2_min else e2_min
                overlap_mins = overlap_end - overlap_start
                conflicts.append((e1_id, e1_name, d1, s1_id, st1, en1, s2_id, st2, en2, overlap_mins))

                emp_label = e1_id + " - " + e1_name
                if emp_label not in conflicting_employees:
                    conflicting_employees.append(emp_label)

# Collect conflict-free valid employees
clean_employees = []
for s_id, e_id, e_name, d, st, en, s_m, e_m in valid_shifts:
    emp_label = e_id + " - " + e_name
    if emp_label not in conflicting_employees and emp_label not in clean_employees:
        clean_employees.append(emp_label)

print("\nDETECTED SHIFT CONFLICTS:")
print("-" * 82)
if len(conflicts) == 0:
    print("  No overlapping shifts detected.")
else:
    for c in conflicts:
        e_id, e_name, day, id1, st1, en1, id2, st2, en2, ov_mins = c
        print(
            f"  [CONFLICT] {e_id} ({e_name}) on {day}: "
            f"{id1} ({st1}-{en1}) overlaps {id2} ({st2}-{en2}) by {ov_mins} mins"
        )

print("\nEMPLOYEES WITH CONFLICTS:")
for emp in conflicting_employees:
    print(f"  * {emp}")

print("\nEMPLOYEES WITH CONFLICT-FREE SCHEDULES:")
for emp in clean_employees:
    print(f"  * {emp}")
