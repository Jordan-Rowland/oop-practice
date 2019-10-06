from datetime import datetime


class Administrator:
    def __init__(self, name, salary, hourly):
        self.name = name
        self.salary = salary
        self.hourly = hourly

    def update_file(self, patient, note):
        patient.notes = note


class Doctor(Administrator):
    def __init__(self, name, salary, hourly=False):
        super().__init__(name, salary, hourly)
        self.hourly = hourly

    def write_prescription(self, patient, medicine, dosage):
        patient.prescriptions[medicine] = dosage
        return patient.prescriptions


class Receptionist(Administrator):
    def __init__(self, name, salary, hourly=True, hours_accrued=0):
        super().__init__(name, salary, hourly)
        self.hourly = hourly
        self.clocked_in = None
        self.hours_accrued = hours_accrued

    def schedule_patient(self, patient):
        print(f'schedule {patient}')

    def timecard(self, time):
        if not self.clocked_in:
            self.clocked_in = time
            print(f'Clocked in at {time}')
        else:
            self.hours_accrued += time - self.clocked_in
            print(f'Clocked out at {time}. {time - self.clocked_in} added to your timecard.')
            self.clocked_in = None


class Patient:
    def __init__(self, name):
        self.name = name
        self.prescriptions = {}
        self._patient_notes = []

    def request_appointment(self, time):
        print(f'request at {time}')

    @property
    def notes(self):
        return self._patient_notes

    @notes.setter
    def notes(self, note):
        self._patient_notes.append(f'[{str(datetime.now())[:-7]}] - {note}')


class TimeCard:
    timecards = []



class PayRoll(list):
    def calculate_payroll(self):
        print([str(datetime.now())[:-7]])
        for employee in self:
            if employee.hourly:
                print(f'{employee.name} - ${employee.salary * employee.hours_accrued}')
                employee.hours_accrued = 0
            else:
                print(f'{employee.name} - ${employee.salary / 25}')

    def append(self, employee, to_database=False):
        if not isinstance(employee, Administrator):
            raise TypeError('Only employees can be added')
        super().append(employee)
        if to_database:
            with open('employees.csv', 'a') as f:
                if isinstance(employee, Doctor):
                    f.write(f'Doctor,{employee.name},{employee.salary},{employee.hourly},\n')
                elif isinstance(employee, Receptionist):
                    f.write(f'Receptionist,{employee.name},{employee.salary},'
                    f'{employee.hourly},{employee.hours_accrued}\n')

    def load_database(self, filename):
        with open(filename, 'r') as f:
            for line in f.readlines()[1:]:
                position, name, salary, hourly, hours_accrued = line.split(',')
                if position == 'Doctor':
                    self.append(Doctor(name, int(salary)))
                elif position == 'Receptionist':
                    self.append(Receptionist(name, int(salary), hourly, int(hours_accrued)))

    def rewrite_to_database(self, filename):
        with open(filename, 'w') as f:
            f.write('position,name,salary,hourly,hours_accrued\n')
            for employee in self:
                if isinstance(employee, Doctor):
                    f.write(f'Doctor,{employee.name},{employee.salary},{employee.hourly},\n')
                if isinstance(employee, Receptionist):
                    f.write(f'Receptionist,{employee.name},{employee.salary},{employee.hourly},'
                            f'{employee.hours_accrued}\n')



p = PayRoll()
