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
        