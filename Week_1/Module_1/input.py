# num = int(input("Enter number : "))

# print(num)
# print(type(num))

# ---------------------------------------------------------------

# print('Now I need money')
# input()
# input('Give me some money: ')

# money = input('Give me some money: ')
# print("here is your money", money)

first_money = input("Kodom Ali, Dosto kichu taka dey: ")
second_money = input("Peyara begum, dosto kichu taka dey: ")

print(type(first_money))

# by default the input from user will be string type:
print("money I got from Kodom", first_money, "and from peyara", second_money)

first_money_int = int(first_money)
second_money_int = int(second_money)

# print(type(first_money_int))
# total = first_money + second_money

total = first_money_int + second_money_int
print("total money i got: ", total)

""" 
1. convert number to string: str
    num = 123
    num_str = str(num)
    print(num_str)       # Output: "123"
    print(type(num_str)) # Output: <class 'str'>

2. convert decimal number: float
    num_str = "45.67"
    num_float = float(num_str)
    print(num_float)       # Output: 45.67
    print(type(num_float)) # Output: <class 'float'>
    
3. python int vs float
    Feature       |         int            |             float
    
    Represents    |      Whole numbers     |    Decimal (floating-point) numbers
    Example       |       5, -3, 1000      |      3.14, -0.001, 2.0
    Conversion    |    int("10") -> 10     |    float("10.5") -> 10.5
    Use case      |  Countable quantities  |    Measurements, precision-based calculations

"""
