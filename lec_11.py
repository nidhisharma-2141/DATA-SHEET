#OOPS

#OBJECT AND CLASSES:in oops ,object are instance of classes.
 #BASIC CONCEPT OF CLASS AND OBJECT

class student:
    name=" "
    age=0
    def study (self):
        print("study 3 hour")

obj=student()
obj.study()

#self = provide access of current class members
class student:
    name="xyz"
    age=0
    def study (self):
        print("study 3 hour",self.name)

obj=student()
obj.study()


class student:
    name="xyz"
    age=0
    def study (self):
        print("study 3 hour",self.name)
        self.sleep()
    def sleep (self):
        print("study 1 hour")

obj=student()
obj.study()

class student:
    name="xyz"
    age=0
    def study (self):
        print("study 3 hour",self.name)
        
    def sleep (self):
        print("study 1 hour")
        study()

obj=student()
obj.study()


#INHERITANCE:
#heirarichal
class a:
    def show(self):
        print("hello")
class b(a):
    pass
class c(a):
    pass

#multi level
class a:
    def show(self):
        print("hello")
class b(a):
    pass
class c(b):
    pass


#hybrid:
class a:
    def show(self):
        print("this is show method")
class b(a):
    def demo(self):
        print("demo method")
class c(a):
    pass
class d(b,c):
    pass
#POLYMORPHISM
def setdata(id,name):
    print("id,name")
def setdata(id,name,age):
    print("id,name,age")
setdata(101,"nidhi",1)

#default value

def sum(a,b,c=0):
    print(a+b+c)
sum(10,20,30)
sum(10,20)

#method overriding:
'''polymorphism let us define methid in the child class that hve the same as the method
int the parent class. inheritance ,the child class inherit the method from the parent
class however,it is possible to modify a method inherited from the parent class. this
is particular usefil in case where the method inherit from parent classs dpesn't quite
fit the child'''



'''class bird:
    def intro(self):
        print("there are many types of birds")
    def flight(self):
        print("most of the bird can fly but some cannot")
class sparrow(bird):
    def fight(self):
        print("i can fly")
class ostrich(bird):
    def flight(self):
        print("i can't fly")
s=ostrich()
a=sparrow()
a.flight()
s.flight()
#_=protected,__=private
class a:
    __name="self"
class b(a):
    def show(self):
        print("this is show method",self.name)
obj=b()
obj.show()'''

#EXCEPTION HANDLING:
#TRY -EXCEPT
print("line 1")
print("line 2")
print("line 3")
print("line 4")
num1=int(input("enter 1 no."))
num2=int(input("enter 2 no."))
try:
    print(num1/num2)
except:
    print("something wents wrong")
else:
    print("else block")#execute when no exception occur
finally:
    print("finally block")
print("line 6")

#wap a py
