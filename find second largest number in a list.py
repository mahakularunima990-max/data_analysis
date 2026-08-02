#find second largest number in a list
def second_largest(numbers):
    return sorted(set(numbers))[-2]
my_list = [10, 20, 4, 45, 99]
print(sorted(my_list))
print("Second largest number is:", second_largest(my_list))
