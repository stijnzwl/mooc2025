def formatted(float_list):
    new_lst = []
    
    for i in float_list:
        new_lst.append(str(f"{i:.2f}"))
        
    return new_lst
    
    
my_list = [1.234, 0.3333, 0.11111, 3.446]
new_list = formatted(my_list)
print(new_list)