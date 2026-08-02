#unique visitor id
# Lists of visitor IDs for two days
day1_visitors = [101, 102, 103, 104, 105]
day2_visitors = [103, 104, 106, 107]

# Convert lists to sets for set operations
day1_set = set(day1_visitors)
day2_set = set(day2_visitors)

# 1. Total unique visitors across both days
total_unique = day1_set.union(day2_set)
print("Total unique visitors:", total_unique)

# 2. Common visitors between two days
common_visitors = day1_set.intersection(day2_set)
print("Common visitors:", common_visitors)

# 3. Visitors who visited ONLY on Day 1
day1_only = day1_set.difference(day2_set)
print("Visitors only on Day 1:", day1_only)