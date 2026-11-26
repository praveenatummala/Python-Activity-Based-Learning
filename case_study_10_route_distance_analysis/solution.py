# Case Study 10 (Q50): Tuple-Based Route Distance Analysis
# Assigned Syllabus Only: variables, data types, operators, conditionals,
# loops, strings, lists, tuples, tuple operations, and unpacking.

# Route tuple format: (route_id, route_name, [(point_name, x_km, y_km), ...])
routes = [
    (
        "RT-01",
        "Campus Logistics Loop",
        [
            ("Main Gate", 0.0, 0.0),
            ("Academic Block", 3.0, 4.0),
            ("Central Library", 6.0, 4.0),
            ("Hostel Complex", 10.0, 7.0),
            ("Sports Arena", 10.0, 1.0),
        ],
    ),
    (
        "RT-02",
        "City Express Shuttle",
        [
            ("Railway Station", 1.0, 2.0),
            ("Tech Park", 7.0, 10.0),
            ("Airport Terminal", 19.0, 15.0),
        ],
    ),
    (
        "RT-03",
        "Incomplete Single-Stop Route",
        [
            ("Depot", 2.0, 3.0),
        ],
    ),
]

print("=" * 80)
print("TUPLE-BASED ROUTE DISTANCE ANALYSIS".center(80))
print("=" * 80)

route_summaries = []

for route in routes:
    route_id, route_name, waypoints = route
    print("\n" + "-" * 80)
    print(f"Route: {route_id} - {route_name} (Waypoints: {len(waypoints)})")
    print("-" * 80)

    if len(waypoints) < 2:
        print("  [INVALID ROUTE] At least 2 coordinate points are required to compute segments.")
        continue

    print(f"  {'Segment':<34} {'From (x, y)':<16} {'To (x, y)':<16} {'Dist (km)':>10}")
    print("  " + "-" * 78)

    total_distance = 0.0
    longest_segment_name = ""
    longest_distance = -1.0
    shortest_segment_name = ""
    shortest_distance = -1.0

    for i in range(len(waypoints) - 1):
        p1_name, x1, y1 = waypoints[i]
        p2_name, x2, y2 = waypoints[i + 1]

        dx = x2 - x1
        dy = y2 - y1
        segment_dist = ((dx * dx) + (dy * dy)) ** 0.5
        total_distance = total_distance + segment_dist

        seg_label = p1_name + " -> " + p2_name
        from_str = "(" + str(x1) + ", " + str(y1) + ")"
        to_str = "(" + str(x2) + ", " + str(y2) + ")"

        print(f"  {seg_label:<34} {from_str:<16} {to_str:<16} {segment_dist:>10.2f}")

        if longest_distance < 0 or segment_dist > longest_distance:
            longest_distance = segment_dist
            longest_segment_name = seg_label

        if shortest_distance < 0 or segment_dist < shortest_distance:
            shortest_distance = segment_dist
            shortest_segment_name = seg_label

    avg_segment = total_distance / (len(waypoints) - 1)
    print("  " + "-" * 78)
    print(f"  Total Route Distance : {total_distance:.2f} km")
    print(f"  Average Segment      : {avg_segment:.2f} km")
    print(f"  Longest Segment      : {longest_segment_name} ({longest_distance:.2f} km)")
    print(f"  Shortest Segment     : {shortest_segment_name} ({shortest_distance:.2f} km)")

    route_summaries.append((route_id, route_name, total_distance, longest_segment_name, longest_distance))

print("\n" + "=" * 80)
print("ROUTE COMPARISON SUMMARY".center(80))
print("=" * 80)
if len(route_summaries) > 0:
    max_route = route_summaries[0]
    for summary in route_summaries:
        r_id, r_name, t_dist, l_seg, l_dist = summary
        print(f"  {r_id} ({r_name}): Total = {t_dist:.2f} km | Longest Leg = {l_seg} ({l_dist:.2f} km)")
        if t_dist > max_route[2]:
            max_route = summary
    print(f"\nLongest Overall Route: {max_route[0]} - {max_route[1]} ({max_route[2]:.2f} km)")
