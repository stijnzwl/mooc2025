# lst = [1, 2, 3, 4, 5]
# # while True:
# #     index = int(input())
# #     if index == -1:
# #         break
# #     new_value = int(input())
# #     lst[index] = new_value
# #     print(lst)
    
    
# lst = []
# amount = int(input("How many items: "))
# for x in range(1, amount + 1):
#     lst.append(int(input(f"Item {x}: ")))  
# print(lst)

# lst = []
# while True:
#     print(f"The list is now {lst}")
#     choice = str(input("a(d)d, (r)emove or e(x)it: "))
#     if len(lst) > 0 and choice == 'd':
#         lst.append(lst[-1] + 1)
#     elif len(lst) <= 0 and choice == 'd':
#         lst.append(1)
#     elif len(lst) > 0 and choice == 'r':
#         lst.pop(-1)
#     elif len(lst) <= 0 and choice == 'r':
#         continue
#     if choice == 'x':
#         print('Bye!')
#         break


# word_lst = []
# while True:
#     word = str(input("Word: "))
#     if word in word_lst:
#         print(f"You typed in {len(word_lst)} different words")
#         break
#     else:
#         word_lst.append(word)


# lst = []

# while True:
#     num = int(input("New item: "))
#     if num == 0:
#         print("Bye!")
#         break
#     else:
#         lst.append(num)
#         print(lst)
#         print(sorted(lst))


# def length(lst):
#     return len(lst)

# result = length([1, 1, 1, 1])
# print("The length is", result)    

# def mean(int_lst):
#     return sum(int_lst) / len(int_lst)  

# my_list = [1, 2, 3, 4, 5]
# result = mean(my_list)
# print("mean value is", result)

def range_of_list(int_lst):
    return abs(max(int_lst) - min(int_lst))

my_list = [1, 2, 3, 4, 5]
result = range_of_list(my_list)
print("The range of the list is", result)