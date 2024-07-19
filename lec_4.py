''''DATA TYPES
    1.LIST 2.TUPLE 3. DICTIONARY 4.SET 5.STRING

LIST:collection of any type of data,mutable,follow insertion order,duplication is allowed

CREATION OF LIST:
 1. BLANK LIST=
       LISTNAME=[]
 2. WITH SOME ELEMENT
       LISTNAME=[10,20,"NIDHI"]
 3. WITH ANOTHER SEQUENCE DATATYPE
       LISTNAME=list(seq datatype)'''



# print the list in reverse order using forward indexing
a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17 ,18,19 ,20]
b = len(a)-1
# using for loop
print("----printing the list in reverse order using forward indexing----")
for i in a:
    print(a[b],end=",")
    b -= 1
# using slicing
print("\n----printing the list in reverse order using slicing----")
print("\n",*a[19:0:-1],a[0])
print("\n----printing the list in reverse order using negative indexing----")
print("\n",*a[-1:-21:-1])     

# insertion in list
# at the end of the list
# --- using append()  -- insert 1 element at the end of the list
# --- extend() ---- insert more than 1 element at the end of list at the same time
# --- listname.extend()
# insert at specified position --- we have insert() function
# --- listname.insert(index,element)
print("\n----insertion----")
d = [76,45 ,78]
print("---using extend()---")
a.extend(d)
print(a)
print("---using insert()---")
a.insert(3,789)
print(a)




# collection datatypes
# list creation , insertion , slicing , indexing , 

# what is the method for inserting multiple elements at a time in a list
print(" method for inserting multiple elements at a time in a list")
print("before inserting -----   d = ",d)
g = [2,3,4,5,4,5,4]
pos = 2
d[pos:pos] = g
print("\nafter inserting----   d = ",d)
print(*d)
print("----remove operation-----")
# remove element from the list
# pop(element) --- delete element from the list from the specified position ---- if position is not specified last element will be deleted
# remove(element to be delete)   ---  to delete the elemnet from the specified position for ex : if there are two duplicates in the list it will delete the element of first occurenvce
# remove() generate exception if the element is not present
# clear() ----- it will delete all elements of the list but does not delete the lists
print("g = ",g)
g.pop(3)
print("after pop operation g = ",g)
g.remove(4)
print("after remove operation g = ",g)
g.clear()
print("after clear operation g = ",g)
