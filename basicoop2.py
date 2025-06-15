#การสร้างคลาส
class Employee: 

    #การสร้างเมธอด
    def detail(self,name,age,position,salary):
        #การกำหนดค่าเริ่มต้น
        self.name = "Wanchana Saelue"
        self.age = 29  
        self.position = "Software Engineer"
        self.salary = 60000        
        #การแสดงผลข้อมูล
        print(f"Name: {self.name}, Age: {self.age}, Position: {self.position}, Salary: {self.salary}")
    
#การสร้างออบเจ็กต์
obj1 = Employee()
obj1.detail("Wanchana Saelue", 29, "Software Engineer", 60000)  

