# Case Study 06 (Q29): Password Policy Validation Engine
# Assigned Syllabus Only: variables, data types, operators, conditionals,
# loops, strings, lists, tuples, tuple operations, and unpacking.

MIN_LENGTH = 8
SPECIAL_CHARS = "!@#$%^&*()-_=+[]{}|;:',.<>?/"
PROHIBITED_WORDS = ["password", "admin", "qwerty", "1234", "welcome"]

test_passwords = [
    ("Valid Strong Password", "kiran", "K!ran@2026#"),
    ("Short + Missing Categories", "asha", "abc12"),
    ("Contains Username + Space", "rohan", "Rohan 99!"),
    ("Consecutive Repetition", "meera", "Meeera@99"),
    ("Prohibited Substring", "vivek", "MyAdmin@2026"),
    ("Valid Complex Password", "neha", "Py#9xL2m!Q"),
]

print("=" * 80)
print("PASSWORD POLICY VALIDATION ENGINE".center(80))
print("=" * 80)

passed_count = 0
failed_count = 0

for record in test_passwords:
    label, username, pwd = record
    failures = []

    # 1. Minimum length check
    if len(pwd) < MIN_LENGTH:
        failures.append("Length is " + str(len(pwd)) + " (minimum required is " + str(MIN_LENGTH) + ")")

    # 2. Character category and whitespace checks
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    has_space = False

    for ch in pwd:
        if "A" <= ch <= "Z":
            has_upper = True
        elif "a" <= ch <= "z":
            has_lower = True
        elif "0" <= ch <= "9":
            has_digit = True
        elif ch == " ":
            has_space = True
        elif ch in SPECIAL_CHARS:
            has_special = True

    if not has_upper:
        failures.append("Missing uppercase letter (A-Z)")
    if not has_lower:
        failures.append("Missing lowercase letter (a-z)")
    if not has_digit:
        failures.append("Missing numeric digit (0-9)")
    if not has_special:
        failures.append("Missing special character")
    if has_space:
        failures.append("Contains whitespace character")

    # 3. Consecutive identical character repetition check (3 or more)
    has_triple_repeat = False
    for i in range(len(pwd) - 2):
        if pwd[i] == pwd[i + 1] and pwd[i + 1] == pwd[i + 2]:
            has_triple_repeat = True
            break
    if has_triple_repeat:
        failures.append("Contains 3 or more consecutive identical characters")

    # 4. Prohibited substrings and username check (case-insensitive)
    lower_pwd = pwd.lower()
    lower_user = username.lower()
    if len(lower_user) > 0 and lower_user in lower_pwd:
        failures.append("Contains username '" + username + "'")

    for bad_word in PROHIBITED_WORDS:
        if bad_word in lower_pwd:
            failures.append("Contains prohibited substring '" + bad_word + "'")

    if len(failures) == 0:
        status = "PASS"
        passed_count = passed_count + 1
    else:
        status = "FAIL"
        failed_count = failed_count + 1

    print(f"\nTest: {label}")
    print(f"  Username : {username} | Password: {pwd} | Result: [{status}]")
    if len(failures) > 0:
        print("  Failed Conditions:")
        for reason in failures:
            print(f"    - {reason}")
    else:
        print("  All password policy requirements satisfied.")

print("\n" + "-" * 80)
print(f"SUMMARY -> Total Evaluated: {len(test_passwords)} | Passed: {passed_count} | Failed: {failed_count}")
