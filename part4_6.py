def everything_reversed(str_lst):
    new_lst = []
    for i in str_lst:
        new_lst.append(i[::-1])
        
    return new_lst[::-1]

my_list = ["Hi", "there", "example", "one more"]
new_list = everything_reversed(my_list)
print(new_list)
  
  
def most_common_character(string):
    x = 0
    letter = ''
    for i in range(len(string)):
        num = string.count(string[i])
        if num > x:
            x = num
            letter = string[i]
            
    return letter


first_string = "abcdbde"
print(most_common_character(first_string))

second_string = "exemplaryelementary"
print(most_common_character(second_string))   


def no_vowels(string):
    vowels = 'iaeuo'
    new_word = ''
    for i in string:
        if i in vowels:
            continue
        else:
            new_word += i
    return new_word

my_string = "this is an example"
print(no_vowels(my_string))

def no_shouting(str_lst):
    new_lst = []
    for i in str_lst:
        if i.isupper():
            continue
        else:
            new_lst.append(i)     
    return new_lst

my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
pruned_list = no_shouting(my_list)
print(pruned_list)  


def longest_series_of_neighbours(lst):
    counts = []
    count = 0
    for i in range(len(lst)):
        if i < len(lst) - 1 and (lst[i] == lst[i + 1] + 1 or lst[i] == lst[i + 1] - 1):
            count += 1
            counts.append(count)
        else:
            count += 1
            counts.append(count)
            count = 0
            continue
    return max(counts)

my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
print(longest_series_of_neighbours(my_list))

def exercise_points(data):
    point_lst = data.split()
    exercise_points = 0
    lst = [1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1]  
    for i in lst:
        if int(point_lst[1]) / 100 >= i:
            exercise_points += (10 * i)
            break     
    return int(exercise_points)

def exam_points(data):
    point_lst = data.split()
    exam_points = point_lst[0]
    return int(exam_points)

def grade_calculator(exam_points, exercise_points):
    total_points = exam_points + exercise_points
    if exam_points < 10:
        return 0
    elif total_points >= 0 and total_points <= 14:
        return 0
    elif total_points >= 15 and total_points <= 17:
        return 1
    elif total_points >= 18 and total_points <= 20:
        return 2
    elif total_points >= 21 and total_points <= 23:
        return 3
    elif total_points >= 24 and total_points <= 27:
        return 4
    elif total_points >= 28 and total_points <= 30:
        return 5
    
def print_results(grades_lst, points_lst):
    numbers = [5, 4, 3, 2, 1, 0]
    print(f"Points average: {sum(points_lst) / len(points_lst):.1f}")
    print(f"Pass percentage: {(1 - (grades_lst.count(0) / len(grades_lst))) * 100:.1f}")
    
    for i in numbers:
        print(f"{i}: {grades.count(i) * '*'}")

grades = []
points = []
data_lst = []

while True:
    data = str(input("Exam points and exercises completed: "))
    if data == '':
        print("Statistics:")
        for i in data_lst:
            points.append(exercise_points(i) + exam_points(i))
            grades.append(grade_calculator(exam_points(i), exercise_points(i)))
   
        print_results(grades, points)
        break
    data_lst.append(data)
    
    