class Patient:
  def __init__(self, name, bill_amount):
    self.name = name
    self.bill_amount = bill_amount

  def get_name(self):
    return self.name

  def set_name(self, name):
    self.name = name

  def get_bill_amount(self):
    return self.bill_amount

  def set_bill_amoint(self, bill_amount):
    self.bill_amount = bill_amount

  def calculate_bill(self):
    return self.bill_amount

  def display_patient_type(self):
    print("Patient Type: Regular Patient")


class SeniorPatient(Patient):
  def calculate_bill(self):
    return self.bill_amount*0.80

  def display_patient_type(self):
    print("Patient Type: Senior Citizen")


class PhilHealth(Patient):
  def calculate_bill(self):
