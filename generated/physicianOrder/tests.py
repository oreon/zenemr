
 
from django.contrib import admin

from . import models
from restbase.commons import CustomModelAdminMixin

 
class OrderTemplateTests(BaseTest):
     
     url = 'orderTemplate'
     
     fixtures = [' OrderTemplates.json','patients.json']
         
     def test_createOrderTemplateByNotAllowed OrderTemplate(self):
         self.login('alicia-rn')
         response = self.read_one_record(suffix='writable')
         data = response.data
         data['id'] = None
         response = self.client.post(self.url,data)
         print(response.data)
         ''' access should be denied'''
         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
         
     def test_createOrderTemplate(self):
         self.login('alicia-rn')
         response = self.read_one_record(suffix='writable')
         data = response.data
         data['id'] = None
         response = self.client.post(self.url,data)
         print(response.data)
         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class OrderTests(BaseTest):
     
     url = 'order'
     
     fixtures = [' Orders.json','patients.json']
         
     def test_createOrderByNotAllowed Order(self):
         self.login('alicia-rn')
         response = self.read_one_record(suffix='writable')
         data = response.data
         data['id'] = None
         response = self.client.post(self.url,data)
         print(response.data)
         ''' access should be denied'''
         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
         
     def test_createOrder(self):
         self.login('alicia-rn')
         response = self.read_one_record(suffix='writable')
         data = response.data
         data['id'] = None
         response = self.client.post(self.url,data)
         print(response.data)
         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

 
 