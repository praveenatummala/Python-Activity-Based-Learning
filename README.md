# Python Activity-Based Learning

A curated collection of **10 complete Python case studies** developed strictly using the assigned foundational Python syllabus:

> **Assigned Syllabus:** Computational thinking, algorithms, flowcharts, pseudocode, variables, data types, operators, conditional statements, loops, strings, pattern generation, lists, nested lists, tuples, tuple operations, and tuple unpacking.

Every case study strictly avoids out-of-syllabus constructs (no custom `def` functions, dictionaries, sets, classes, comprehensions, lambdas, exception blocks, or external imports) and includes all **10 mandatory deliverables**:

1. Problem Statement
2. Objectives
3. Assumptions
4. Algorithm
5. Flowchart (Mermaid diagram)
6. Pseudocode
7. Python Source Code (`solution.py`)
8. Test Cases
9. Output Screenshots (`output_screenshot.png` captured from Python 3.12.7 execution)
10. Conclusion

---

## Selected 10 Case Studies

| # | PDF Q# | Case Study Title | Primary Syllabus Concepts | Folder & Docs |
| :---: | :---: | :--- | :--- | :--- |
| 01 | Q1 | University Scholarship Allocation | Conditionals, Lists, Tuples, Unpacking, Manual Bubble Sort | [`case_study_01_university_scholarship_allocation`](./case_study_01_university_scholarship_allocation/README.md) |
| 02 | Q2 | Progressive Electricity Billing | Slab Conditionals, Arithmetic, Loops, Tuples, Anomaly Detection | [`case_study_02_progressive_electricity_billing`](./case_study_02_progressive_electricity_billing/README.md) |
| 03 | Q4 | Employee Payroll and Deduction Analysis | Progressive Tax Slabs, String Formatting, Tuples, Unpacking | [`case_study_03_employee_payroll_deduction`](./case_study_03_employee_payroll_deduction/README.md) |
| 04 | Q13 | ATM Transaction Sequence Simulation | State Loops, Multi-Rule Validation, Lists, Tuple Unpacking | [`case_study_04_atm_transaction_simulation`](./case_study_04_atm_transaction_simulation/README.md) |
| 05 | Q27 | Advanced Numeric Pattern Generator | Pattern Generation, Nested Loops, String Spacing, Validation | [`case_study_05_numeric_pattern_generator`](./case_study_05_numeric_pattern_generator/README.md) |
| 06 | Q29 | Password Policy Validation Engine | String Indexing, Character Scanning, Loops, Rule Lists | [`case_study_06_password_policy_validation`](./case_study_06_password_policy_validation/README.md) |
| 07 | Q31 | String-Based Examination Answer Evaluation | String Methods, Indexing, Negative Marking, Tuples | [`case_study_07_exam_answer_evaluation`](./case_study_07_exam_answer_evaluation/README.md) |
| 08 | Q42 | Student Marks Matrix Analysis | 2D Nested Lists, Nested Loops, Row & Column Analytics | [`case_study_08_student_marks_matrix`](./case_study_08_student_marks_matrix/README.md) |
| 09 | Q48 | Tuple-Based Employee Shift Conflict Detection | Tuples, String Splitting, Pairwise Nested Loops, Intervals | [`case_study_09_employee_shift_conflict`](./case_study_09_employee_shift_conflict/README.md) |
| 10 | Q50 | Tuple-Based Route Distance Analysis | Coordinate Tuples, Unpacking, Arithmetic Operators, Loops | [`case_study_10_route_distance_analysis`](./case_study_10_route_distance_analysis/README.md) |

---

## Repository Structure

```text
Python-Activity-Based-Learning/
├── README.md
├── case_study_01_university_scholarship_allocation/
│   ├── README.md
│   ├── solution.py
│   └── output_screenshot.png
├── case_study_02_progressive_electricity_billing/
│   ├── README.md
│   ├── solution.py
│   └── output_screenshot.png
...
└── case_study_10_route_distance_analysis/
    ├── README.md
    ├── solution.py
    └── output_screenshot.png
```

---

## How to Run Any Solution

Each `solution.py` script runs standalone in Python 3 with built-in test scenarios and zero external dependencies:

```bash
python case_study_01_university_scholarship_allocation/solution.py
```

---

## Syllabus Compliance Checklist

- [x] **Only assigned syllabus constructs used** (`variables`, `data types`, `operators`, `if/elif/else`, `for/while` loops, `strings`, `pattern generation`, `lists`, `nested lists`, `tuples`, `tuple operations`, `unpacking`)
- [x] **No** `def` functions, `dict`, `set`, `class`, `lambda`, list comprehensions, `try/except`, or `import` statements
- [x] All 10 case studies executed and verified on **Python 3.12.7** with real output screenshots included
