import math
from num2words import num2words


def times_ten(start_index: int, end_index: int):
    new_dict = {}
    for i in range(start_index, end_index + 1):
        new_dict[i] = i * 10
    return new_dict


d = times_ten(3, 6)
print(d)


def factorials(n: int):
    new_dict = {}
    for i in range(n + 1):
        new_dict[i] = math.factorial(i)
    return new_dict

k = factorials(5)
print(k[1])
print(k[3])
print(k[5])


def histogram(string):
    new_dict = {}
    for i in string:
        if i not in new_dict:
            new_dict[i] = ""
        new_dict[i] += "*"
        
    for key, value in new_dict.items():
        print(key, value)
    
histogram("statistically")


# phonebook = {}
# while True:
#     command = input("command (1 search, 2 add, 3 quit): ")
#     if str(command) == "3":
#         print("quitting...")
#         break
#     elif str(command) == "2":
#         name = input("name: ")
#         number = input("number: ")
#         if name and number:
#             phonebook[name] = number
#             print('ok!')
#         else:
#             continue
        
#     elif str(command) == "1":
#         search = input("name: ")
#         if search in phonebook:
#            print(phonebook[search]) 
#         else:
#             print('no number')

# phonebook = {}
# while True:
#     command = input("command (1 search, 2 add, 3 quit): ")
#     if str(command) == "3":
#         print("quitting...")
#         break
#     elif str(command) == "2":
#         name = input("name: ")
#         number = input("number: ")
#         if name and number:
#             if name in phonebook:
#                 phonebook[name].append(number)
#                 print('ok!')
#             else:
#                 phonebook[name] = [number]
#                 print('ok!')
#         else:
#             continue
        
#     elif str(command) == "1":
#         search = input("name: ")
#         if search in phonebook:
#            for i in phonebook[search]:
#                print(i)
#         else:
#             print('no number')
            

def invert(dictionary: dict):
    new_dict = {}
    for x, y in dictionary.items():
        new_dict[y] = x
    dictionary.clear()
    for x, y in new_dict.items():
        dictionary[x] = y
              
s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
invert(s)
print(s)  

def dict_of_numbers():
    new_dict = {}
    for i in range(100):
        new_dict[i] = num2words(i)
    return new_dict

numbers = dict_of_numbers()
print(numbers[2])
print(numbers[11])
print(numbers[45])
print(numbers[99])
print(numbers[0])


def add_movie(database: list, name: str, director: str, year: int, runtime: int):
    new_dict = {}
    new_dict["name"] = name
    new_dict["director"] = director
    new_dict["year"] = year
    new_dict["runtime"] = runtime
    database.append(new_dict)
    
# database = []
# add_movie(database, "Gone with the Python", "Victor Pything", 2017, 116)
# add_movie(database, "Pythons on a Plane", "Renny Pytholin", 2001, 94)
# print(database)


def find_movies(database: list, search_term: str):
    new_list = []
    for i in database:
        if search_term.lower() in i["name"].lower():
            new_list.append(i)
    return new_list


database = [{"name": "Gone with the Python", "director": "Victor Pything", "year": 2017, "runtime": 116},
{"name": "Pythons on a Plane", "director": "Renny Pytholin", "year": 2001, "runtime": 94},
{"name": "Dawn of the Dead Programmers", "director": "M. Night Python", "year": 2011, "runtime": 101}]

my_movies = find_movies(database, "python")
print(my_movies)