from Model.voyage import Voyage
from datetime import datetime, timedelta
from data_layer.data_wrapper import Data_Wrapper


class Voyage_Logic:
    
    def __init__(self, data_connection):
        self.data_wrapper = Data_Wrapper()

    def create_voyage(self, voyage):
        """Takes in destination object and forwards it to the data layer"""
        every_voyage = self.data_wrapper.get_all_voyages()
        for v in every_voyage:
            if voyage == v:
                return False #already exists
        check_everything = self.check_everything
        if check_everything == False:
            return False #please enter correct data
        else:
            self.data_wrapper.create_voyage(voyage)


    def check_everything(self, voyage):
        check_if_employee_exists = self.check_if_employee_exists(voyage)
        if check_if_employee_exists == False:
            return False #employee dose not exist
        check_aircraft = self.check_aircraft_id
        if check_aircraft == False:
            return False # aircaft dose not exist
        check_arr_destination = self.check_arr_destination(voyage)
        check_dep_destination = self.check_dep_destination(voyage)
        if check_dep_destination == False or check_arr_destination == False:
            return False # destination dose not exist
        check_date_out = self.date_time(voyage.date_out)
        if check_date_out == None:
            return False #date is not correct
        check_date_home = self.date_time(voyage.date_home)
        if check_date_home == None:
            return False #date is not correct
        if check_date_out > check_date_home:
            return False #home date is bigger then out date
        check_correct_role = self.in_correct_role(voyage)
        if check_correct_role == False:
            return False #check if everyone is in correct role
        check_if_employee_working = self.check_working(voyage)
        if check_if_employee_working == True:
            return False #employee is already working
        
        


    def check_dep_destination(self, voyage):
        every_destination = self.data_wrapper.get_all_destinations()
        every_airport = []
        for dest in every_destination:
            every_airport.append(dest.airport_initials)
        if voyage.dep_from not in every_airport:
            return False

    def check_arr_destination(self, voyage):
        every_destination = self.data_wrapper.get_all_destinations()
        every_airport = []
        for dest in every_destination:
            every_airport.append(dest.airport_initials)
        if voyage.arr_at not in every_airport:
            return False

    def check_aircraft_id(self,voyage):
        every_airplane = self.data_wrapper.get_all_airplanes()
        every_airplane_id = []
        for plane in every_airplane:
            every_airplane_id.append(plane.aircraft_id)
        if voyage.aircraft_id not in every_airplane_id:
            return False

    def get_all_pilots(self):
        '''gets all pilots'''
        pilots = self.get_all_captains() + self.get_all_copilots()
        return pilots
    
    def get_all_crew(self):
        '''gets all crew'''
        crew = self.get_all_fa() + self.get_all_fsm()
        return crew
    def in_correct_role(self, voyage):
        all_captains = self.get_all_captains()
        if voyage.captain not in all_captains:
            return False
        all_copilots = self.get_all_copilots()
        if voyage.copilot not in all_copilots:
            return False
        all_fsm = self.get_all_fsm()
        if voyage.flight_service_manager not in all_fsm:
            return False
        all_fa = self.get_all_fa()
        if voyage.flight_attendant1 not in all_fa or voyage.flight_attendant2 not in all_fa:
            return False

    def get_all_captains(self):
        every_employee = self.data_wrapper.get_all_employees()
        captains = []
        for employee in every_employee:
            if employee.rank == "Captain":
                captains.append(employee.nid)
        return captains
    
    def get_all_copilots(self):
        every_employee = self.data_wrapper.get_all_employees()
        copilots = []
        for employee in every_employee:
            if employee.rank == "Copilot":
                copilots.append(employee.nid)
        return copilots
    
    def get_all_fsm(self):
        every_employee = self.data_wrapper.get_all_employees()
        fsm = []
        for employee in every_employee:
            if employee.rank == "Flight Service Manager":
                fsm.append(employee.nid)
        return fsm
    
    def get_all_fa(self):
        every_employee = self.data_wrapper.get_all_employees()
        fa = []
        for employee in every_employee:
            if employee.rank == "Flight Attendant":
                fa.append(employee.nid)
        return fa
    

    def check_if_employee_exists(self, voyage):
        every_employee = self.data_wrapper.get_all_employees()
        nids = []
        for em in every_employee:
            nids.append(em.nid)

        if voyage.captain in nids or voyage.captain == "N/A":
            if voyage.copilot in nids or voyage.copilot == "N/A":
                if voyage.flight_service_manager in nids or voyage.flight_service_manager == "N/A":
                    if voyage.flight_attendant1 in nids or voyage.flight_attendant1 == "N/A":
                        if voyage.flight_attendant2 in nids or voyage.flight_attendant2 == "N/A":
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
        
    def check_working(self, voyage):
        #check if employee alredy working that day

        date_out = voyage.date_out
        date_home = voyage.date_home
        
        working_out_date = self.check_day(date_out)
        working_out_date = working_out_date[0]
        working_home_date = self.check_day(date_home)
        working_home_date = working_home_date[0]

        already_working = working_out_date + working_home_date

        if voyage.captain in already_working:
            #Captain is already working that day
            return True
        elif voyage.copilot in already_working:
            #copilot is already working that day
            return True
        elif voyage.flight_service_manager in already_working:
            #Flight service manager is already working that day
            return True
        elif voyage.flight_attendant1 in already_working or voyage.flight_attendant2 in already_working and voyage.flight_attendant2 == voyage.flight_attendant1:
            #Flight attented is already working that day or it is the same flight attendent
            return True
        else: 
            return False
        

    def get_all_voyages(self):
        '''Gets all voyages'''
        return self.data_wrapper.get_all_voyages()

    

    def date_time(self, date):
        '''gets date and time, splits it and makes so you can calculate'''
            #date is an str yyyy.mm.dd
            #we need to split it
        try:
            year, month, day = map(int, date.split("."))
            result_date = datetime(year, month, day)
            return result_date
        except ValueError:
            return None

    def date_time_plus_week(self, date):
        '''adds 7 days to a date thefore a week'''
        try:
            date = self.date_time(date)
            if date == None:
                return None
            else:
                week_from_date = date + timedelta(days=7)
            return week_from_date
        except ValueError or TypeError:
            return None

    def check_day(self, date="yyyy.mm.dd"):
        '''checks if people are working, not working on perticuler 
        day and also gets every voyages on that day'''

        #get every voyage and employee
        voyages = self.data_wrapper.get_all_voyages()
        every_employee = self.data_wrapper.get_all_employees()
        
        #list of voyages at that date
        voyages_in_date = []

        search_date = self.date_time(date) 

        #checks every voyage and appends if thay are the same as out pr home date
        for voyage in voyages:
            date_out = self.date_time(voyage.date_out)
            date_home = self.date_time(voyage.date_home)
            if date_out == search_date or date_home == search_date:
                voyages_in_date.append(voyage)



        working_nid = []    #nid for employees working that day
        not_working = []    #employee that are not working (every information)
        working = []        #employee that are working (every information)
        dest = []

        for voyage in voyages_in_date:
            #only gets nid's
            working_nid.append(voyage.captain)
            dest.append(voyage.arr_at)
            working_nid.append(voyage.copilot)
            dest.append(voyage.arr_at)
            working_nid.append(voyage.flight_service_manager)
            dest.append(voyage.arr_at)
            working_nid.append(voyage.flight_attendant1)
            dest.append(voyage.arr_at)
            working_nid.append(voyage.flight_attendant2)
            dest.append(voyage.arr_at)


        #gets every working employee informations
        counter = 0
        for employee in every_employee:
            for nid in working_nid:
                if nid == employee.nid:
                    employee_destination = (employee, dest[counter])
                    working.append(employee_destination)
                    counter += 1


        #not working function
        for employee in every_employee:
            if employee.nid not in working:
                not_working.append(employee)

        return working, not_working, voyages_in_date
     # if you want a list of who are working on the date you do [0], not working [1], voyages on that day [2]


    def check_week(self, date="yyyy.mm.dd"): #enter the first day in that week
        '''checks if people are working, not working on perticuler 
        week and also gets every voyages on that week'''
        #get every employee and voyages
        voyages = self.data_wrapper.get_all_voyages()
        every_employee = self.data_wrapper.get_all_employees()
        #list of voyages at that date
        voyages_in_date = []


        search_date = self.date_time(date) 
        week_from_date = self.date_time_plus_week(date)

        for voyage in voyages:
            date_out = self.date_time(voyage.date_out)
            date_home = self.date_time(voyage.date_home)
            if  search_date <= date_out <= week_from_date or search_date <= date_home <= week_from_date :
                voyages_in_date.append(voyage)

        working_nid = []    #nid for employees working that day
        not_working = []    #employee that are not working (every information)
        working = []        #employee that are working (every information)
        dest = []

        for voyage in voyages_in_date:
            #only gets nid's
            working_nid.append(voyage.captain)
            dest.append(voyage.arr_at)
            working_nid.append(voyage.copilot)
            dest.append(voyage.arr_at)
            working_nid.append(voyage.flight_service_manager)
            dest.append(voyage.arr_at)
            working_nid.append(voyage.flight_attendant1)
            dest.append(voyage.arr_at)
            working_nid.append(voyage.flight_attendant2)
            dest.append(voyage.arr_at)


        #gets every working employee informations
        counter = 0
        for employee in every_employee:
            for nid in working_nid:
                if nid == employee.nid:
                    employee_destination = (employee, dest[counter])
                    working.append(employee_destination)
                    counter += 1

        #not working function
        for employee in every_employee:
            if employee.nid not in working:
                not_working.append(employee)

        return working, not_working,voyages_in_date
    # if you want a list of who are working on the date you do [0], not working [1], voyages in that time period [2]


    def generte_voyage_nr(self):
        '''Create voyage number, counts all voyages and then gives it a number'''
        voyages = self.data_wrapper.get_all_voyages()
        count_voyages = len(voyages)

        begin = "NA"
        number = count_voyages + 1
        if len(str(number)) == 3:
            return begin+number
        elif len(str(number)) == 2:
            return f"{begin}0{number}"
        elif len(str(number)) == 1:
            return f"{begin}00{number}"
        else:
            return False

