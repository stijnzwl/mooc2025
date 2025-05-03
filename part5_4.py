def create_tuple(x: int, y: int, z: int):
    return (min(x, y, z), max(x, y, z), x + y + z)
  
if __name__ == "__main__":
    print(create_tuple(5, 3, -1))  
    
    
def oldest_person(people: int):
    year = []
    for i in people:
        year.append(i[1])
        
    for i in people:
        if i[1] == min(year):
            return i[0]
        
        
p1 = ("Adam", 1977)
p2 = ("Ellen", 1985)
p3 = ("Mary", 1953)
p4 = ("Ernest", 1997)
people = [p1, p2, p3, p4]

print(oldest_person(people))


def older_people(people: list, year: int):
    new_list = []
    for i in people:
        if i[1] < year:
            new_list.append(i[0])
    return new_list

p1 = ("Adam", 1977)
p2 = ("Ellen", 1985)
p3 = ("Mary", 1953)
p4 = ("Ernest", 1997)
people = [p1, p2, p3, p4]

older = older_people(people, 1979)
print(older)