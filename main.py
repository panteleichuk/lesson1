# #Клас студента школи Логіка
# # данні студента - ім'я, прізвище, логіки, група, логін та пароль,вік, телеграм
# # діїї студента - вивод інформації - уся, логін та пароль загальна кількість логіків, телеграм 
                
class Student:
    def __init__(self,name,surname,age,logiks,
                group,login,password,telegram):
        self.name = name
        self.surname = surname
        self.age = age
        self.logiks = logiks
        self.group = group
        self.login = login
        self.password = password
        self.telegram = telegram

    def all_info(self):
        print("==========All information of student==============")
        print("Name -",self.name)
        print("Surname - ", self.surname)
        print("Age -",self.age )
        print("Logiks -",self.logiks)
        print("Group -",self.group )
        print("Login -",self.login)
        print("Password -", self.password )
        print("Telegram -",self.telegram )
        print("===================================================")
    def logik_info(self):
        print("==========Logiks of student==============")
        lg = ""
        for logik in self.logiks:
            lg += str(logik)+", "
        all_lg = sum(self.logiks)
        print(lg)
        print("All logiks:", all_lg)
        print("===================================================")
    

students = list()
student = Student("Maria","Panteleicjuk",18,
                  [7,8,7,8,7,8],"Python","pantel",
                  "123","@mpantel")    
students.append(student)
print("======All students=======")
for i in range(len(students)):
    print(i,"-",students[i].surname)

while True:
    print("What do you want? 1- all info, 2- logik,3-exit")
    do = int(input(""))
    who = int(input("Enter number of student"))
    if do==1:
        students[who].all_info()
        

        

