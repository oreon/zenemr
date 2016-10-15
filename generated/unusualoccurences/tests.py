
 
from django.contrib import admin

from . import models
from restbase.commons import CustomModelAdminMixin

 
class UnusualOccurenceTests(BaseTest):
     
     url = 'unusualOccurence'
     
     fixtures = [' UnusualOccurences.json','patients.json']
         
     def test_createUnusualOccurenceByNotAllowed UnusualOccurence(self):
         self.login('alicia-rn')
         response = self.read_one_record(suffix='writable')
         data = response.data
         data['id'] = None
         response = self.client.post(self.url,data)
         print(response.data)
         ''' access should be denied'''
         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
         
     def test_createUnusualOccurence(self):
         self.login('alicia-rn')
         response = self.read_one_record(suffix='writable')
         data = response.data
         data['id'] = None
         response = self.client.post(self.url,data)
         print(response.data)
         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class OccurenceTypeTests(BaseTest):
     
     url = 'occurenceType'
     
     fixtures = [' OccurenceTypes.json','patients.json']
         
     def test_createOccurenceTypeByNotAllowed OccurenceType(self):
         self.login('alicia-rn')
         response = self.read_one_record(suffix='writable')
         data = response.data
         data['id'] = None
         response = self.client.post(self.url,data)
         print(response.data)
         ''' access should be denied'''
         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
         
     def test_createOccurenceType(self):
         self.login('alicia-rn')
         response = self.read_one_record(suffix='writable')
         data = response.data
         data['id'] = None
         response = self.client.post(self.url,data)
         print(response.data)
         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

 
 