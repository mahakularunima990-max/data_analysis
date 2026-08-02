#student management system
# Dictionary to store student records {Name: Marks}
students = {}

# 1. Add students
students["Alice"] = 85
students["Bob"] = 70
students["Charlie"] = 92
print("After adding students:", students)

# 2. Update marks
students["Bob"] = 82
print("After updating Bob's marks:", students)

# 3. Delete a student
del students["Alice"]
print("After deleting Alice:", students)

# 4. Search by name
search_name = "Charlie"
if search_name in students:
    print(f"Found {search_name} with marks: {students[search_name]}")
else:
    print(f"{search_name} not found.")