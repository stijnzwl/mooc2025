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