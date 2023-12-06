import check_input
import small_plate
import large_plate
from turkey import Turkey
from stuffing import Stuffing
from potatoes import Potatoes
from beans import Beans
from pies import Pies

myPlate = small_plate.SmallPlate()

myPlate = Turkey(myPlate)
myPlate = Stuffing(myPlate)

#mydes = myPlate.description()

print(myPlate.description()[:-4])

# #Sturdiness | Weight
#         if myPlate.weight() >= 13:
#             Sturdiness = "Strong"
#         elif 7 <= myPlate.weight() <= 12:
#             Sturdiness = "Weak"
#         elif 1 <= myPlate.weight() <= 6:
#             Sturdiness = "Bending"
#         elif myPlate.weight() <= 0:
#             break
#
#
#         #Space | Area
#         if myPlate.area() >= 41:
#             Space = "Plenty"
#         elif 21 <= myPlate.area() <= 40:
#             Space = "Some"
#         elif 1 <= myPlate.area() <= 20:
#             Space = "Tiny bit"
#         elif myPlate.area() <= 0:
#             break