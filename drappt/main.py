from datetime import datetime
import json
from os import rename

class Administrator:
    """Base class for Doctor and Receptionist classes. Hashes an employee ID based on the name
    and salary of the initialized employee."""
    def __init__(self, name, salary, hourly):
        self.name = name
        self.salary = salary
        self.eid = abs(hash(self.name + str(self.salary)))
        self.hourly = hourly

    def update_file(self, patient, note):
        """Updates patient notes. Accepts a Patient object, and a note."""
        patient.notes = note

    def __str__(self):
        return self.name


class Doctor(Administrator):
    """Initializes with 'hourly=False' by default."""
    def __init__(self, name, salary, hourly=False):
        super().__init__(name, salary, hourly)
        self.hourly = hourly

    def write_prescription(self, patient, medicine, dosage):
        """Adds or updates prescriptions on Patient object. Accepts a medicine name and dosage."""
        patient.prescriptions[medicine] = dosage
        return patient.prescriptions


class Receptionist(Administrator):
    """Initializes with 'hourly=False' be default and has an 'hours_accrued' attribute for
    calculating payroll."""
    def __init__(self, name, salary, hourly=True, hours_accrued=0):
        super().__init__(name, salary, hourly)
        self.hourly = hourly
        self.hours_accrued = hours_accrued

    def schedule_patient(self, patient):
        """Schedules patients in calendar object. Doctors cannot do this because they cannot manage
        their own schedules."""
        print(f'schedule {patient}')

    def timecard(self, time):
        """Adds a time argument to the 'hours_accrued' attribute for calculating payroll."""
        self.hours_accrued += time


class Patient:
    """Has prescriptions and notes attributes for managing patients."""
    def __init__(self, name, prescriptions={}, _patient_notes=[]):
        self.name = name
        self.prescriptions = prescriptions
        self._patient_notes = _patient_notes

    def request_appointment(self, time):
        """Requests appointments on Calendar object."""
        print(f'request at {time}')

    def __str__(self):
        return f"[Patient]{self.name}"

    @property
    def notes(self):
        return self._patient_notes

    @notes.setter
    def notes(self, note):
        self._patient_notes.append(f'[{str(datetime.now())[:-7]}] - {note}')


class PatientRecords(list):
    """Holds list of patients"""
    def __init__(self, filename):
        self.filename = filename
        self.load_database()

    def append(self, patient):
        if not isinstance(patient, Patient):
            raise TypeError('Only patients can be added')
        super().append(patient)

    def write_database(self):
        """Writes all patients to database."""
        with open(self.filename, 'w') as f:
            f.write('name,prescriptions,notes\n')
            for p in self:
                f.write(f"{p.name},{json.dumps(p.prescriptions)},"
                        f"{'<==>'.join(p._patient_notes) if p._patient_notes else []}\n")

    def load_database(self):
        with open(self.filename, "r") as f:
            for line in f.readlines()[1:]:
                name, prescriptions, notes = line.split(',')
                self.append(Patient(name, prescriptions, notes))

    def find(self, name):
        found_user = [x for x in self if name.lower() == x.name.lower()]
        if found_user:
            return found_user[0]

    def __str__(self):
        names = [patient.name for patient in self]
        return '\n'.join(names)


class PayRoll(list):
    """Extends List class, acts as a singleton and maintains employee roster."""

    def __init__(self, filename):
        self.filename = filename
        self.load_database()

    def calculate_payroll(self):
        """Takes no arguments, runs payroll on contents of self."""
        print([str(datetime.now())[:-7]])
        for employee in self:
            if employee.hourly:
                print(f'{employee.name} - ${employee.salary * employee.hours_accrued}')
                employee.hours_accrued = 0
            else:
                print(f'{employee.name} - ${employee.salary / 25}')

    def append(self, employee):
        """Appends new Employee object of either type, and checks for existing employee IDs."""
        if not isinstance(employee, Administrator):
            raise TypeError('Only employees can be added')
        eids = [e.eid for e in self]
        if employee.eid in eids:
            raise Exception('Employee ID already exists')
        super().append(employee)

    def load_database(self):
        """Reinitializes employees and payroll from CSV file."""
        with open(self.filename, 'r') as f:
            for line in f.readlines()[1:]:
                _, position, name, salary, hourly, hours_accrued = line.split(',')
                if position == 'Doctor':
                    self.append(Doctor(name, int(salary)))
                elif position == 'Receptionist':
                    self.append(Receptionist(name, int(salary), hourly, int(hours_accrued)))

    def write_database(self):
        """Writes all employees to database."""
        with open(self.filename, 'r') as original_file:
            with open('tmp.csv', "w") as f:
                f.write('eid,position,name,salary,hourly,hours_accrued\n')
                if self:
                    for employee in self:
                        if isinstance(employee, Doctor):
                          f.write(f'{employee.eid},Doctor,{employee.name},{employee.salary},'
                                  f'{employee.hourly},None\n')
                        elif isinstance(employee, Receptionist):
                            f.write(f'{employee.eid},Receptionist,{employee.name},'
                                    f'{employee.salary},{employee.hourly},'
                                    f'{employee.hours_accrued}\n')
        rename('tmp.csv', self.filename)

    def find(self, name):
        """Finds and returns"""
        found_user = [x for x in self if name.lower() == x.name.lower()]
        if found_user:
            return found_user[0]

    def __str__(self):
        names = [f"{'[D]' if isinstance(employee, Doctor) else '[R]'}{employee.name}"
                 for employee in self]
        return '\n'.join(names)


class Calendar(dict):
    def __init__(self, filename):
        self.filename = filename
        self['monday'] = {'12pm': [], '1pm': [], '2pm': [], '3pm': [], '4pm': []}
        self['tuesday'] = {'12pm': [], '1pm': [], '2pm': [], '3pm': [], '4pm': []}
        self['wednesday'] = {'12pm': [], '1pm': [], '2pm': [], '3pm': [], '4pm': []}
        self['thursday'] = {'12pm': [], '1pm': [], '2pm': [], '3pm': [], '4pm': []}
        self['friday'] = {'12pm': [], '1pm': [], '2pm': [], '3pm': [], '4pm': []}

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
        # TODO: Fix issue where next appt at same time not saving
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


providers = PayRoll('employees.csv')
patients = PatientRecords('patients.csv')
c = Calendar('appointments.csv')


# c.book_appt('tuesday', 3, 'jim kelly', 'julie kerns')
# c.book_appt('Friday', 1,  'jim kelly', 'jim fellows')
# c.book_appt('Friday', 12, 'jim kelly', 'pam fellows')
# c.book_appt('Friday', 12, 'richard davies', 'karen freedman')


c.load_database()
c.show_calendar()
