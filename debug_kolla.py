
'''from data_layer.Airplane_Data import Airplane_Data
from Model.airplane import Airplane

data_class = Airplane_Data()
c = Airplane

c.plane_insignia = input("plane_insignia")
c.plane_type_id = input("plane_type_id")
c.capacity = input("capacity")

result = data_class.create_airplane(c)
'''

from logic_layer.voyage_logic import Voyage_Logic
from logic_layer.employee_logic import Employee_Logic
from data_layer.data_wrapper import Data_Wrapper
from Model.employee import Employee
from Model.desinations import Desinations
from data_layer.Destinations_Data import Destinations_Data
from logic_layer.destinations_logic import Destinations_Logic


#nid,name,role,rank,licence,address,phone_nr,email,homephone_nr
data_class = Data_Wrapper()
e = Desinations
e.destination = input("enter destination: ")

e.contact_name = input("contact name:")
e.emergency_phone_nr = input("emergency phone number:")


logic_class = Destinations_Logic(data_class)
result = logic_class.update_destination(e)
