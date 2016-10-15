
from rest_framework import serializers
from .models import *

import sys

from django.db import transaction


     
from  ddx.serializers import  ChronicConditionLookupSerializer
     

     

     
    
class AppliedChartLookupSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()

    class Meta:
        model = AppliedChart
        fields = ('displayName', 'id',)

class ChartLookupSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()

    class Meta:
        model = Chart
        fields = ('displayName', 'id',)

class ChartItemLookupSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()

    class Meta:
        model = ChartItem
        fields = ('displayName', 'id',)

class ChartProcedureLookupSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()

    class Meta:
        model = ChartProcedure
        fields = ('displayName', 'id',)
    
    
    
    

class AppliedChartSerializer(serializers.ModelSerializer):
    displayName = serializers.ReadOnlyField()
    
    chart = ChartLookupSerializer()
  
    
    class Meta:
        model = AppliedChart


    
        
    
    

class ChartItemSerializer(serializers.ModelSerializer):
    displayName = serializers.ReadOnlyField()
    
    chart = ChartLookupSerializer()
  
    
    class Meta:
        model = ChartItem


    
    

class ChartSerializer(serializers.ModelSerializer):
    displayName = serializers.ReadOnlyField()
    
    chronicCondition = ChronicConditionLookupSerializer()
  
    chartItems = ChartItemSerializer(many=True, read_only = True)
    
    class Meta:
        model = Chart


    
    

class ChartProcedureSerializer(serializers.ModelSerializer):
    displayName = serializers.ReadOnlyField()
    
    chartItem = ChartItemLookupSerializer()
  
    
    class Meta:
        model = ChartProcedure


    
    
    
    
class AppliedChartWritableSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()
    
    chart_displayName = serializers.ReadOnlyField(source='chartDisplayName')
    
    
    
    
    
    
    

    class Meta:
        model = AppliedChart
        
    


    
        
    
    
    
class ChartItemWritableSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()
    
    chart_displayName = serializers.ReadOnlyField(source='chartDisplayName')
    
    
    
    chart = serializers.PrimaryKeyRelatedField(queryset=Chart.objects.all())
    
    
    
    
    

    class Meta:
        model = ChartItem
        exclude = ('chart',)
    


    
    
    
class ChartWritableSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()
    
    chronicCondition_displayName = serializers.ReadOnlyField(source='chronicConditionDisplayName')
    
    
    
    
    
    chartItems = ChartItemWritableSerializer(many=True)
    
    
    
    
    @transaction.atomic
    def create(self, validated_data):
        try:
            
            chartItemsCurrent = validated_data.pop('chartItems')   
            
            
            chart = Chart.objects.create(**validated_data)
            
            
            for item in chartItemsCurrent:
                ChartItem(chart=chart, **item).save()    
            
            return chart
        except :
            e = sys.exc_info()[0]

    @transaction.atomic
    def update(self, instance, validated_data):
        try:
            
            self.updateChartItems(instance, validated_data)    
            
            return super(ChartWritableSerializer, self).update( instance, validated_data)
        except :
            e = sys.exc_info()[0]
    
    
    def updateChartItems(self, instance , validated_data):
        if not 'chartItems' in validated_data.keys() : return;
    
        chartItemsCurrent = validated_data.pop('chartItems')
            
        ids = [item['id'] for item in chartItemsCurrent  if 'id' in item.keys() ]
        
        for item in instance.chartItems.all() :
            if item.id not in ids: 
                item.delete()
        
        for item in chartItemsCurrent:
            ChartItem(chart=instance, **item).save()  
     
     

    class Meta:
        model = Chart
        
    


    
    
    
class ChartProcedureWritableSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()
    
    chartItem_displayName = serializers.ReadOnlyField(source='chartItemDisplayName')
    
    
    
    
    
    
    

    class Meta:
        model = ChartProcedure
        
    


    
class FullAppliedChartSerializer(AppliedChartSerializer):

 
    
    class Meta(AppliedChartSerializer.Meta):
        model = AppliedChart

class FullChartSerializer(ChartSerializer):

 
    
    class Meta(ChartSerializer.Meta):
        model = Chart

class FullChartItemSerializer(ChartItemSerializer):

 
    
    class Meta(ChartItemSerializer.Meta):
        model = ChartItem

class FullChartProcedureSerializer(ChartProcedureSerializer):

 
    
    class Meta(ChartProcedureSerializer.Meta):
        model = ChartProcedure

    
  