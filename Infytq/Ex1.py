#DSA-Exer-1

def update_mark_list(mark_list, new_element, pos):
    mark_list.insert(pos, new_element)
    return mark_list

def find_mark(mark_list,pos1,pos2):
    result_list = []
    result_list.append(mark_list[pos1])
    result_list.append(mark_list[pos2])
    return result_list

mark_list=[89, 78, 99, 76, 77, 67, 99, 98, 90]
new_element=78
pos=8
pos1=5
pos2=7
print(update_mark_list(mark_list, new_element, pos))
print(find_mark(mark_list, pos1, pos2))