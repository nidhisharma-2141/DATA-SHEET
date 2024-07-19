Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#student table



# students = [
#     {'stdid':'std101','stdname':'ashish kumar','standard':'10th','age':15,'hindi':67,'english':89,'maths':87,'science':89,'computer':90,'total':422},
#     {'stdid':'std102','stdname':'abhishek kumar','standard':'10th','age':15,'hindi':67,'english':89,'maths':87,'science':89,'computer':90,'total':422}
#     ]
import pandas as pd

students = [
    {'stdid': 'std101', 'stdname': 'Ashish Kumar', 'standard': '10th', 'age': 15, 'hindi': 67, 'english': 89, 'maths': 87, 'science': 89, 'computer': 90, 'total': 422},
    {'stdid': 'std102', 'stdname': 'Abhishek Kumar', 'standard': '10th', 'age': 15, 'hindi': 67, 'english': 89, 'maths': 87, 'science': 89, 'computer': 90, 'total': 422},
    {'stdid': 'std103', 'stdname': 'Aman', 'standard': '10th', 'age': 15, 'hindi': 45, 'english': 56, 'maths': 78, 'science': 78, 'computer': 45, 'total': 302},
    {'stdid': 'std104', 'stdname': 'Rahul', 'standard': '10th', 'age': 14, 'hindi': 67, 'english': 49, 'maths': 56, 'science': 45, 'computer': 78, 'total': 295},
    {'stdid': 'std105', 'stdname': 'Ruby', 'standard': '10th', 'age': 13, 'hindi': 89, 'english': 67, 'maths': 45, 'science': 45, 'computer': 56, 'total': 258},
    {'stdid': 'std106', 'stdname': 'Suman', 'standard': '10th', 'age': 15, 'hindi': 90, 'english': 90, 'maths': 56, 'science': 78, 'computer': 89, 'total': 403},
    {'stdid': 'std107', 'stdname': 'Saurabh', 'standard': '10th', 'age': 15, 'hindi': 45, 'english': 45, 'maths': 23, 'science': 67, 'computer': 67, 'total': 247},
    {'stdid': 'std108', 'stdname': 'Sumit', 'standard': '10th', 'age': 14, 'hindi': 23, 'english': 56, 'maths': 78, 'science': 78, 'computer': 78, 'total': 313},
    {'stdid': 'std109', 'stdname': 'Kamlesh', 'standard': '10th', 'age': 15, 'hindi': 67, 'english': 78, 'maths': 67, 'science': 78, 'computer': 78, 'total': 368},
    {'stdid': 'std110', 'stdname': 'Rohan', 'standard': '10th', 'age': 15, 'hindi': 12, 'english': 24, 'maths': 45, 'science': 56, 'computer': 56, 'total': 171}
]

df = pd.DataFrame(students)
# display the students whose marks are above 50 in english
print("--------display the students whose marks are above 50 in english----------")
for i in students:
    if(i['english']>50):
        print(i['stdname'])

# display top 4 scrores in maths
print("------------top 4 scrores in maths-------------- ")
new_data = df.sort_values(by='maths',ascending=False)
print(new_data.head(4))

print("------last 3 entries-----------")
# last three entries
print(df.tail(3))
print(df)
