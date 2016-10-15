
 
from django.contrib import admin

from . import models
from restbase.commons import CustomModelAdminMixin

 
class AtcDrugTests(BaseTest):
     
     url = 'atcDrug'
     
     fixtures = [' AtcDrugs.json','patients.json']
         
     def test_createAtcDrugByNotAllowed AtcDrug(self):
         self.login('alicia-rn')
         response = self.read_one_record(suffix='writable')
         data = response.data
         data['id'] = None
         response = self.client.post(self.url,data)
         print(response.data)
         ''' access should be denied'''
         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
         
     def test_createAtcDrug(self):
         self.login('alicia-rn')
         response = self.read_one_record(suffix='writable')
         data = response.data
         data['id'] = None
         response = self.client.post(self.url,data)
         print(response.data)
         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class DrugTests(BaseTest):
     
     url = 'drug'
     
     fixtures = [' Drugs.json','patients.json']
         
     def test_createDrugByNotAllowed Drug(self):
         self.login('alicia-rn')
         response = self.read_one_record(suffix='writable')
         data = response.data
         data['id'] = None
         response = self.client.post(self.url,data)
         print(response.data)
         ''' access should be denied'''
         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
         
     def test_createDrug(self):
         self.login('alicia-rn')
         response = self.read_one_record(suffix='writable')
         data = response.data
         data['id'] = None
         response = self.client.post(self.url,data)
         print(response.data)
         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class DrugInteractionTests(BaseTest):
     
     url = 'drugInteraction'
     
     fixtures = [' DrugInteractions.json','patients.json']
         
     def test_createDrugInteractionByNotAllowed DrugInteraction(self):
         self.login('alicia-rn')
         response = self.read_one_record(suffix='writable')
         data = response.data
         data['id'] = None
         response = self.client.post(self.url,data)
         print(response.data)
         ''' access should be denied'''
         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
         
     def test_createDrugInteraction(self):
         self.login('alicia-rn')
         response = self.read_one_record(suffix='writable')
         data = response.data
         data['id'] = None
         response = self.client.post(self.url,data)
         print(response.data)
         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class DrugCategoryTests(BaseTest):
     
     url = 'drugCategory'
     
     fixtures = [' DrugCategorys.json','patients.json']
         
     def test_createDrugCategoryByNotAllowed DrugCategory(self):
         self.login('alicia-rn')
         response = self.read_one_record(suffix='writable')
         data = response.data
         data['id'] = None
         response = self.client.post(self.url,data)
         print(response.data)
         ''' access should be denied'''
         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
         
     def test_createDrugCategory(self):
         self.login('alicia-rn')
         response = self.read_one_record(suffix='writable')
         data = response.data
         data['id'] = None
         response = self.client.post(self.url,data)
         print(response.data)
         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

 
 