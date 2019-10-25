class Calendar(dict):
    def __init__(self, filename):
        self.filename = filename
        self['monday'] = {'12pm': [], '1pm': [], '2pm': [], '3pm': [], '4pm': []}
        self['tuesday'] = {'12pm': [], '1pm': [], '2pm': [], '3pm': [], '4pm': []}
        self['wednesday'] = {'12pm': [], '1pm': [], '2pm': [], '3pm': [], '4pm': []}
        self['thursday'] = {'12pm': [], '1pm': [], '2pm': [], '3pm': [], '4pm': []}
        self['friday'] = {'12pm': [], '1pm': [], '2pm': [], '3pm': [], '4pm': []}
        self.load_database()

    def show_appt(self, day, time):
        appt = self.get(day.lower()).get(f"{time}pm")
        if appt:
            print(f"{appt[0]} -- {appt[1]}")
        else:
            print('No appointment at this time.')

    def book_appt(self, day, time, doctor, patient):
        time = time if str(time).endswith('pm') else f"{time}pm"
        if time not in ['12pm', '1pm', '2pm', '3pm', '4pm']:
            print('This time is not available. Please select a time between 12pm and 4pm.')
            return
        appt = self.get(day.lower()).get(time)
        appt_details = [doctor, patient]
        if not appt:
            self[day.lower()][time] = [appt_details]
        else:
            doctor_names = [details[0].lower() for details in appt]
            if doctor.lower() in doctor_names:
                print(f'Appointment slot with {doctor.title()} at {time} on {day.title()}' \
                      'already booked.'
                      '\nPlease choose another time, or delete the existing appointment.')
                return
            appt.append(appt_details)
        print(f"Appointment confirmed at {time} on {day.title()} for {patient.title()} with " \
              f"{doctor.title()}")

    def remove_appt(self, day, time, doctor_name=None):
        day = day.lower()
        doctor_name = doctor_name.lower() if doctor_name else None
        appts = self.get(day).get(f"{time}pm")
        if not appts:
            print('No appointments at this time to delete')
            self.show_calendar()
            return
        if not doctor_name:
            del appts[0]
            self.show_calendar()
            return
        for appointment in appts:
            if doctor_name in appointment[0].name.lower():
                appts.remove(appointment)
                self.show_calendar()
                return
        print(f"No appointments on {day.title()} at {time} with Dr. {doctor_name.title()}")

    def show_calendar(self):
        print()
        for day, times in self.items():
            print('=' * 50)
            print(day.title())
            for time, details in times.items():
                if details:
                    print(f"\t{time}")
                    print(f"\t{'-' * 10}")
                    for appt in details:
                        print(f"\t{appt[0].title()} - [PATIENT]{appt[1].title()[:-1]}")
                    print(f"\t{'-' * 42}")
        print('=' * 50)

    def load_database(self):
        with open(self.filename, 'r') as f:
            for line in f.readlines()[1:]:
                day, time, doctor, patient = line.split(',')
                self.book_appt(day, time, doctor, patient)

    def write_database(self):
        with open(self.filename, 'w') as f:
            f.write('day,time,doctor,patient\n')
            for day, times in self.items():
                for time, details in times.items():
                    if details:
                        for detail in details:
                            f.write(f"{day},{time},{detail[0]},{detail[1]}\n")
        print('Appointments written to database')
