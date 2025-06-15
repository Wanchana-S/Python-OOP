#การสร้างคลาส
class Employee: 

    #การสร้างเมธอด
    def detail(self,name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary        

    def showData(self):
        #การแสดงผลข้อมูล
        print(f"Name: {self.name}, Age: {self.age}, Position: {self.position}, Salary: {self.salary}")
    
#การสร้างออบเจ็กต์
obj1 = Employee()
obj1.detail("Wanchana Saelue", 29, "Software Engineer", 60000)  

obj2 = Employee()
obj2.detail("John Doe", 30, "Data Scientist", 70000) 

obj3 = Employee()
obj3.detail("Jane Smith", 28, "Web Developer", 65000) 

obj1.showData()
obj2.showData()     
obj3.showData()
# Output:

