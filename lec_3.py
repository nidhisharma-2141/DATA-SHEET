#ITERATION
#to repeat statement or group of statement unitil the condition becomes false
#component=1.initialization,2.condition,3.update
#FOR= use where the fix sequence and number of itration is known



a = [80 ,90 ,30 , 20 , 70 , 80 , 39 , 87]
sum = 0
for i in a:
    sum = sum+i
print(sum)
# range function
b = range(1,7,2)
# 1 --- start  value(included)
# 7 --- end value(not inculded)
# 2 --- step--updation
for j in b:
    print(j)
c = range(10)
# starts with 0 if starting point is not specified
# step will be 1 by default step will always 1 if not specified in range
for k in c:
    print(k)
d = range(20 , -50 , -4)
for h in d:
    print(h)

print("---------------------------------------------------")
g = range(10,501)
for s in g:
    if(s%10 == 0 and s%7 == 0):
        print(s)

print("---------------------------------------------------")
q = range(100 , 1000)
count = 0
for i in q:
    if(i%2 == 0 and i%3==0):
        count += 1
        print(i,end=",")


print("\ntotal numbers : ",count)




print("------------------------------------------------------")
# while 
# it is used when we are not sure of number of iterations

# -----------display total number between 100 to 1000 which is even and divisible by 3

print("-----------display total number between 100 to 1000 which is even and divisible by 3----------------")
a = 100
count = 0
while(a < 1000):
    if(a%2 == 0 and a%3==0):
        print(a ,end = ",")
        count +=1
        a += 1
    else:
        a +=1
print("\ntotal count : ",count)

