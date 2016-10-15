
 
from django.contrib import admin

from . import models
from restbase.commons import CustomModelAdminMixin

 
class AdmissionTests(BaseTest):
     
     url = 'admission'
     
     fixtures = [' Admissions.json','patients.json']
         
     def test_createAdmissionByNotAllowed Admission(self):
         self.login('alicia-rn')
         response = self.read_one_record(suffix='writable')
         data = response.data
         data['id'] = None
         response = self.client.post(self.url,data)
         print(response.data)
         ''' access should be denied'''
         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
         
     def test_createAdmission(self):
         self.login('alicia-rn')
         response = self.read_one_record(suffix='writable')
         data = response.data
         data['id'] = None
         response = self.client.post(self.url,data)
         print(response.data)
         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class BedStayTests(BaseTest):
     
     url = 'bedStay'
     
     fixtures = [' BedStays.json','patients.json']
         
     def test_createBedStayByNotAllowed BedStay(self):
         self.login('alicia-rn')
         response = self.read_one_record(suffix='writable')
         data = response.data
         data['id'] = None
         response = self.client.post(self.url,data)
         print(response.data)
         ''' access should be denied'''
         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
         
     def test_createBedStay(self):
         self.login('alicia-rn')
         response = self.read_one_record(suffix='writable')
         data = response.data
         data['id'] = None
         response = self.client.post(self.url,data)
         print(response.data)
         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

 
 