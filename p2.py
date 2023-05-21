def factorial(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return n*factorial(n-1)


print("Hello Ali")

for i in range(1, 5):
    print("Your Friendly Neighborhood Spiderman:)")


class Student:
    def __init__(self, Id, name, family):
        self.Id = Id
        self.name = name
        self.family = family

    def ShowInfo(self):
        print(f"Id:{self.Id},name:{self.name},family:{self.family}")

s1=Student(100,"Ali","Kazempour")
s1.ShowInfo()        
