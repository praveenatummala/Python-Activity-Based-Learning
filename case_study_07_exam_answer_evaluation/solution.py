# Case Study 07 (Q31): String-Based Examination Answer Evaluation
# Assigned Syllabus Only: variables, data types, operators, conditionals,
# loops, strings, lists, tuples, tuple operations, and unpacking.

ANSWER_KEY = "ABCDABCDAB"
MARKS_CORRECT = 4.0
MARKS_WRONG = -1.0
MARKS_UNANSWERED = 0.0
PASS_PCT = 40.0
VALID_OPTIONS = "ABCD-"

student_submissions = [
    ("24CS001", "Aditi Rao", "ABCDABCDAB"),
    ("24CS002", "Bharath K", "abcdab--ab"),
    ("24CS003", "Charan V", "AAAAABBBBB"),
    ("24CS004", "Divya S", "ABCDABCDAA"),
    ("24CS005", "Eshwar M", "ABCDABC"),       # Length mismatch
    ("24CS006", "Farah Z", "ABCDXBCDAB"),    # Invalid option character
]

total_questions = len(ANSWER_KEY)
max_score = total_questions * MARKS_CORRECT

print("=" * 84)
print("STRING-BASED EXAMINATION ANSWER EVALUATION".center(84))
print("=" * 84)
print(
    f"Answer Key: {ANSWER_KEY} ({total_questions} Qs) | Max Score: {max_score:.1f} | "
    f"Scheme: +{MARKS_CORRECT:.1f} / {MARKS_WRONG:.1f} / {MARKS_UNANSWERED:.1f}"
)
print("-" * 84)
print(f"{'RollNo':<9} {'Name':<13} {'Correct':>7} {'Wrong':>6} {'Blank':>6} {'Score':>8} {'Pct(%)':>8} {'Grade':>6} {'Status'}")
print("-" * 84)

valid_scores = []
pass_count = 0
invalid_records = []

for submission in student_submissions:
    roll_no, name, raw_answers = submission
    answers = raw_answers.strip().upper()

    # Validate answer string length and characters
    if len(answers) != total_questions:
        invalid_records.append((roll_no, name, f"Expected {total_questions} responses, got {len(answers)}"))
        print(f"{roll_no:<9} {name:<13} {'INVALID SUBMISSION (Length Mismatch)':>60}")
        continue

    invalid_char = False
    bad_ch = ""
    for ch in answers:
        if ch not in VALID_OPTIONS:
            invalid_char = True
            bad_ch = ch
            break

    if invalid_char:
        invalid_records.append((roll_no, name, f"Invalid option character '{bad_ch}'"))
        print(f"{roll_no:<9} {name:<13} {'INVALID SUBMISSION (Bad Character)':>60}")
        continue

    correct = 0
    wrong = 0
    blank = 0

    for i in range(total_questions):
        ans_ch = answers[i]
        key_ch = ANSWER_KEY[i]
        if ans_ch == "-":
            blank = blank + 1
        elif ans_ch == key_ch:
            correct = correct + 1
        else:
            wrong = wrong + 1

    score = (correct * MARKS_CORRECT) + (wrong * MARKS_WRONG) + (blank * MARKS_UNANSWERED)
    if score < 0:
        pct = 0.0
    else:
        pct = (score / max_score) * 100.0

    if pct >= 85.0:
        grade = "A+"
    elif pct >= 70.0:
        grade = "A"
    elif pct >= 55.0:
        grade = "B"
    elif pct >= PASS_PCT:
        grade = "C"
    else:
        grade = "F"

    if pct >= PASS_PCT:
        status = "PASS"
        pass_count = pass_count + 1
    else:
        status = "FAIL"

    valid_scores.append((roll_no, name, score, pct))
    print(f"{roll_no:<9} {name:<13} {correct:>7} {wrong:>6} {blank:>6} {score:>8.1f} {pct:>8.2f} {grade:>6} {status}")

print("-" * 84)
if len(valid_scores) > 0:
    score_sum = 0.0
    top_score = valid_scores[0][2]
    for rec in valid_scores:
        r_no, r_name, sc, p = rec
        score_sum = score_sum + sc
        if sc > top_score:
            top_score = sc

    top_students = []
    for rec in valid_scores:
        r_no, r_name, sc, p = rec
        if sc == top_score:
            top_students.append(r_name + " (" + r_no + ")")

    avg_score = score_sum / len(valid_scores)
    print(f"Valid Evaluated : {len(valid_scores)} | Passed: {pass_count} | Failed: {len(valid_scores) - pass_count}")
    print(f"Class Average   : {avg_score:.2f} / {max_score:.1f}")
    print(f"Top Performer(s): {', '.join(top_students)} with {top_score:.1f} marks")
if len(invalid_records) > 0:
    print("Invalid Records Flagged:")
    for inv in invalid_records:
        r_no, r_name, err = inv
        print(f"  - {r_no} ({r_name}): {err}")
