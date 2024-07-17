#creation of dictionary and insertion of element 
dictionary = {}
dictionary['NAME'] = 'nidhi'
dictionary['address'] = 'ghaziabad'
dictionary['branch'] = 'csds'
print(dictionary)

#pop()= for remove element in dictionary
dictionary.pop('branch')
print(dictionary)


#key()=  display list of all key of dictionary
elementkeys=dictionary.keys()
print(elementkeys)


#values()= display list of values of all the element of dictionary
elementvalues=dictionary.values()
print(elementvalues)

'''items()=return a list of items(each element in the form of
tuple with two memeber key and value)'''
elements=dictionary.items()
print(elements)

#clear()=remove all element of dictionary
dictionary.clear()
print(dictionary)

#copy

#fromkeys

#get

#update()=to update or insert multiple element (key:value pair)in dictionary
dict1={1:'mon',2:'tue',3:'wed'}
dict2={4:'thu'}
dict1.update(dict2)
print(dict1) 

# len()= count the no. of element in dictionary


print("----------------------------------------------------------------------------")

#student data display by dictionay
student={'stdid':['std101','std102','std103','std104','std105','std106','std107','std108','std109','std110'],
         'stdname':['ashish','abhishek','aman','rahul','ruby','suman','saurab','sumit','kamlesh','rohan'],
         'age':[15,14,15,14,13,13,15,14,15,15],
         'hindi':[67,23,45,89,90,45,23,45,34],
         'english':[89,45,56,67,67,46,23,45,56,12],
         'maths':[87,48,78,45,89,67,34,67,78,24],
         'science':[89,90,78,45,93,67,45,78,99,45],
         'computer':[90,45,67,56,65,67,34,90,67,56],
         'total':[422,313,302,258,403,337,181,303,345,171]}
print("Students with English score greater than 50:")
for i in range(len(student['stdid'])):
    if student['english'][i] > 50:
        print("Student Name:", student['stdname'][i])
print("----------------------------------------------------------------------------")

maths_scores = list(zip(student['stdid'], student['stdname'], student['maths']))
maths_scores.sort(key=lambda x: x[2], reverse=True)
print("Top 5 students in Maths:")
for i in range(5):
    print("Student Name:", maths_scores[i][1])
'''from tabulate import tabulate

student={'stdid':['std101','std102','std103','std104','std105','std106','std107','std108','std109','std110'],
         'stdname':['ashish','abhishek','aman','rahul','ruby','suman','saurab','sumit','kamlesh','rohan'],
         'age':[15,14,15,14,13,13,15,14,15,15],
         'hindi':[67,23,45,89,90,45,23,45,34],
         'english':[89,45,56,67,67,46,23,45,56,12],
         'maths':[87,48,78,45,89,67,34,67,78,24],
         'science':[89,90,78,45,93,67,45,78,99,45],
         'computer':[90,45,67,56,65,67,34,90,67,56],
         'total':[422,313,302,258,403,337,181,303,345,171]}

headers = ['stdid', 'stdname', 'age', 'hindi', 'english', 'maths', 'science', 'computer', 'total']
data = list(zip(student['stdid'], student['stdname'], student['age'], student['hindi'], student['english'], student['maths'], student['science'], student['computer'], student['total']))

print(tabulate(data, headers, tablefmt="grid"))'''
#
