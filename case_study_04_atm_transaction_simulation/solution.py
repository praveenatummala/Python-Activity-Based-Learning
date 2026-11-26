# Case Study 04 (Q13): ATM Transaction Sequence Simulation
# Assigned Syllabus Only: variables, data types, operators, conditionals,
# loops, strings, lists, tuples, tuple operations, and unpacking.

scenarios = [
    (
        "TC-01: Mixed Deposits, Valid Withdrawals & Limit Enforcement",
        15000,   # Opening balance (INR)
        10000,   # Per-transaction withdrawal limit
        20000,   # Daily withdrawal limit
        [
            ("TXN01", "deposit", 5000),
            ("TXN02", "withdraw", 8000),
            ("TXN03", "withdraw", 12000),  # Exceeds per-txn limit
            ("TXN04", "withdraw", 4550),   # Not a multiple of 100
            ("TXN05", "withdraw", 9000),
            ("TXN06", "withdraw", 4000),   # Exceeds daily limit (8000+9000+4000=21000)
            ("TXN07", "deposit", -500),    # Invalid negative amount
            ("TXN08", "transfer", 1000),   # Unsupported type
            ("TXN09", "withdraw", 3000),   # Valid: total daily = 20000, balance = 0
        ],
    ),
    (
        "TC-02: Insufficient Balance Check",
        2000,
        5000,
        10000,
        [
            ("TXN11", "withdraw", 2500),
            ("TXN12", "deposit", 1000),
            ("TXN13", "withdraw", 2500),
        ],
    ),
]

print("=" * 80)
print("ATM TRANSACTION SEQUENCE SIMULATION".center(80))
print("=" * 80)

for title, opening_balance, per_txn_limit, daily_limit, txns in scenarios:
    print("\n" + "-" * 80)
    print(title)
    print(
        f"Opening Balance: INR {opening_balance} | Per-Txn Limit: INR {per_txn_limit} | "
        f"Daily Limit: INR {daily_limit}"
    )
    print("-" * 80)
    print(f"{'TxnID':<8} {'Type':<10} {'Amount':>9} {'Status':<10} {'Balance':>10}  {'Remarks'}")
    print("-" * 80)

    balance = opening_balance
    daily_withdrawn = 0
    total_deposited = 0
    accepted_count = 0
    rejected_count = 0
    rejected_records = []

    for txn in txns:
        txn_id, raw_type, amount = txn
        txn_type = raw_type.strip().upper()
        accepted = False
        remark = ""

        if amount <= 0:
            remark = "Rejected: Amount must be positive"
        elif txn_type == "DEPOSIT":
            balance = balance + amount
            total_deposited = total_deposited + amount
            accepted = True
            remark = "Cash deposited successfully"
        elif txn_type == "WITHDRAW":
            if amount % 100 != 0:
                remark = "Rejected: Amount must be multiple of 100"
            elif amount > per_txn_limit:
                remark = "Rejected: Exceeds per-transaction limit"
            elif daily_withdrawn + amount > daily_limit:
                remark = "Rejected: Exceeds daily withdrawal limit"
            elif amount > balance:
                remark = "Rejected: Insufficient account balance"
            else:
                balance = balance - amount
                daily_withdrawn = daily_withdrawn + amount
                accepted = True
                remark = "Cash dispensed successfully"
        else:
            remark = "Rejected: Unsupported transaction type"

        if accepted:
            accepted_count = accepted_count + 1
            status_label = "ACCEPTED"
        else:
            rejected_count = rejected_count + 1
            status_label = "REJECTED"
            rejected_records.append((txn_id, txn_type, amount, remark))

        print(f"{txn_id:<8} {txn_type:<10} {amount:>9} {status_label:<10} {balance:>10}  {remark}")

    print("-" * 80)
    print("TRANSACTION SUMMARY:")
    print(f"  Opening Balance   : INR {opening_balance}")
    print(f"  Total Deposited   : INR {total_deposited}")
    print(f"  Total Withdrawn   : INR {daily_withdrawn}")
    print(f"  Closing Balance   : INR {balance}")
    print(f"  Accepted / Rejected: {accepted_count} accepted, {rejected_count} rejected")
