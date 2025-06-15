from employee import Employee

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