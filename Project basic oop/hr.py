from employee import Employee

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