from patients import Patient, PatientRecords
from employees import Doctor, Receptionist, PayRoll
from cal import Calendar


if __name__ == "__main__":
    providers = PayRoll('employees.csv')
    patients = PatientRecords('patients.csv')
    c = Calendar('appointments.csv')

    c.show_calendar()
