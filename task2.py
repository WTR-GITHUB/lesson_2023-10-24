# 2) Create a program which takes 5 random number per 1 input.The create a
# function which takes the sum of those numbers (lets agree argument is being
# called 'num_sum'),and all those 5 numbers as separate free arguments as well.
# Multiply all those numbers with with the num_sum you calculated in a list
# data structure.

def numbers_action(num_sum: int, *argum) -> int:
    num_multy: int = 1
    for item in argum:
        num_multy *= item
    return num_multy*num_sum

user_numbers = input("Please enter 5 numbers seperated with ',' char: ")
num_list = [int(num) for num in user_numbers.split(",")]
num_list_sum = sum(num_list)
print(numbers_action(num_list_sum, *num_list))


# from typing import List

# def sum_and_multiply(numbers: str) -> List[int]:
#     number_list: list = [int(x) for x in numbers.split(",")]
#     num_sum: int = sum(number_list)
#     num_multiply: list = [x * num_sum for x in number_list]
#     return num_multiply

# my_numbers: str = "3,2,6,1,8"
# print(sum_and_multiply(my_numbers))