# Case Study 02 (Q2): Progressive Electricity Billing
# Assigned Syllabus Only: variables, data types, operators, conditionals,
# loops, strings, lists, tuples, tuple operations, and unpacking.

test_cases = [
    (
        "TC-01: Normal Usage with Seasonal Spike Detection",
        "EB-4091",
        "Karthik Reddy",
        [
            ("January", 95),
            ("February", 110),
            ("March", 185),
            ("April", 420),
            ("May", 460),
            ("June", 210),
        ],
    ),
    (
        "TC-02: Zero Reading, Boundary Slabs & Invalid Reading",
        "EB-5120",
        "Lakshmi Devi",
        [
            ("July", 0),
            ("August", 100),
            ("September", 200),
            ("October", 400),
            ("November", -15),
        ],
    ),
]

FIXED_CHARGE = 120.0
SPIKE_THRESHOLD_PCT = 30.0

print("=" * 84)
print("PROGRESSIVE ELECTRICITY BILLING & ANOMALY ANALYZER".center(84))
print("=" * 84)

for case_title, consumer_id, consumer_name, monthly_readings in test_cases:
    print("\n" + "-" * 84)
    print(f"{case_title} | Consumer: {consumer_id} - {consumer_name}")
    print("-" * 84)
    print(
        f"{'Month':<11} {'Units':>7} {'Energy(INR)':>12} {'Fixed':>8} "
        f"{'Surcharge':>10} {'Rebate':>9} {'Net Bill':>11} {'Status':<14}"
    )
    print("-" * 84)

    prev_units = -1
    total_net_bill = 0.0
    valid_months = 0
    unusual_months = []

    for reading in monthly_readings:
        month_name, units = reading

        if units < 0:
            print(f"{month_name:<11} {units:>7} {'INVALID READING - SKIPPED':>55}")
            continue

        # Slab-wise energy calculation
        energy_charge = 0.0
        if units <= 100:
            energy_charge = units * 2.00
        elif units <= 200:
            energy_charge = (100 * 2.00) + ((units - 100) * 3.50)
        elif units <= 400:
            energy_charge = (100 * 2.00) + (100 * 3.50) + ((units - 200) * 5.00)
        else:
            energy_charge = (100 * 2.00) + (100 * 3.50) + (200 * 5.00) + ((units - 400) * 7.00)

        # Surcharge (10% if > 400 units) and Rebate (5% if 1..100 units)
        surcharge = 0.0
        rebate = 0.0
        if units > 400:
            surcharge = energy_charge * 0.10
        elif units > 0 and units <= 100:
            rebate = energy_charge * 0.05

        net_bill = energy_charge + FIXED_CHARGE + surcharge - rebate
        total_net_bill = total_net_bill + net_bill
        valid_months = valid_months + 1

        # Compare with previous valid month
        status = "Normal"
        if prev_units > 0:
            pct_change = ((units - prev_units) / prev_units) * 100.0
            if pct_change >= SPIKE_THRESHOLD_PCT:
                status = f"SPIKE (+{pct_change:.1f}%)"
                unusual_months.append((month_name, prev_units, units, pct_change))
        elif prev_units == 0 and units > 0:
            status = "Usage Resumed"

        prev_units = units

        print(
            f"{month_name:<11} {units:>7} {energy_charge:>12.2f} {FIXED_CHARGE:>8.2f} "
            f"{surcharge:>10.2f} {rebate:>9.2f} {net_bill:>11.2f} {status:<14}"
        )

    print("-" * 84)
    if valid_months > 0:
        avg_bill = total_net_bill / valid_months
        print(f"Total Valid Months: {valid_months} | Cumulative Bill: INR {total_net_bill:.2f} | Average Bill: INR {avg_bill:.2f}")
    if len(unusual_months) > 0:
        print("Unusual Consumption Increases (>= 30% MoM):")
        for spike in unusual_months:
            m_name, p_u, c_u, pct = spike
            print(f"  * {m_name}: {p_u} -> {c_u} units (+{pct:.1f}%)")
    else:
        print("Unusual Consumption Increases: None detected.")
