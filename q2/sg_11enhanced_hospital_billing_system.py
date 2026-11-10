class Patient:
  def __init__(self, name, bill):
    self.name = name
    self.bill = bill

def display_info(self):
  print("Patient Name:", self.name)
  print("Hospital Bill:", self.bill)


class SeniorPatient(Patient):
  def display_patient_type(self):
    print("Patient Type: Senior Citizen")


class PhilHealthPatient(Patient):
  print("Patient Type: PhilHealth Member")

patient1 = Patient("Juan Dela Cruz", 5000)
patient2 = SeniorPatient("Maria Santos", 5000)
patient3 = PhilHealthPatient("Pedro Reyes", 5000)

patient1.display_patient_type()
patient2.display_patient_type()
patient3.display_patient_type()
