
 
from django.contrib import admin

from . import models
from restbase.commons import CustomModelAdminMixin

 
class AppliedChartTests(BaseTest):
     
     url = 'appliedChart'
     
     fixtures = [' AppliedCharts.json','patients.json']
         
     def test_createAppliedChartByNotAllowed AppliedChart(self):
         self.login('alicia-rn')
         response = self.read_one_record(suffix='writable')
         data = response.data
         data['id'] = None
         response = self.client.post(self.url,data)
         print(response.data)
         ''' access should be denied'''
         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
         
     def test_createAppliedChart(self):
         self.login('alicia-rn')
         response = self.read_one_record(suffix='writable')
         data = response.data
         data['id'] = None
         response = self.client.post(self.url,data)
         print(response.data)
         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class ChartTests(BaseTest):
     
     url = 'chart'
     
     fixtures = [' Charts.json','patients.json']
         
     def test_createChartByNotAllowed Chart(self):
         self.login('alicia-rn')
         response = self.read_one_record(suffix='writable')
         data = response.data
         data['id'] = None
         response = self.client.post(self.url,data)
         print(response.data)
         ''' access should be denied'''
         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
         
     def test_createChart(self):
         self.login('alicia-rn')
         response = self.read_one_record(suffix='writable')
         data = response.data
         data['id'] = None
         response = self.client.post(self.url,data)
         print(response.data)
         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class ChartItemTests(BaseTest):
     
     url = 'chartItem'
     
     fixtures = [' ChartItems.json','patients.json']
         
     def test_createChartItemByNotAllowed ChartItem(self):
         self.login('alicia-rn')
         response = self.read_one_record(suffix='writable')
         data = response.data
         data['id'] = None
         response = self.client.post(self.url,data)
         print(response.data)
         ''' access should be denied'''
         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
         
     def test_createChartItem(self):
         self.login('alicia-rn')
         response = self.read_one_record(suffix='writable')
         data = response.data
         data['id'] = None
         response = self.client.post(self.url,data)
         print(response.data)
         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class ChartProcedureTests(BaseTest):
     
     url = 'chartProcedure'
     
     fixtures = [' ChartProcedures.json','patients.json']
         
     def test_createChartProcedureByNotAllowed ChartProcedure(self):
         self.login('alicia-rn')
         response = self.read_one_record(suffix='writable')
         data = response.data
         data['id'] = None
         response = self.client.post(self.url,data)
         print(response.data)
         ''' access should be denied'''
         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
         
     def test_createChartProcedure(self):
         self.login('alicia-rn')
         response = self.read_one_record(suffix='writable')
         data = response.data
         data['id'] = None
         response = self.client.post(self.url,data)
         print(response.data)
         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

 
 