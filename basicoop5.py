#ฟังก์ชั่นเสริม
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
    
#การสร้างออบเจ็กต์
obj1 = Employee("Wanchana Saelue", 29, "Software Engineer", 60000)
obj2 = Employee("John Doe", 30, "Data Scientist", 70000)
obj3 = Employee("Jane Smith", 28, "Web Developer", 65000)

print(isinstance(obj1, Employee))  # True
print(dir(obj1))  # Lists all attributes and methods of the object
print(obj1.__class__)   # <class '__main__.Employee'>