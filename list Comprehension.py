#list Comprehension
def square_numbers(numbers):
    return [x**2 for x in numbers]

my_list = [1, 2, 3, 4, 5,6,7,8,9,10]
print(square_numbers(my_list))