''''condition statement:
1.if =If the simple code of block is to be performed if the condition
      holds true then the if statement is used. Here the condition mentioned holds
      then the code of the block runs otherwise not.'''
a = int(input("enter the first no."))
b = int(input("enter the second no."))
if(a==b):
    print("both are equal")



'''2.if-else =execute a block of code when the condition in the if statement is true,
        gand another block of code when the condition is false.'''
# if(a>b):
#     print(a)
# else:
#     print(b)
# find greatest between  2 numbers
a = int(input("enter the first no."))
b = int(input("enter the second no."))
if(a==b):
    print("both are equal")
print(a if(a>b)else b)


'''3.elif= If the first if statement evaluates to false, then elif statements
        are evaluated one by one and comes out of the  if any one is satisfied.
        Last the else block which will  when all
        preceding if/elif conditions fails.'''
#find profit and loss
sp = float(input("enter the selling price"))
cp = float(input("enter the cost price"))
if(sp < 0):
    print("invalid")
elif(cp < 0):
    print("invalid")
if(sp > cp):
    print("profit of : ",sp-cp)
else:
    print("loss of :" , cp-sp)

# time conversion of seconds into hours , minutes , seconds
# logic
# for ex : 7340
# 7340/3600 ---- as the output it will give hours 
# rem = 7340%3600 ---- it will give remainder in seconds now we will convert those seconds into min,sec
# rem/60 --- minutes
# rem%60 --- seconds
secs = int(input("enter the time in seconds"))
# 7340
if(secs < 0):
    print("invalid input")
else:
    if(secs < 60):
        print("00:00:",secs)
    elif(secs < 3600):
        mins = (secs%3600)/60
        # secs_2 is to store the remainder of secs and then we wil divide the remainder by 60 
        secs_2 = (secs%3600)
        secs_3 = secs_2%60
        print("00hr:",int(mins),"min:",secs_3,"sec")
    else:
        hours = secs/3600
        mins = (secs%3600)/60
        # secs_2 is to store the remainder of secs and then we wil divide the remainder by 60 
        secs_2 = (secs%3600)
        secs_3 = secs_2%60
        print(int(hours),":",int(mins),":",secs_3)



# print(int(hours))
# mins = (secs%3600)/60
# print(int(mins))
# secs_2 = (secs%3600)
# secs_3 = secs_2%60
# print(secs_3)
