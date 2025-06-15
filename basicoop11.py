#
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
    def _getIncome(self):
        return self.__salary * 12  # Assuming salary is monthly, return annual income
    
    def __str__(self):
        # Override the __str__ method to provide a string representation of the object
        return f"Employee(Name: {self.__name}, Department: {self._department}, Salary: {self.__salary},Salary Per Year: {self._getIncome()})"

class Accounting(Employee):
    __department = "Accounting"  # Private class variable
    def __init__(self,name,salary):
        super().__init__(name,self.__department, salary)
        # super()._showData()  # Call the private method from the superclass

class IT(Employee):
    __department = "IT"  # Private class variable
    def __init__(self,name,salary):
        super().__init__(name,self.__department, salary)
        # super()._showData()  # Call the private method from the superclass

class HR(Employee):
    __department = "HR"  # Private class variable
    def __init__(self,name,salary):
        super().__init__(name,self.__department, salary)
        # super()._showData()  # Call the private method from the superclass

#การสร้างออบเจ็กต์
objAc = Accounting("Wanchana Saelue", 50000) 
print(objAc.__str__())  # Call the __str__ method to print object details
objIt = IT("Naphat Saelue", 60000)       
print(objIt.__str__())  # Call the __str__ method to print object details
objHr = HR("Nattapong Saelue", 70000)
print(objHr.__str__())  # Call the __str__ method to print object details



#Print Public
# obj1._showData()
# obj2._showData()
# obj3._showData()

# Print class variables
# print(Accounting._Employee__minsalary)
# print(IT._companyName)
# print(HR._companyName)

