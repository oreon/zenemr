
from rest_framework import serializers
from .models import *

import sys

from django.db import transaction


     
     

     
     
    
class CodeLookupSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()

    class Meta:
        model = Code
        fields = ('displayName', 'id',)

class ChapterLookupSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()

    class Meta:
        model = Chapter
        fields = ('displayName', 'id',)

class SectionLookupSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()

    class Meta:
        model = Section
        fields = ('displayName', 'id',)

class SimpleCodeLookupSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()

    class Meta:
        model = SimpleCode
        fields = ('displayName', 'id',)
    
    
    
        
    
        
    
    

class CodeSerializer(serializers.ModelSerializer):
    displayName = serializers.ReadOnlyField()
    
    section = SectionLookupSerializer()
  
    
    class Meta:
        model = Code


    
    

class SectionSerializer(serializers.ModelSerializer):
    displayName = serializers.ReadOnlyField()
    
    chapter = ChapterLookupSerializer()
  
    codes = CodeSerializer(many=True, read_only = True)
    
    class Meta:
        model = Section


    
    

class ChapterSerializer(serializers.ModelSerializer):
    displayName = serializers.ReadOnlyField()
    
  
    sections = SectionSerializer(many=True, read_only = True)
    
    class Meta:
        model = Chapter


    
    

class SimpleCodeSerializer(serializers.ModelSerializer):
    displayName = serializers.ReadOnlyField()
    
  
    
    class Meta:
        model = SimpleCode


    
    
        
    
        
    
    
    
class CodeWritableSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()
    
    section_displayName = serializers.ReadOnlyField(source='sectionDisplayName')
    
    
    
    section = serializers.PrimaryKeyRelatedField(queryset=Section.objects.all())
    
    
    
    
    

    class Meta:
        model = Code
        exclude = ('section',)
    


    
    
    
class SectionWritableSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()
    
    chapter_displayName = serializers.ReadOnlyField(source='chapterDisplayName')
    
    
    
    chapter = serializers.PrimaryKeyRelatedField(queryset=Chapter.objects.all())
    
    
    
    codes = CodeWritableSerializer(many=True)
    
    
    
    
    @transaction.atomic
    def create(self, validated_data):
        try:
            
            codesCurrent = validated_data.pop('codes')   
            
            
            section = Section.objects.create(**validated_data)
            
            
            for item in codesCurrent:
                Code(section=section, **item).save()    
            
            return section
        except :
            e = sys.exc_info()[0]

    @transaction.atomic
    def update(self, instance, validated_data):
        try:
            
            self.updateCodes(instance, validated_data)    
            
            return super(SectionWritableSerializer, self).update( instance, validated_data)
        except :
            e = sys.exc_info()[0]
    
    
    def updateCodes(self, instance , validated_data):
        if not 'codes' in validated_data.keys() : return;
    
        codesCurrent = validated_data.pop('codes')
            
        ids = [item['id'] for item in codesCurrent  if 'id' in item.keys() ]
        
        for item in instance.codes.all() :
            if item.id not in ids: 
                item.delete()
        
        for item in codesCurrent:
            Code(section=instance, **item).save()  
     
     

    class Meta:
        model = Section
        exclude = ('chapter',)
    


    
    
    
class ChapterWritableSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()
    
    
    
    
    
    
    sections = SectionWritableSerializer(many=True)
    
    
    
    
    @transaction.atomic
    def create(self, validated_data):
        try:
            
            sectionsCurrent = validated_data.pop('sections')   
            
            
            chapter = Chapter.objects.create(**validated_data)
            
            
            for item in sectionsCurrent:
                Section(chapter=chapter, **item).save()    
            
            return chapter
        except :
            e = sys.exc_info()[0]

    @transaction.atomic
    def update(self, instance, validated_data):
        try:
            
            self.updateSections(instance, validated_data)    
            
            return super(ChapterWritableSerializer, self).update( instance, validated_data)
        except :
            e = sys.exc_info()[0]
    
    
    def updateSections(self, instance , validated_data):
        if not 'sections' in validated_data.keys() : return;
    
        sectionsCurrent = validated_data.pop('sections')
            
        ids = [item['id'] for item in sectionsCurrent  if 'id' in item.keys() ]
        
        for item in instance.sections.all() :
            if item.id not in ids: 
                item.delete()
        
        for item in sectionsCurrent:
            Section(chapter=instance, **item).save()  
     
     

    class Meta:
        model = Chapter
        
    


    
    
    
class SimpleCodeWritableSerializer(serializers.ModelSerializer):
    
    displayName = serializers.ReadOnlyField()
    
    
    
    
    
    
    
    

    class Meta:
        model = SimpleCode
        
    


    
class FullCodeSerializer(CodeSerializer):

 
    
    class Meta(CodeSerializer.Meta):
        model = Code

class FullChapterSerializer(ChapterSerializer):

 
    
    class Meta(ChapterSerializer.Meta):
        model = Chapter

class FullSectionSerializer(SectionSerializer):

 
    
    class Meta(SectionSerializer.Meta):
        model = Section

class FullSimpleCodeSerializer(SimpleCodeSerializer):

 
    
    class Meta(SimpleCodeSerializer.Meta):
        model = SimpleCode

    
  