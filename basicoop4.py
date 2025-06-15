#การสร้าง Constructor & Destructors ใน Python
# การสร้างคลาส
class Employee: 

    #การสร้างเมธอด
    def __init__(self, name, age, position, salary):
        #การกำหนดค่าเริ่มต้น
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary   

    def showData(self):
        #การแสดงผลข้อมูล
        print(f"Name: {self.name}, Age: {self.age}, Position: {self.position}, Salary: {self.salary}")

    def __del__(self):
        #การทำลายออบเจ็กต์
        print(f"Object {self.name} is being deleted")
    
#การสร้างออบเจ็กต์
obj1 = Employee("Wanchana Saelue", 29, "Software Engineer", 60000)
obj1.salary = 50000
obj1.showData()  

obj2 = Employee("John Doe", 30, "Data Scientist", 70000)
obj1.salary = 40000
obj2.showData() 

obj3 = Employee("Jane Smith", 28, "Web Developer", 65000)
obj1.salary = 55000
obj3.showData() 


