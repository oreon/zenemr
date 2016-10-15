# 
#  
# from django.contrib import admin
# 
# from . import models
# from .commons import CustomModelAdminMixin
# 
#  
# class DrugTests(BaseTest):
#      
#      url = 'drug'
#      
#      fixtures = [' Drugs.json','patients.json']
#          
#      def test_createDrugByNotAllowed Drug(self):
#          self.login('alicia-rn')
#          response = self.read_one_record(suffix='writable')
#          data = response.data
#          data['id'] = None
#          response = self.client.post(self.url,data)
#          print(response.data)
#          ''' access should be denied'''
#          self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
#          
#      def test_createDrug(self):
#          self.login('alicia-rn')
#          response = self.read_one_record(suffix='writable')
#          data = response.data
#          data['id'] = None
#          response = self.client.post(self.url,data)
#          print(response.data)
#          self.assertEqual(response.status_code, status.HTTP_201_CREATED)
# 
# class CategoryTests(BaseTest):
#      
#      url = 'category'
#      
#      fixtures = [' Categorys.json','patients.json']
#          
#      def test_createCategoryByNotAllowed Category(self):
#          self.login('alicia-rn')
#          response = self.read_one_record(suffix='writable')
#          data = response.data
#          data['id'] = None
#          response = self.client.post(self.url,data)
#          print(response.data)
#          ''' access should be denied'''
#          self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
#          
#      def test_createCategory(self):
#          self.login('alicia-rn')
#          response = self.read_one_record(suffix='writable')
#          data = response.data
#          data['id'] = None
#          response = self.client.post(self.url,data)
#          print(response.data)
#          self.assertEqual(response.status_code, status.HTTP_201_CREATED)
# 
# class PatientTests(BaseTest):
#      
#      url = 'patient'
#      
#      fixtures = [' Patients.json','patients.json']
#          
#      def test_createPatientByNotAllowed Patient(self):
#          self.login('alicia-rn')
#          response = self.read_one_record(suffix='writable')
#          data = response.data
#          data['id'] = None
#          response = self.client.post(self.url,data)
#          print(response.data)
#          ''' access should be denied'''
#          self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
#          
#      def test_createPatient(self):
#          self.login('alicia-rn')
#          response = self.read_one_record(suffix='writable')
#          data = response.data
#          data['id'] = None
#          response = self.client.post(self.url,data)
#          print(response.data)
#          self.assertEqual(response.status_code, status.HTTP_201_CREATED)
# 
# class PrescriptionTests(BaseTest):
#      
#      url = 'prescription'
#      
#      fixtures = [' Prescriptions.json','patients.json']
#          
#      def test_createPrescriptionByNotAllowed Prescription(self):
#          self.login('alicia-rn')
#          response = self.read_one_record(suffix='writable')
#          data = response.data
#          data['id'] = None
#          response = self.client.post(self.url,data)
#          print(response.data)
#          ''' access should be denied'''
#          self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
#          
#      def test_createPrescription(self):
#          self.login('alicia-rn')
#          response = self.read_one_record(suffix='writable')
#          data = response.data
#          data['id'] = None
#          response = self.client.post(self.url,data)
#          print(response.data)
#          self.assertEqual(response.status_code, status.HTTP_201_CREATED)
# 
# class PrescriptionItemTests(BaseTest):
#      
#      url = 'prescriptionItem'
#      
#      fixtures = [' PrescriptionItems.json','patients.json']
#          
#      def test_createPrescriptionItemByNotAllowed PrescriptionItem(self):
#          self.login('alicia-rn')
#          response = self.read_one_record(suffix='writable')
#          data = response.data
#          data['id'] = None
#          response = self.client.post(self.url,data)
#          print(response.data)
#          ''' access should be denied'''
#          self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
#          
#      def test_createPrescriptionItem(self):
#          self.login('alicia-rn')
#          response = self.read_one_record(suffix='writable')
#          data = response.data
#          data['id'] = None
#          response = self.client.post(self.url,data)
#          print(response.data)
#          self.assertEqual(response.status_code, status.HTTP_201_CREATED)
# 
# class EmployeeTests(BaseTest):
#      
#      url = 'employee'
#      
#      fixtures = [' Employees.json','patients.json']
#          
#      def test_createEmployeeByNotAllowed Employee(self):
#          self.login('alicia-rn')
#          response = self.read_one_record(suffix='writable')
#          data = response.data
#          data['id'] = None
#          response = self.client.post(self.url,data)
#          print(response.data)
#          ''' access should be denied'''
#          self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
#          
#      def test_createEmployee(self):
#          self.login('alicia-rn')
#          response = self.read_one_record(suffix='writable')
#          data = response.data
#          data['id'] = None
#          response = self.client.post(self.url,data)
#          print(response.data)
#          self.assertEqual(response.status_code, status.HTTP_201_CREATED)
# 
# class VaccinationTests(BaseTest):
#      
#      url = 'vaccination'
#      
#      fixtures = [' Vaccinations.json','patients.json']
#          
#      def test_createVaccinationByNotAllowed Vaccination(self):
#          self.login('alicia-rn')
#          response = self.read_one_record(suffix='writable')
#          data = response.data
#          data['id'] = None
#          response = self.client.post(self.url,data)
#          print(response.data)
#          ''' access should be denied'''
#          self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
#          
#      def test_createVaccination(self):
#          self.login('alicia-rn')
#          response = self.read_one_record(suffix='writable')
#          data = response.data
#          data['id'] = None
#          response = self.client.post(self.url,data)
#          print(response.data)
#          self.assertEqual(response.status_code, status.HTTP_201_CREATED)
# 
# class EncounterTests(BaseTest):
#      
#      url = 'encounter'
#      
#      fixtures = [' Encounters.json','patients.json']
#          
#      def test_createEncounterByNotAllowed Encounter(self):
#          self.login('alicia-rn')
#          response = self.read_one_record(suffix='writable')
#          data = response.data
#          data['id'] = None
#          response = self.client.post(self.url,data)
#          print(response.data)
#          ''' access should be denied'''
#          self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
#          
#      def test_createEncounter(self):
#          self.login('alicia-rn')
#          response = self.read_one_record(suffix='writable')
#          data = response.data
#          data['id'] = None
#          response = self.client.post(self.url,data)
#          print(response.data)
#          self.assertEqual(response.status_code, status.HTTP_201_CREATED)
# 
# class VaccineTests(BaseTest):
#      
#      url = 'vaccine'
#      
#      fixtures = [' Vaccines.json','patients.json']
#          
#      def test_createVaccineByNotAllowed Vaccine(self):
#          self.login('alicia-rn')
#          response = self.read_one_record(suffix='writable')
#          data = response.data
#          data['id'] = None
#          response = self.client.post(self.url,data)
#          print(response.data)
#          ''' access should be denied'''
#          self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
#          
#      def test_createVaccine(self):
#          self.login('alicia-rn')
#          response = self.read_one_record(suffix='writable')
#          data = response.data
#          data['id'] = None
#          response = self.client.post(self.url,data)
#          print(response.data)
#          self.assertEqual(response.status_code, status.HTTP_201_CREATED)
# 
#  
#  