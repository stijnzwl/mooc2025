# import math

# def create_tuple(x: int, y: int, z: int):
#     return (min(x, y, z), max(x, y, z), x + y + z)
  
# if __name__ == "__main__":
#     print(create_tuple(5, 3, -1))  
    
    
# def oldest_person(people: int):
#     year = []
#     for i in people:
#         year.append(i[1])
        
#     for i in people:
#         if i[1] == min(year):
#             return i[0]
        
        
# p1 = ("Adam", 1977)
# p2 = ("Ellen", 1985)
# p3 = ("Mary", 1953)
# p4 = ("Ernest", 1997)
# people = [p1, p2, p3, p4]

# print(oldest_person(people))


# def older_people(people: list, year: int):
#     new_list = []
#     for i in people:
#         if i[1] < year:
#             new_list.append(i[0])
#     return new_list

# p1 = ("Adam", 1977)
# p2 = ("Ellen", 1985)
# p3 = ("Mary", 1953)
# p4 = ("Ernest", 1997)
# people = [p1, p2, p3, p4]

# older = older_people(people, 1979)
# print(older)


# def add_student(dictionary: dict, student: str):
#     dictionary[student] = []

# def print_student(dictionary: dict, student: str):
#     if student not in dictionary:
#         print(f"{student}: no such person in the database")
#     else:


#         if not dictionary[student]:
#             print(f"{student}: ")
#             print(" no completed courses")
#         else:
#             print(f"{student}: ")
#             print(f" {len(dictionary[student])} completed courses:")
#             grades = []

#             for i, n in dictionary[student]:
#                 print("  " + str(i), str(n))
#                 grades.append(n)
#             print(f" average grade {sum(grades)/len(grades)}")


# def add_course(dictionary: dict, student: str, course: tuple):
#     title, grade = course
#     if grade <= 0:
#         return
#     for id, (old_title, old_grade) in enumerate(dictionary[student]):
#         if old_title == title:
#             if grade > old_grade:
#                 dictionary[student][id] = course
#             return

#     dictionary[student].append(course)
 

# def summary(dictionary: dict):
#     print(f"students {len(dictionary)}")
#     amount = 0
#     person = ''
#     for i, y in dictionary.items():
#         if len(y) >= amount:
#             amount = len(y)
#             person = i
#     print(f"most courses completed {amount} {person}")

#     best_avg = 0
#     p = ''
#     for key, value in dictionary.items():
#         total = 0
#         for item in value:
#             total += item[1]
#         average = total / len(value)
#         if average > best_avg:
#             best_avg = average
#             p = key
#     print(f"best average grade {best_avg} {p}")
            
# students = {}
# add_student(students, "Peter")
# add_student(students, "Eliza")
# add_course(students, "Peter", ("Data Structures and Algorithms", 1))
# add_course(students, "Peter", ("Introduction to Programming", 1))
# add_course(students, "Peter", ("Advanced Course in Programming", 1))
# add_course(students, "Eliza", ("Introduction to Programming", 5))
# add_course(students, "Eliza", ("Introduction to Computer Science", 4))
# summary(students)


alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
layers = 2

count = 0
# for i in range(1, layers + 1):
#     for n in range(1, i*2-1):
        


for i in range(layers*2-1):
    print(alphabet[i] * (layers*2-1))

    # print(alphabet[i] * (i*2-1))


# layers 3
# 5
# 1 3 1
# 1 1 1 1 1
# 1 3 1
# 5



# letter amount = i
# size square = (i * 2) - 1