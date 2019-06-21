import sys
# This function provides the capacity, size and space left in the list. It can be invoked to get details about the list
def list_details(lst):
    #Number of elements that can be stored in the list
    print("Capacity: ", (sys.getsizeof(lst) - 64)//8)
    #Number of elements in the list
    print("Size: ", len(lst))
    #Number of elements that can be stored in space left
    print("Space left: ", ((sys.getsizeof(lst) - 64) - len(lst*8))//8)

    #(size - 36)/4 for 32 bit machines and
    #(size - 64)/8 for 64 bit machines
    #36, 64 - size of an empty list based on machine
    #4, 8 - size of a single element in the list based on machine

marias_list = []
print("Empty list created:")
print("List details: ")
list_details(marias_list)

marias_list.append("Sugar")
print("Maria's list after adding sugar:")
print(marias_list)
print("List details: ")
list_details(marias_list)

marias_list.append("Tea Bags")
marias_list.append("Milk")
marias_list.append("Biscuit")
print(marias_list)
print("List details:")
list_details(marias_list)

marias_list.insert(1,"Salt")
print(marias_list)
print("List details:")
list_details(marias_list)

marias_list.pop(1)
print(marias_list)
print("List details: ")
list_details(marias_list)