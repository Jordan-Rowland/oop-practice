
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
        with open(self.filename, 'r') as f:
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

    def find(self, name):
        """Finds and returns"""
        found_user = [x for x in self if name.lower() == x.name.lower()]
        if found_user:
            return found_user[0]

    def __str__(self):
        names = [f"{'[D]' if isinstance(employee, Doctor) else '[R]'}{employee.name}"
                 for employee in self]
        return '\n'.join(names)
