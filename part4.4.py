# string = str(input("Please type in a string: "))

# for i in string:
#     print(i)
#     print("*")
    
    
# positive_int = int(input("Please type in a positive integer: "))

# for i in range(-positive_int, positive_int + 1):
#     if i == 0:
#         continue
#     else:
#         print(i)


def list_of_stars(int_lst):
    for x in int_lst:
        print(x * '*')
        
list_of_stars([3, 7, 1, 1, 2])


def anagrams(string1, string2):
    if sorted(string1) == sorted(string2):
        return True
    else:
        return False
    
print(anagrams("tame", "meta")) # True
print(anagrams("tame", "mate")) # True
print(anagrams("tame", "team")) # True
print(anagrams("tabby", "batty")) # False
print(anagrams("python", "java")) # False


def palindromes(string):
    palindrome = ''
    
    for i in reversed(range(len(string))):
        palindrome += string[i]
    if string == palindrome:
        return True
    else:
        return False
    
# while True:
#     word = str(input("Please type in a palindrome: "))
#     if palindromes(word):
#         print(f"{word} is a palindrome!")
#         break
#     else:
#         print("that wasn't a palindrome")

def sum_of_positives(int_lst):
    sum = 0
    for i in int_lst:
        if i > 0:
            sum += i
        else:
            continue
    return sum

my_list = [1, -2, 3, -4, 5]
result = sum_of_positives(my_list)
print("The result is", result)
        

def even_numbers(int_lst):
    new_lst = []
    for i in int_lst:
        if i % 2 == 0:
            new_lst.append(i)
        else:
            continue
    return new_lst
        
my_list = [1, 2, 3, 4, 5]
new_list = even_numbers(my_list)
print("original", my_list)
print("new", new_list)


def list_sum(int_lst1, int_lst2):
    new_lst = []
    for i in range(len(int_lst1)):
        new_lst.append(int_lst1[i] + int_lst2[i])
    return new_lst

a = [1, 2, 3]
b = [7, 8, 9]
print(list_sum(a, b)) # [8, 10, 12]


def distinct_numbers(int_lst):
    new_list = []
    for i in int_lst:
        if i not in new_list:
            print("hi")
            new_list.append(i)
        else:
            continue

    return sorted(new_list)

my_list = [3, 2, 2, 1, 3, 3, 1]
print(distinct_numbers(my_list)) # [1, 2, 3]


def length_of_longest(my_list):
    longest_word = ''
    
    for i in my_list:
        if len(i) > len(longest_word):
            longest_word = i
            
    return len(longest_word)

my_list = ["first", "second", "fourth", "eleventh"]

result = length_of_longest(my_list)
print(result)

my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

result = length_of_longest(my_list)
print(result)

