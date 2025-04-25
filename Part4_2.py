def line(integer, string):
    new_string = ''
    while len(new_string) < integer:
        if len(string) > 0:
            new_string += string[0]
        else:
            new_string += '*'
    print(new_string)
    

line(7, "%")
line(10, "LOL")
line(3, "")


def box_of_hashes(length):
    while length > 0:
        line(10, "#")
        length -= 1
        
box_of_hashes(5)


def square_of_hashes(length):
    save_it = length
    while length > 0:
        line(save_it, '#')
        length -= 1
        
square_of_hashes(4)


def square(length, character):
    save_it = length
    while length > 0:
        line(save_it, character)
        length -= 1
        
square(3, '#')


def triangle(height):
    start = 1
    while height > 0:
        line(start, "#")
        height -= 1
        start += 1
        
triangle(3)


def shape(width, char1, height, char2):
    start = 1
    save_it = width
    while width > 0:
        line(start, char1)
        width -= 1
        start += 1
        
    while height > 0:
        line(save_it, char2)
        height -= 1
        
shape(5, "X", 3, "*")    
shape(2, "o", 4, "+")
shape(3, ".", 0, ",")


def spruce(n):
    print('a spruce!')
    for i in range(1, n + 1):
        spaces = (n - i) * " "
        stars = ((i * 2) - 1) * "*"
        print(spaces + stars)
    print((n - 1) * " " + "*")
    
spruce(3)
spruce(7)


def greatest_number(n, y, x): 
    return max(n, y, x)
        
print(greatest_number(3, 4, 1)) # 4
print(greatest_number(99, -4, 7)) # 99
print(greatest_number(0, 0, 0)) # 0


def same_chars(string, int1, int2):
    if int1 < len(string) and int2 < len(string):
        if string[int1] == string[int2]:
            return True
        else:
            return False
    else:
        return False

# same characters m and m
print(same_chars("programmer", 6, 7)) # True

# different characters p and r
print(same_chars("programmer", 0, 4)) # False

# the second index is not within the string
print(same_chars("programmer", 0, 12)) # False


def first_word(string):
    lst = string.split()
    return lst[0]

def second_word(string):
    lst = string.split()
    return lst[1]

def last_word(string):
    lst = string.split()
    return lst[-1]

sentence = "it was a dark and stormy python"
print(first_word(sentence)) # it
print(second_word(sentence)) # was
print(last_word(sentence)) # python


