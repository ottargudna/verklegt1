from Model.voyage import Voyage
from datetime import datetime, timedelta


class Voyage_Logic:
    
    def __init__(self, data_connection):
        self.data_wrapper = data_connection

    def create_voyage(self, voyage):
        """Takes in destination object and forwards it to the data layer"""
        self.data_wrapper.create_voyage(voyage)


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
        voyages = self.data_wrapper.get_all_voyages()
        every_employee = self.data_wrapper.get_all_employees()

        voyages_in_date = []

        for voyage in voyages:
            if voyage.date_out == date or date == voyage.date_home:
                voyages_in_date.append(voyage)

        working = []
        not_working = []    
        for voyage in voyages_in_date:

            working.append(voyage.captain)
            working.append(voyage.copilot)
            working.append(voyage.flight_service_manager)
            working.append(voyage.flight_attendant1)
            working.append(voyage.flight_attendant2)

        #not working function
        for employee in every_employee:
            if employee.nid not in working:
                not_working.append(employee.nid)

        return working, not_working, voyages_in_date
     # if you want a list of who are working on the date you do [0], not working [1], voyages on that day [2]


    def check_week(self, date="yyyy.mm.dd"): #enter the first day in that week
        '''checks if people are working, not working on perticuler 
        week and also gets every voyages on that week'''
        voyages = self.data_wrapper.get_all_voyages()
        every_employee = self.data_wrapper.get_all_employees()
        voyages_in_date = []
        search_date = self.date_time(date)
        week_from_date = self.date_time_plus_week(date)

        for voyage in voyages:
            date_out = self.date_time(voyage.date_out)
            date_home = self.date_time(voyage.date_home)
            if  search_date <= date_out <= week_from_date or search_date <= date_home <= week_from_date :
                voyages_in_date.append(voyage)

        working = []
        not_working = []    
        for voyage in voyages_in_date:
            working.append(voyage.captain)
            working.append(voyage.copilot)
            working.append(voyage.flight_service_manager)
            working.append(voyage.flight_attendant1)
            working.append(voyage.flight_attendant2)

        #not working function
        for employee in every_employee:
            if employee.nid not in working:
                not_working.append(employee.nid)

        return working, not_working,voyages_in_date
    # if you want a list of who are working on the date you do [0], not working [1], voyages in that time period [2]
