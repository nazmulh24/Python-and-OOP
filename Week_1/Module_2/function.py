"""

# def sum(numbers):  # --> Through an error..
#     print(numbers)


# def sum(*args):
#     print(args)


# num = sum(23, 56)


def display_person(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


display_person(Name="Amir Khan", Age="45")

"""


# define
def double_it(num):
    result = num * 2
    print("inside the function.py file", result)
    return result


double_it(8)
double_it(88)


def sum(num1, num2):
    result = num1 + num2
    return result


total = sum(44, 39)
print("total value", total)

final = double_it(total)
print("final value", final)
