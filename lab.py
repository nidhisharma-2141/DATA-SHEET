                   #LAB

#ASSIGNMENT
'''ScriptsDeclare a div() function with two parameters. Then call the function and pass two
numbers and display their division.'''
def div (a,b):
    return a/b
result=div(40,2)
print(result)

'''2.Declare a square() function with one parameter.Then call the function and pass
one number and display the square of that number'''
def div (a):
    return a*a
result=div(40)
print(result)


'''3.Using max() and min() functions display the maximum and minimum of 5 random
numbers.
'''
a=[10,20,30,40]
print(max(a))
print(min(a))

''' 4.Accept a name from the user and display that in lower case using lower()
function
'''
str=input("enter your name:")
str1=str.lower()
str2=str.upper()
print('in lower case:',str1)
print('in upper case:',str2)

#ASSIGNMENT

'''1. Write a Python program to count the occurrences of each word in a
given sentence
string = “To change the overall look of your document. To change the look
available in the gallery”
'''

'''2. Write a Python program to remove a newline in Python
String = "\nBest \nDeeptech \nPython \nTraining\n"'''
txt = "\nBest \nDeeptech \nPython \nTraining\n"
x = txt.replace("\n", " ")
print(x)

'''3. Write a Python program to reverse words in a string
String = “Deeptech Python Training”'''
def reverse(x):
  return x[::-1]
txt = reverse("Deeptech Python Training")
print(txt)

''' 4.Write a Python program to count and display the vowels of a given
text
String=”Welcome to python Training”
'''
def Check_Vow(string, vowels):
	final = [each for each in string if each in vowels]
	print(len(final))
	print(final)
string = "Welcome to python Training"
vowels = "AaEeIiOoUu"
Check_Vow(string, vowels);


#ASSIGNMENT

''' 1. Write a Python program to Count all letters, digits, and special
 symbols from the given string
 Input = “P@#yn26at^&i5ve”
 Output: Chars = 8 Digits = 2 Symbol = 3'''
a=str(input("enter the string:-"))
def find_digits_chars_symbols(a):
    letters = 0
    digits = 0
    symbols = 0
    for i in a:
        if "A"<=i <= "z" :
            letters += 1

        elif "0"<=i <= "9":
            digits +=1

        else:
            symbol += 1
            
    print("Letters=",letters)
    print("Digits=",digits)
    print("Symbols=",symbols)
find_digits_chars_symbols(a);
    

    
''' 4. Write a Python Count vowels in a string
 input= “Welcome to Python Assignment”
 Output: Total vowels are: 8'''
def Check_Vow(string, vowels):
	final = [each for each in string if each in vowels]
	print("Total vowels are:",(final))
string = "Welcome to Python Assignment"
vowels = "AaEeIiOoUu"
Check_Vow(string, vowels);

''' Write a Python program to count Uppercase, Lowercase, special
 character and numeric values in a given string
Input = “Hell0 W0rld ! 123 * # welcome to pYtHoN”
 Output:
 UpperCase : 5
 LowerCase : 18
 NumberCase : 5
 SpecialCase : 11'''

''' Write a Python program to remove duplicate characters of a given
 string.
 Input = “String and String Function”
 Output: String and Function'''

