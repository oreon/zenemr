
from rest_framework import serializers
from .models import *

import sys

from django.db import transaction

from  patients.serializers import  PatientLookupSerializer
     
     


     
    
class InvoiceLookupSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()

    class Meta:
        model = Invoice
        fields = ('displayName', 'id',)

class ServiceLookupSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()

    class Meta:
        model = Service
        fields = ('displayName', 'id',)

class InvoiceItemLookupSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()

    class Meta:
        model = InvoiceItem
        fields = ('displayName', 'id',)
    
    
    
        
    
    

class InvoiceItemSerializer(serializers.ModelSerializer):
    displayName = serializers.ReadOnlyField()
    
    service = ServiceLookupSerializer()
    invoice = InvoiceLookupSerializer()
  
    
    class Meta:
        model = InvoiceItem


    
    

class InvoiceSerializer(serializers.ModelSerializer):
    displayName = serializers.ReadOnlyField()
    
    patient = PatientLookupSerializer()
  
    invoiceItems = InvoiceItemSerializer(many=True, read_only = True)
    
    class Meta:
        model = Invoice


    
    

class ServiceSerializer(serializers.ModelSerializer):
    displayName = serializers.ReadOnlyField()
    
  
    
    class Meta:
        model = Service


    
    
        
    
    
    
class InvoiceItemWritableSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()
    
    service_displayName = serializers.ReadOnlyField(source='serviceDisplayName')
    invoice_displayName = serializers.ReadOnlyField(source='invoiceDisplayName')
    
    
    
    invoice = serializers.PrimaryKeyRelatedField(queryset=Invoice.objects.all())
    
    
    
    
    

    class Meta:
        model = InvoiceItem
        exclude = ('invoice',)
    


    
    
    
class InvoiceWritableSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()
    
    patient_displayName = serializers.ReadOnlyField(source='patientDisplayName')
    
    
    
    
    
    invoiceItems = InvoiceItemWritableSerializer(many=True)
    
    
    
    
    @transaction.atomic
    def create(self, validated_data):
        try:
            
            invoiceItemsCurrent = validated_data.pop('invoiceItems')   
            
            
            invoice = Invoice.objects.create(**validated_data)
            
            
            for item in invoiceItemsCurrent:
                InvoiceItem(invoice=invoice, **item).save()    
            
            return invoice
        except :
            e = sys.exc_info()[0]

    @transaction.atomic
    def update(self, instance, validated_data):
        try:
            
            self.updateInvoiceItems(instance, validated_data)    
            
            return super(InvoiceWritableSerializer, self).update( instance, validated_data)
        except :
            e = sys.exc_info()[0]
    
    
    def updateInvoiceItems(self, instance , validated_data):
        if not 'invoiceItems' in validated_data.keys() : return;
    
        invoiceItemsCurrent = validated_data.pop('invoiceItems')
            
        ids = [item['id'] for item in invoiceItemsCurrent  if 'id' in item.keys() ]
        
        for item in instance.invoiceItems.all() :
            if item.id not in ids: 
                item.delete()
        
        for item in invoiceItemsCurrent:
            InvoiceItem(invoice=instance, **item).save()  
     
     

    class Meta:
        model = Invoice
        
    


    
    
    
class ServiceWritableSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()
    
    
    
    
    
    
    
    

    class Meta:
        model = Service
        
    


    
class FullInvoiceSerializer(InvoiceSerializer):

 
    
    class Meta(InvoiceSerializer.Meta):
        model = Invoice

class FullServiceSerializer(ServiceSerializer):

 
    
    class Meta(ServiceSerializer.Meta):
        model = Service

class FullInvoiceItemSerializer(InvoiceItemSerializer):

 
    
    class Meta(InvoiceItemSerializer.Meta):
        model = InvoiceItem

    
  