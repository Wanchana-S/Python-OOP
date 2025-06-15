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