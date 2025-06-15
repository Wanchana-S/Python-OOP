from accounting import Accounting
from it import IT
from hr import HR

#การสร้างออบเจ็กต์
objAc = Accounting("Wanchana Saelue", 50000, 30) 
# objAc._showData()  # Call the private method from the subclass
print(objAc.__str__())  # Call the overridden __str__ method
objIt = IT("Naphat Saelue", 60000, 5, ["Python", "Java"])       
print(objIt.__str__())  # Call the overridden __str__ method
objHr = HR("Nattapong Saelue", 70000, "Bangkok")
print(objHr.__str__())  # Call the overridden __str__ method