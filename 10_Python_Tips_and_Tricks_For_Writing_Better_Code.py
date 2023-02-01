print('source: https://www.youtube.com/watch?v=C-gEQdGVXbk&ab_channel=CoreySchafer')


# --------------------------------------------------------------------------------------------------------
# Tip: Using ternary conditions
# --------------------------------------------------------------------------------------------------------
# condition = False
#
# x = 1 if condition else 0
# print(x)
# --------------------------------------------------------------------------------------------------------
# Tip: Using "_" as seperator for big numbers
# --------------------------------------------------------------------------------------------------------
# num1 = 10000000
# num2 = 2000000
# print(num1 + num2)
#
# num3 = 10_000_000
# num4 = 2_000_000
# print(num3 + num4)
# # --------------------------
# # Todo: Usage of f strings?
# # print(f’totalAmount:,’)

# --------------------------------------------------------------------------------------------------------
# Tip: Usage of context managers when dealing with a resource (file, database, threads etc..)
# --------------------------------------------------------------------------------------------------------
# with open("test.txt", 'r') as fptr:
#     file_contents = fptr.readlines()
#
# line_counts = len(file_contents)
# print(line_counts)
# --------------------------------------------------------------------------------------------------------
# Tip: Usage of "enumarate" and "zip" functions
# --------------------------------------------------------------------------------------------------------
# list1 = ['Peter Parker', 'Clark Kent', 'Wade Wilson', 'Bruce Wayne']
# list2 = ['Spiderman', 'Superman', 'Deadpool', 'batman']
# list3 = ['Marvel', 'DC', 'Marvel', 'DC']
#
# for index, item in enumerate(list1):
#     print(index, item)
#
# print("\n")
# for index, item in enumerate(list1):
#     print("{}'s name is {}".format(list2[index], item))
#
# print("\n")
# # zip function matches element with same index from given lists
# for hero, name in zip(list2, list1):
#     print(f"{hero}'s name is {name}")
#
# print("\n")
# for hero, name, universe in zip(list2, list1, list3):
#     print(f"{hero}'s name is {name} and he is from {universe}")
    
# --------------------------------------------------------------------------------------------------------
# Tip: packing and unpacking
# --------------------------------------------------------------------------------------------------------
# a, b = (1, 2)
# print('a: {}\nb: {}\n'.format(a, b))
# # --------------------------
# # to neglect unused variable
# a, _ = (1, 2)
# print(a)
# # --------------------------
# # a, b, c = (1, 2, 3, 4, 5)  # error
# # a, b, c = (1, 2)           # error
# a, b, *c = (1, 2, 3, 4, 5)
# print('a: {}\nb: {}\nc: {}'.format(a, b, c))
#
# # ignoring multiple values
# a, b, *_ = (1, 2, 3, 4, 5)
# print('a: {}\nb: {}\nc: {}'.format(a, b, c))

# --------------------------------------------------------------------------------------------------------
# Tip: Getting and Setting certain attributes
# --------------------------------------------------------------------------------------------------------
# we can dynamically add attributes and values to objects


class Person:
    pass


# --------------------------
# person = Person()
# person.firstName = "Furkan"
# person.lastName = "Yilmaz"
#
# print("name:{}\nsurname:{}".format(person.firstName, person.lastName))
# --------------------------
# person = Person()
# first_key = "firstName"
# first_val = "Furkan"
#
# # setattr and getattr are useful when checking or setting various objects and their attributes
# setattr(person, first_key, first_val)
# print(getattr(person, first_key))
# --------------------------
# # example
# person = Person()
# person_info = {'firstName': 'Furkan', 'lastName': 'Yilmaz'}
#
# for key, val in person_info.items():
#     setattr(person, key, val)
#
# for key in person_info.keys():
#     print(getattr(person, key))

# --------------------------------------------------------------------------------------------------------
# Tip: Inputting secret information
# --------------------------------------------------------------------------------------------------------
# from getpass import getpass
# # It is not working as Corey showed but this module can be further investigated.
# username = input("Username: ")
# password = getpass('asd', 'asdsasd')
#
# print("Logging In...")

# --------------------------------------------------------------------------------------------------------
# Tip: "-m" search sys.path
# --------------------------------------------------------------------------------------------------------
# py -3 -m venv my_venv

