#Overloading and Overriding in Python
class Employee:
    __minsalary = 20000  # Protected class variable
    __maxsalary = 200000  # Private class variable
    _companyName = "Tech Solutions"  # Public class variable
    def __init__(self, name, department, salary):
        #Private attributes
        self.__name = name
        self._department = department
        self.__salary = salary   
        
    #Private method
    def _showData(self):
        #การแสดงผลข้อมูล
        print(f"Name: {self.__name}, Position: {self._department}, Salary: {self.__salary}")
    
    #การคำนวณรายได้ต่อปี
    def _getIncome(self,bonus=0,ot=0):
        return self.__salary * 12  + bonus + ot
    
    def __str__(self):
        # Override the __str__ method to provide a string representation of the object
        return f"Employee(Name: {self.__name}, Department: {self._department}, Salary: {self.__salary})"

class Accounting(Employee):
    __department = "Accounting"  # Private class variable
    def __init__(self,name,salary,age):
        super().__init__(name,self.__department, salary)
        self.__age = age  # Set the private age attribute

    def _showData(self):
        #การแสดงผลข้อมูล
        super()._showData()
        print(f"Age: {self.__age}")
        print("==================================")

    def __str__(self):
        # Override the __str__ method to provide a string representation of the object
        return f"Accounting(Name: {self._Employee__name}, Department: {self._department}, Salary: {self._Employee__salary}, Age: {self.__age})"

class IT(Employee):
    __department = "IT"  # Private class variable
    __skill = ["Python", "Java", "C++"]  # Example skill set
    def __init__(self,name,salary,experience,skill):
        super().__init__(name,self.__department, salary)
        self.__experience = experience
        self.__skill = skill    

    def _showData(self):
        #การแสดงผลข้อมูล
        super()._showData()
        print(f"Experience: {self.__experience} years, Skills: {', '.join(self.__skill)}")
        print("==================================")

    def __str__(self):
        # Override the __str__ method to provide a string representation of the object
        return f"IT(Name: {self._Employee__name}, Department: {self._department}, Salary: {self._Employee__salary}, Experience: {self.__experience} years, Skills: {', '.join(self.__skill)})"
        
class HR(Employee):
    __department = "HR"  # Private class variable
    def __init__(self,name,salary,area):
        super().__init__(name,self.__department, salary)
        self.__area = area

    def _showData(self):
        #การแสดงผลข้อมูล
        super()._showData()
        print(f"Area: {self.__area}")

    def __str__(self):
        # Override the __str__ method to provide a string representation of the object
        return f"HR(Name: {self._Employee__name}, Department: {self._department}, Salary: {self._Employee__salary}, Area: {self.__area})"
        

#การสร้างออบเจ็กต์
objAc = Accounting("Wanchana Saelue", 50000, 30) 
# objAc._showData()  # Call the private method from the subclass
print(objAc.__str__())  # Call the overridden __str__ method
objIt = IT("Naphat Saelue", 60000, 5, ["Python", "Java"])       
print(objIt.__str__())  # Call the overridden __str__ method
objHr = HR("Nattapong Saelue", 70000, "Bangkok")
print(objHr.__str__())  # Call the overridden __str__ method



