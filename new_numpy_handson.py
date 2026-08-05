import numpy as np

students = np.array([
    [101, 18, 78, 82, 75, 88],
    [102, 19, 91, 89, 93, 95],
    [103, 18, 65, 70, 68, 72],
    [104, 20, 88, 85, 90, 87],
    [105, 19, 76, 79, 81, 80],
    [106, 18, 84, 83, 86, 89],
    [107, 20, 69, 72, 74, 70],
    [108, 19, 95, 94, 96, 98],
    [109, 18, 58, 62, 60, 65],
    [110, 20, 82, 80, 84, 83],
    [111, 19, 73, 75, 71, 74],
    [112, 18, 89, 91, 90, 92],
    [113, 20, 67, 69, 70, 68],
    [114, 19, 85, 87, 86, 88],
    [115, 18, 79, 81, 80, 82],
    [116, 20, 92, 93, 94, 95],
    [117, 19, 61, 64, 63, 66],
    [118, 18, 87, 85, 88, 90],
    [119, 20, 74, 76, 75, 78],
    [120, 19, 90, 92, 91, 94]
])
print(students)
print("Shape of the array:", students.shape)
print("Data type of the array:", students.dtype)
print("Number of dimensions:", students.ndim)
print("Size of the array:", students.size)
print("Memory size of each element in bytes:", students.itemsize)
print("Accessing the first row:", students[0])
print("Accessing the last row:", students[-1])
print("Accessing the first column:", students[:, 0])
print("Accessing the last column:", students[:, -1])
print("Slicing:", students[1:4, 2:5])
print("Reshaping the array to 5x6:", students.reshape(8,15))
print("Mean of the scores:", np.mean(students))
print("Standard deviation of the scores:", np.std(students))
print("Sum of the scores:", np.sum(students))
print("Maximum score:", np.max(students))
print("Minimum score:", np.min(students))
print("Median of the scores:", np.median(students))

