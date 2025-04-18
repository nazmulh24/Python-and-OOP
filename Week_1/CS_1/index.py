"""
a = 10
b = 10
# --> If value same then memory address will be same...
print(id(a))
print(id(b))
"""

""" 
# --> String modify
c = "Rahim"
c = list(c)
c[0] = "K"
# c = "_".join(c)  # -> For loop er moto kaj kore..
c = "".join(c)  # -> For loop er moto kaj kore..
print(c)
"""

""" 
dict1 = {"karim": 10, "Rahim": 23, "Akkas": 2}
dict2 = {"karim": 7, "Rahim": 4, "Kuddus": 4}

result = dict1

for key, value in dict2.items():
    result[key] = result.get(key, 0) + value

print(result)
 """


# ----> lambda function
