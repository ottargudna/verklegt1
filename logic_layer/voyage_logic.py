from Model.voyage import Voyage


class Voyage_Logic:
    
    def __init__(self, data_connection):
        self.data_wrapper = data_connection

    def create_voyage(self, voyage):
        """Takes in destination object and forwards it to the data layer"""
        self.data_wrapper.create_voyage(voyage)


    def schedule_voyage(self):
        pass

    def get_all_voyages(self):
        self.data_wrapper.get_all_voyages()



<<<<<<< HEAD



    def check_working_status(self, date):
        voyages = self.get_all_voyages()
        voyages_in_date = []
        every_employee = self.get_all_employee()

        for voyage in voyages:
            if voyages[3] >= date <= voyages[4]:
=======
    def check_working_status_day(self, date="yyyy.mm.dd"):
        voyages = self.data_wrapper.get_all_voyages()
        voyages_in_date = []
        every_employee = self.data_wrapper.get_all_employees()



        for voyage in voyages:
            if voyage.date_out == date or date == voyage.date_home:
>>>>>>> ottar5
                voyages_in_date.append(voyage)

        working = []
        not_working = []    
        for voyage in voyages_in_date:
<<<<<<< HEAD
            working.append(voyage[5])
            working.append(voyage[6])
            working.append(voyage[7])
            working.append(voyage[8])
            working.append(voyage[9])

        for employee in every_employee:
            if employee[0] not in working:
                not_working.append(employee[0])

        return working, not_working


    
=======
            working.append(voyage.captain)
            working.append(voyage.copilot)
            working.append(voyage.flight_service_manager)
            working.append(voyage.flight_attendant1)
            working.append(voyage.flight_attendant2)

        for employee in every_employee:
            if employee.nid not in working:
                not_working.append(employee.nid)

        return working, not_working
    # if you want a list of who are working on the date you do [0] and not working [1]


    """def check_working_status_week(self, date="yyyy.mm.dd"):
        voyages = self.data_wrapper.get_all_voyages()
        voyages_in_date = []
        every_employee = self.data_wrapper.get_all_employees()

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

        for employee in every_employee:
            if employee.nid not in working:
                not_working.append(employee.nid)

        return working, not_working"""
    # if you want a list of who are working on the date you do [0] and not working [1]

>>>>>>> ottar5
