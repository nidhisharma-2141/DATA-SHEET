'''#SET
set is mutable datatype,does not contain duplicate value,{},unordered
 #CREATION OF SET
s={20,30,40}
print(s)
s=set([10,20,30])
print(s)


#insertion in set

#ADD()-adding one element only
set1={20,30,40}
set1.add(50)
print(set1)

#UPDATE()-adding more than one element

set2={20,30,40}
set2.update(50,60,70)
print(set2)

#discard()=remove element if its not present than no error will be occur

set3={20,30,40}
set3.discard(50)
print(set3)

#remove()= remove element form the set if it is not present than error will be occur

set4={20,30,40}
set4.remove(50)
print(set4)'''

#STRING
name="i am java trainer"
print(name)
print('name[2:4]',name[2:4])
print('name[5:9]',name[5:9])
print('name[:15]',name[:15])
print('name[2:]',name[2:])
print('name[:]',name[:])
print('name[0:17:3]',name[0:17:3])
print('name[::]',name[::])
print('name[::-1]',name[::-1])


'''#memdership oprater
#IS OR IS NOT
X=['A','B']
Y=['C','D']
Z=X
print(x is y)
print(x is z)'''

''' #CAPIALAIZE
str="nidhi sharma"
print(str)
str=str.capitalize()
print(str)


#CENTER()= method allign the string to the center by filling padding left and right of the string.this method take two arguments ,first width and second fillchar
str="nidhi sharma"
print(str)
str=str.center(16,"$")
print(str)

#COUNT()= COUNT THE OCCRANCE OF ELEMENT,it takes three paraments ,first is substring ,second is start index,third is last index ,start and last both are optional
STR="MY NAME IS NIDHI"
A=STR.count("I")
print(A)
#endswith()= check string is ending with same element or not if it is correct than result will be true otherwise false
STR="MY NAME IS NIDHI"
A=STR.endswith("I")
print(A)

#startswith()= check string is starting with same element or not if it is correct than result will be true otherwise false
STR="MY NAME IS NIDHI"
A=STR.startswith("I")
print(A)

#FIND()=find substring in the whole string and return index of the first match .it retuen -1 if substring does not match
str="my name is nidhi"
str1=str.find("i")
print(str1)

#index()=find substring in the whole string and return index of the first match .it retuen error if substring does not match
str="my name is nidhi"
str1=str.index("z")
print(str1)

#isalnum()= its checks is alphanumeric or not

str="my name is nidhi"
str1=str.("z")
print(str1)'''

#isalpha()=
#isnum()=
#islower()=check the string in upper case or not
#isupper()=check the string in lower case or not
#lower()=convert the string into lower case
#upper()=convert the string into upper case
#lstrip()=remove space from left hand side
#rstrip()=remove space from the right hand side
#strip()=remove space from both hand side
str="....nidhi...."
str1=str.lstrip(".")
str2=str.rstrip(".")
str3=str.strip(".")
print(str1)
print(str2)
print(str3)
print(str)

#replace()=return a copy of the string all occrance of substring old replace by new , if the count argument is given then first count occurnce will be replace

str="my name is nidhi"

#swapcase=convert the string into upper case to lower case and vice-versa
#title()= each word of string,first letter capital




