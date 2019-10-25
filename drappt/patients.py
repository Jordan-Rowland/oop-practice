from datetime import datetime
import json

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
                f.write(f"{p.name},{json.dumps(p.prescriptions)}," \
                        f"{'<==>'.join(p._patient_notes) if p._patient_notes else ''}")
                f.write("\n")

    def load_database(self):
        with open(self.filename, "r") as f:
            for line in f.readlines()[1:]:
                print(line.split(','))
                name, prescriptions, notes = line.split(',')
                notes = notes[:-1].split('<==>') if notes[:-1] else []
                print(notes)
                self.append(Patient(name, json.loads(prescriptions), notes))

    def find(self, name):
        found_user = [x for x in self if name.lower() == x.name.lower()]
        if found_user:
            return found_user[0]

    def __str__(self):
        names = [patient.name for patient in self]
        return '\n'.join(names)
