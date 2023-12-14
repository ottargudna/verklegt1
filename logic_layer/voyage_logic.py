from Model.voyage import Voyage
from datetime import datetime, timedelta


class Voyage_Logic:
    
    def __init__(self, data_connection):
        self.data_wrapper = data_connection

    def create_voyage(self, voyage):
        """Takes in destination object and forwards it to the data layer"""
        every_voyage = self.data_wrapper.get_all_voyages()
        for v in every_voyage:
            if voyage == v:
                return False #already exists
        check_if_employee_exists = self.check_if_employee_exists(voyage)
        if check_if_employee_exists == False:
            return False
        check_if_employee_working = self.check_working(voyage)
        if check_if_employee_working == True:
            return False
        else:
            self.data_wrapper.create_voyage(voyage)

    def check_if_employee_exists(self, voyage):
        every_employee = self.data_wrapper.get_all_employees()
        nids = every_employee[0]

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

        date_out = self.date_time(voyage[4])
        date_home = self.date_time(voyage[5])
        
        working_out_date = self.check_day(date_out)
        working_out_date = working_out_date[0]
        working_home_date = self.check_day(date_home)
        working_home_date = working_home_date[0]

        already_working = working_out_date + working_home_date

        if voyage[6] in already_working:
            #Captain is already working that day
            return True
        elif voyage[7] in already_working:
            #copilot is already working that day
            return True
        elif voyage[8] in already_working:
            #Flight service manager is already working that day
            return True
        elif voyage[9] in already_working:
            #Flight attented is already working that day
            return True
        elif voyage[10] in already_working:
            #Captain is alredy working that day
            return True
        else: 
            return False
        

    def get_all_voyages(self):
        '''Gets all voyages'''
        self.data_wrapper.get_all_voyages()

    

    def date_time(self, date):
        '''gets date and time, splits it and makes so you can calculate'''
            #date is an str yyyy.mm.dd
            #we need to split it
        try:
            year, month, day = map(int, date.split("."))
            result_date = datetime(year, month, day)
            return result_date
        except ValueError:
            return False

    def date_time_plus_week(self, date):
        '''adds 7 days to a date thefore a week'''
        int_date = self.date_time(date)

        week_from_date = int_date + timedelta(days=7)

        return week_from_date

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
            if date_out == search_date or date == search_date:
                voyages_in_date.append(voyage)



        working_nid = []    #nid for employees working that day
        not_working = []    #employee that are not working (every information)
        working = []        #employee that are working (every information)

        for voyage in voyages_in_date:
            #only gets nid's
            working_nid.append(voyage.captain)
            working_nid.append(voyage.copilot)
            working_nid.append(voyage.flight_service_manager)
            working_nid.append(voyage.flight_attendant1)
            working_nid.append(voyage.flight_attendant2)

        #gets every working employee informations
        for employee in every_employee:
            for nid in working_nid:
                if nid == employee.nid:
                    working.append(employee)

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
        
        for voyage in voyages_in_date:
            #only gets nid's
            working_nid.append(voyage.captain)
            working_nid.append(voyage.copilot)
            working_nid.append(voyage.flight_service_manager)
            working_nid.append(voyage.flight_attendant1)
            working_nid.append(voyage.flight_attendant2)

        #gets every working employee informations
        for employee in every_employee:
            for nid in working_nid:
                if nid == employee.nid:
                    working.append(employee)

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

