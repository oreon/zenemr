
from django.db import models

    
EmployeeType = (
    ('0', 'BRONZE'),
    ('1', 'SILVER'),
    ('2', 'GOLD'),
  
)

Title = (
    ('0', 'Mr'),
    ('1', 'Mrs'),
    ('2', 'Ms'),
    ('3', 'Dr'),
  
)

AllergySeverity = (
    ('0', 'SEVERE'),
    ('1', 'MODERATE'),
    ('2', 'MILD'),
  
)

Route = (
    ('0', 'PO'),
    ('1', 'IV'),
    ('2', 'IM'),
    ('3', 'SC'),
    ('4', 'TOPICAL'),
  
)

Gender = (
    ('0', 'F'),
    ('1', 'M'),
  
)

TreatmentCategory = (
    ('0', 'Radiation'),
    ('1', 'Chemotherapy'),
    ('2', 'Anesthesia'),
    ('3', 'Surgery'),
    ('4', 'Other'),
  
)

Severity = (
    ('0', 'Mild'),
    ('1', 'Moderate'),
    ('2', 'Critical'),
  
)

Route = (
    ('0', 'PO'),
    ('1', 'IV'),
    ('2', 'IM'),
    ('3', 'SC'),
    ('4', 'TOPICAL'),
  
)

InteractionSeverity = (
    ('0', 'MILD'),
    ('1', 'MODERATE'),
    ('2', 'SEVERE'),
  
)

LabFindingType = (
    ('0', 'ELEVATED'),
    ('1', 'DECREASED'),
    ('2', 'NEGATIVE'),
    ('3', 'POSITIVE'),
    ('4', 'FALSE_POSITIVE'),
  
)

TimeEnumeration = (
    ('0', 'HOUR'),
    ('1', 'DAY'),
    ('2', 'WEEK'),
    ('3', 'MONTH'),
    ('4', 'YEAR'),
  
)

DischargeCode = (
    ('0', 'Deceased'),
    ('1', 'Referred'),
    ('2', 'Normal'),
  
)

    
  

class PersonBase(models.Model): 

    firstName = models.CharField(null = False, blank =  False, max_length=30)
    
    lastName = models.CharField(null = False, blank =  False, max_length=30)
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    
    
    def __str__(self):
        return ''.join([self.firstName , ', ', self.lastName]) 
        
    class Meta:
        abstract = True
        
    
      
        

    
 

class AppUserBase(models.Model): 

    userName = models.CharField(null = False, blank =  True, max_length=30)
    
    password = models.CharField(null = False, blank =  True, max_length=30)
    
    enabled = models.NullBooleanField(null = False, blank =  True, )
    
    groups =    models.ManyToManyField("users.Group",  blank=True,   null = True,  related_name="groups")
            
        
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    
    
    def __str__(self):
        return self.userName 
        
    class Meta:
        abstract = True
        
    
      
        


 

class AppRoleBase(models.Model): 

    name = models.CharField(null = False, blank =  False, max_length=30)
    
    groups =    models.ManyToManyField("users.Group",  blank=True,   null = True,  related_name="groups")
            
        
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    
    
    def __str__(self):
        return self.name 
        
    class Meta:
        abstract = True
        
    
      
        


 

class GroupBase(models.Model): 

    appUsers =    models.ManyToManyField("users.AppUser",  blank=True,   null = True,  related_name="appUsers")
            
        
    
    appRoles =    models.ManyToManyField("users.AppRole",  blank=True,   null = True,  related_name="appRoles")
            
        
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    
    
    def __str__(self):
        return self.appUsers+ "" 
        
    class Meta:
        abstract = True
        
    
      
        


 

class PatientBase(PersonBase): 

    customerType = models.CharField(null = False, blank =  True, max_length = 1 , choices = EmployeeType)
    
            
        
    
            
        
    
            
        
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    
    
    def __str__(self):
        return super().__str__() 
        
    class Meta:
        abstract = True
        
    
      
        


 

class VaccinationBase(models.Model): 

    review = models.TextField(null = False, blank =  True, )
    
    rating = models.PositiveIntegerField(null = False, blank =  True, )
    
    vaccine = models.ForeignKey('patients.Vaccine', related_name='vaccination')
        
    
    patient = models.ForeignKey('patients.Patient', related_name='vaccination')
        
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    @property   
    def vaccineDisplayName(self):
        return self.vaccine.__str__()
    @property   
    def patientDisplayName(self):
        return self.patient.__str__()
    
    
    def __str__(self):
        return self.review 
        
    class Meta:
        abstract = True
        
    
      
        


 

class EncounterBase(models.Model): 

    reason = models.TextField(null = False, blank =  True, )
    
    patient = models.ForeignKey('patients.Patient', related_name='encounter')
        
    
    labTests =    models.ManyToManyField("patients.LabTest",  blank=True,   null = True,  related_name="labTests")
            
        
    
        
    prescription =    models.OneToOneField("prescription.Prescription",  null = True,blank=True,  related_name="prescription")
        
    
    admission = models.ForeignKey('admission.Admission', related_name='encounter')
        
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    @property   
    def patientDisplayName(self):
        return self.patient.__str__()
    @property   
    def prescriptionDisplayName(self):
        return self.prescription.__str__()
    @property   
    def admissionDisplayName(self):
        return self.admission.__str__()
    
    
    def __str__(self):
        return self.reason 
        
    class Meta:
        abstract = True
        
    
      
        


 

class VaccineBase(models.Model): 

    name = models.CharField(null = False, blank =  False, max_length=30)
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    
    
    def __str__(self):
        return self.name 
        
    class Meta:
        abstract = True
        
    
      
        


 

class LabTestBase(models.Model): 

    name = models.CharField(null = False, blank =  False, max_length=30)
    
    encounters =    models.ManyToManyField("patients.Encounter",  blank=True,   null = True,  related_name="encounters")
            
        
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    
    
    def __str__(self):
        return self.name 
        
    class Meta:
        abstract = True
        
    
      
        


 

class TestResultsBase(models.Model): 

    patient = models.ForeignKey('patients.Patient', related_name='testResults')
        
    
            
        
    
    labTest = models.ForeignKey('patients.LabTest', related_name='testResults')
        
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    @property   
    def patientDisplayName(self):
        return self.patient.__str__()
    @property   
    def labTestDisplayName(self):
        return self.labTest.__str__()
    
    
    def __str__(self):
        return self.patient+ "" 
        
    class Meta:
        abstract = True
        
    
      
        


 

class ResultRowBase(models.Model): 

    testResults = models.ForeignKey('patients.TestResults', related_name='resultRows')
        
    
    name = models.CharField(null = False, blank =  False, max_length=30)
    
    value = models.CharField(null = False, blank =  True, )
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    @property   
    def testResultsDisplayName(self):
        return self.testResults.__str__()
    
    
    def __str__(self):
        return self.name 
        
    class Meta:
        abstract = True
        
    
      
        


 

class FacilityBase(models.Model): 

    name = models.CharField(null = False, blank =  True, max_length=30)
    
            
        
    
    isResidential = models.NullBooleanField(null = False, blank =  True, )
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    
    
    def __str__(self):
        return self.name 
        
    class Meta:
        abstract = True
        
    
      
        


 

class RoomBase(models.Model): 

            
        
    
    name = models.CharField(null = False, blank =  False, max_length=30)
    
    roomType = models.ForeignKey('facility.RoomType', related_name='room')
        
    
    ward = models.ForeignKey('facility.Ward', related_name='rooms')
        
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    @property   
    def roomTypeDisplayName(self):
        return self.roomType.__str__()
    @property   
    def wardDisplayName(self):
        return self.ward.__str__()
    
    
    def __str__(self):
        return self.name 
        
    class Meta:
        abstract = True
        
    
      
        


 

class BedBase(models.Model): 

    room = models.ForeignKey('facility.Room', related_name='beds')
        
    
    name = models.CharField(null = False, blank =  False, max_length=30)
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    @property   
    def roomDisplayName(self):
        return self.room.__str__()
    
    
    def __str__(self):
        return room.getName() + " " + name 
        
    class Meta:
        abstract = True
        
    
      
        


 

class WardBase(models.Model): 

    facility = models.ForeignKey('facility.Facility', related_name='wards')
        
    
            
        
    
    name = models.CharField(null = False, blank =  False, max_length=30)
    
    gender = models.CharField(null = False, blank =  True, max_length = 1 , choices = Gender)
    
    maxAge = models.PositiveIntegerField(null = False, blank =  True, )
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    @property   
    def facilityDisplayName(self):
        return self.facility.__str__()
    
    
    def __str__(self):
        return self.name 
        
    class Meta:
        abstract = True
        
    
      
        


 

class RoomTypeBase(models.Model): 

    name = models.CharField(null = False, blank =  False, max_length=30)
    
    description = models.TextField(null = False, blank =  True, )
    
    rate = models.CharField(null = False, blank =  True, )
    
    numberOfBeds = models.PositiveIntegerField(null = False, blank =  True, )
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    
    
    def __str__(self):
        return self.name 
        
    class Meta:
        abstract = True
        
    
      
        


 

class UnusualOccurenceBase(models.Model): 

    occurenceType = models.ForeignKey('unusualoccurences.OccurenceType', related_name='unusualOccurence')
        
    
    category = models.CharField(null = False, blank =  True, max_length = 1 , choices = TreatmentCategory)
    
    severity = models.CharField(null = False, blank =  True, max_length = 1 , choices = Severity)
    
    description = models.TextField(null = False, blank =  True, )
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    @property   
    def occurenceTypeDisplayName(self):
        return self.occurenceType.__str__()
    
    
    def __str__(self):
        return self.description 
        
    class Meta:
        abstract = True
        
    
      
        


 

class OccurenceTypeBase(models.Model): 

    name = models.CharField(null = False, blank =  False, max_length=30)
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    
    
    def __str__(self):
        return self.name 
        
    class Meta:
        abstract = True
        
    
      
        


 

class SettingsBase(models.Model): 

 
    @property   
    def displayName(self):
        return self.__str__()
        
    
    
    def __str__(self):
        return self.Empty class - no display name possible 
        
    class Meta:
        abstract = True
        
    
      
        


 

class SettingBase(models.Model): 

    value = models.CharField(null = False, blank =  False, max_length=30)
    
    settingName = models.ForeignKey('settings.SettingName', related_name='setting')
        
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    @property   
    def settingNameDisplayName(self):
        return self.settingName.__str__()
    
    
    def __str__(self):
        return self.value 
        
    class Meta:
        abstract = True
        
    
      
        


 

class SettingNameBase(models.Model): 

    name = models.CharField(null = False, blank =  False, max_length=30)
    
    settingGroup = models.ForeignKey('settings.SettingGroup', related_name='settingNames')
        
    
    defaultValue = models.CharField(null = False, blank =  False, max_length=30)
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    @property   
    def settingGroupDisplayName(self):
        return self.settingGroup.__str__()
    
    
    def __str__(self):
        return self.name 
        
    class Meta:
        abstract = True
        
    
      
        


 

class SettingGroupBase(models.Model): 

    name = models.CharField(null = False, blank =  False, max_length=30)
    
            
        
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    
    
    def __str__(self):
        return self.name 
        
    class Meta:
        abstract = True
        
    
      
        


 

class PrescriptionTemplateBase(models.Model): 

    name = models.CharField(null = False, blank =  False, max_length=30)
    
    directivesForPatient = models.TextField(null = False, blank =  True, )
    
            
        
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    
    
    def __str__(self):
        return self.name 
        
    class Meta:
        abstract = True
        
    
      
        


 

class PrescriptionBase(models.Model): 

            
        
    
    active = models.NullBooleanField(null = False, blank =  True, )
    
    directivesForPatient = models.TextField(null = False, blank =  True, )
    
    drugs = models.CharField(null = False, blank =  True, max_length=30)
    
    startDate = models.DateField(null = False, blank =  True, )
    
    endDate = models.DateField(null = False, blank =  True, )
    
        
    encounter =    models.OneToOneField("patients.Encounter",  null =  False,blank=True,  related_name="encounter")
        
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    @property   
    def encounterDisplayName(self):
        return self.encounter.__str__()
    
    
    def __str__(self):
        return drugs 
        
    class Meta:
        abstract = True
        
    
      
        


 

class PrescriptionItemBase(models.Model): 

    drug = models.ForeignKey('drugs.Drug', related_name='prescriptionItem')
        
    
    qty = models.CharField(null = False, blank =  True, )
    
    strength = models.CharField(null = False, blank =  True, max_length=30)
    
    prescription = models.ForeignKey('prescription.Prescription', related_name='prescriptionItems')
        
    
    route = models.CharField(null = False, blank =  True, max_length = 1 , choices = Route)
    
    duration = models.PositiveIntegerField(null = False, blank =  True, )
    
    frequency = models.ForeignKey('prescription.Frequency', related_name='prescriptionItem')
        
    
    remarks = models.CharField(null = False, blank =  True, max_length=30)
    
    brandName = models.CharField(null = False, blank =  True, max_length=30)
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    @property   
    def drugDisplayName(self):
        return self.drug.__str__()
    @property   
    def prescriptionDisplayName(self):
        return self.prescription.__str__()
    @property   
    def frequencyDisplayName(self):
        return self.frequency.__str__()
    
    
    def __str__(self):
        return self.strength 
        
    class Meta:
        abstract = True
        
    
      
        


 

class PrescriptionItemTemplateBase(models.Model): 

    drug = models.ForeignKey('drugs.Drug', related_name='prescriptionItemTemplate')
        
    
    qty = models.CharField(null = False, blank =  True, )
    
    frequency = models.ForeignKey('prescription.Frequency', related_name='prescriptionItemTemplate')
        
    
    strength = models.CharField(null = False, blank =  True, max_length=30)
    
    route = models.CharField(null = False, blank =  True, max_length = 1 , choices = Route)
    
    duration = models.PositiveIntegerField(null = False, blank =  True, )
    
    remarks = models.CharField(null = False, blank =  True, max_length=30)
    
    brandName = models.CharField(null = False, blank =  True, max_length=30)
    
    prescriptionTemplate = models.ForeignKey('prescription.PrescriptionTemplate', related_name='prescriptionItemTemplates')
        
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    @property   
    def drugDisplayName(self):
        return self.drug.__str__()
    @property   
    def frequencyDisplayName(self):
        return self.frequency.__str__()
    @property   
    def prescriptionTemplateDisplayName(self):
        return self.prescriptionTemplate.__str__()
    
    
    def __str__(self):
        return self.strength 
        
    class Meta:
        abstract = True
        
    
      
        


 

class FrequencyBase(models.Model): 

    name = models.CharField(null = False, blank =  False, max_length=30)
    
    qtyPerDay = models.PositiveIntegerField(null = False, blank =  True, )
    
    remarkts = models.TextField(null = False, blank =  True, )
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    
    
    def __str__(self):
        return self.name 
        
    class Meta:
        abstract = True
        
    
      
        


 

class AtcDrugBase(models.Model): 

    code = models.CharField(null = False, blank =  True, max_length=30)
    
    name = models.CharField(null = False, blank =  False, max_length=30)
    
            
        
    
    drug = models.ForeignKey('drugs.Drug', related_name='atcDrug')
        
    
    parent = models.ForeignKey('drugs.AtcDrug', related_name='subcategories')
        
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    @property   
    def drugDisplayName(self):
        return self.drug.__str__()
    @property   
    def parentDisplayName(self):
        return self.parent.__str__()
    
    
    def __str__(self):
        return self.name 
        
    class Meta:
        abstract = True
        
    
      
        


 

class DrugBase(models.Model): 

    name = models.CharField(null = False, blank =  False, max_length=30)
    
    absorption = models.TextField(null = False, blank =  True, )
    
    biotransformation = models.TextField(null = False, blank =  True, )
    
    atcCodes = models.CharField(null = False, blank =  True, max_length=30)
    
    contraIndication = models.TextField(null = False, blank =  True, )
    
    description = models.TextField(null = False, blank =  True, )
    
    dosageForm = models.CharField(null = False, blank =  True, max_length=30)
    
    foodInteractions = models.TextField(null = False, blank =  True, )
    
    halfLife = models.TextField(null = False, blank =  True, )
    
    indication = models.TextField(null = False, blank =  True, )
    
    halfLifeNumberOfHours = models.CharField(null = False, blank =  True, )
    
    mechanismOfAction = models.TextField(null = False, blank =  True, )
    
    patientInfo = models.TextField(null = False, blank =  True, )
    
    pharmacology = models.TextField(null = False, blank =  True, )
    
            
        
    
    drugCategorys =    models.ManyToManyField("drugs.DrugCategory",  blank=True,   null = True,  related_name="drugCategorys")
            
        
    
    toxicity = models.TextField(null = False, blank =  True, )
    
    routeOfElimination = models.TextField(null = False, blank =  True, )
    
    volumeOfDistribution = models.CharField(null = False, blank =  True, max_length=30)
    
    drugBankId = models.CharField(null = False, blank =  True, max_length=30)
    
    categories = models.CharField(null = False, blank =  True, max_length=30)
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    
    
    def __str__(self):
        return self.name 
        
    class Meta:
        abstract = True
        
    
      
        


 

class DrugInteractionBase(models.Model): 

    description = models.TextField(null = False, blank =  True, )
    
    drug = models.ForeignKey('drugs.Drug', related_name='drugInteractions')
        
    
    interactingDrug = models.ForeignKey('drugs.Drug', related_name='drugInteraction')
        
    
    severity = models.CharField(null = False, blank =  True, max_length = 1 , choices = InteractionSeverity)
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    @property   
    def drugDisplayName(self):
        return self.drug.__str__()
    @property   
    def interactingDrugDisplayName(self):
        return self.interactingDrug.__str__()
    
    
    def __str__(self):
        return self.description 
        
    class Meta:
        abstract = True
        
    
      
        


 

class DrugCategoryBase(models.Model): 

    name = models.CharField(null = False, blank =  False, max_length=30)
    
    drugs =    models.ManyToManyField("drugs.Drug",  blank=True,   null = True,  related_name="drugs")
            
        
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    
    
    def __str__(self):
        return self.name 
        
    class Meta:
        abstract = True
        
    
      
        


 

class FindingBase(models.Model): 

    name = models.CharField(null = False, blank =  False, max_length=30)
    
            
        
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    
    
    def __str__(self):
        return self.name 
        
    class Meta:
        abstract = True
        
    
      
        


 

class PhysicalFindingBase(FindingBase): 

    icdCode = models.CharField(null = False, blank =  True, max_length=30)
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    
    
    def __str__(self):
        return name 
        
    class Meta:
        abstract = True
        
    
      
        


 

class LabFindingBase(FindingBase): 

    testName = models.CharField(null = False, blank =  False, max_length=30)
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    
    
    def __str__(self):
        return name 
        
    class Meta:
        abstract = True
        
    
      
        


 

class DiseaseBase(models.Model): 

    gender = models.CharField(null = False, blank =  True, max_length = 1 , choices = Gender)
    
    name = models.CharField(null = False, blank =  False, max_length=30)
    
            
        
    
    relatedDisease = models.ForeignKey('ddx.Disease', related_name='differentialDiagnoses')
        
    
    conditionCategory = models.ForeignKey('ddx.ConditionCategory', related_name='disease')
        
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    @property   
    def relatedDiseaseDisplayName(self):
        return self.relatedDisease.__str__()
    @property   
    def conditionCategoryDisplayName(self):
        return self.conditionCategory.__str__()
    
    
    def __str__(self):
        return self.name 
        
    class Meta:
        abstract = True
        
    
      
        


 

class ConditionFindingBase(models.Model): 

    disease = models.ForeignKey('ddx.Disease', related_name='conditionFinding')
        
    
    falsePositive = models.NullBooleanField(null = False, blank =  True, )
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    @property   
    def diseaseDisplayName(self):
        return self.disease.__str__()
    
    
    def __str__(self):
        return self.disease+ "" 
        
    class Meta:
        abstract = True
        
    
      
        


 

class ConditionCategoryBase(models.Model): 

    name = models.CharField(null = False, blank =  False, max_length=30)
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    
    
    def __str__(self):
        return self.name 
        
    class Meta:
        abstract = True
        
    
      
        


 

class DifferentialDxBase(models.Model): 

    name = models.CharField(null = False, blank =  False, max_length=30)
    
    dxCategory = models.ForeignKey('ddx.DxCategory', related_name='differentialDx')
        
    
    finding = models.ForeignKey('ddx.Finding', related_name='differentialDxs')
        
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    @property   
    def dxCategoryDisplayName(self):
        return self.dxCategory.__str__()
    @property   
    def findingDisplayName(self):
        return self.finding.__str__()
    
    
    def __str__(self):
        return self.name 
        
    class Meta:
        abstract = True
        
    
      
        


 

class DxCategoryBase(models.Model): 

    name = models.CharField(null = False, blank =  False, max_length=30)
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    
    
    def __str__(self):
        return self.name 
        
    class Meta:
        abstract = True
        
    
      
        


 

class PatientFindingBase(models.Model): 

    finding = models.ForeignKey('ddx.Finding', related_name='patientFinding')
        
    
    patientDiffDx = models.ForeignKey('ddx.PatientDiffDx', related_name='patientFindings')
        
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    @property   
    def findingDisplayName(self):
        return self.finding.__str__()
    @property   
    def patientDiffDxDisplayName(self):
        return self.patientDiffDx.__str__()
    
    
    def __str__(self):
        return self.finding+ "" 
        
    class Meta:
        abstract = True
        
    
      
        


 

class PatientDiffDxBase(models.Model): 

            
        
    
    notes = models.TextField(null = False, blank =  True, )
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    
    
    def __str__(self):
        return self.notes 
        
    class Meta:
        abstract = True
        
    
      
        


 

class DxTestBase(models.Model): 

    name = models.CharField(null = False, blank =  False, max_length=30)
    
    description = models.TextField(null = False, blank =  True, )
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    
    
    def __str__(self):
        return self.name 
        
    class Meta:
        abstract = True
        
    
      
        


 

class ChronicConditionBase(models.Model): 

    name = models.CharField(null = False, blank =  True, max_length=30)
    
            
        
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    
    
    def __str__(self):
        return self.name 
        
    class Meta:
        abstract = True
        
    
      
        


 

class CodeBase(AbstractCodeBase): 

    includes = models.TextField(null = False, blank =  True, )
    
    notIncludedHere = models.TextField(null = False, blank =  True, )
    
    codeFirst = models.TextField(null = False, blank =  True, )
    
    section = models.ForeignKey('codes.Section', related_name='codes')
        
    
    notCodedHere = models.TextField(null = False, blank =  True, )
    
    codeAlso = models.TextField(null = False, blank =  True, )
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    @property   
    def sectionDisplayName(self):
        return self.section.__str__()
    
    
    def __str__(self):
        return super().__str__() 
        
    class Meta:
        abstract = True
        
    
      
        


 

class ChapterBase(AbstractCodeBase): 

            
        
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    
    
    def __str__(self):
        return super().__str__() 
        
    class Meta:
        abstract = True
        
    
      
        


 

class SectionBase(AbstractCodeBase): 

    chapter = models.ForeignKey('codes.Chapter', related_name='sections')
        
    
            
        
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    @property   
    def chapterDisplayName(self):
        return self.chapter.__str__()
    
    
    def __str__(self):
        return super().__str__() 
        
    class Meta:
        abstract = True
        
    
      
        


 

class AbstractCodeBase(models.Model): 

    name = models.CharField(null = False, blank =  False, max_length=30)
    
    description = models.TextField(null = False, blank =  True, )
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    
    
    def __str__(self):
        return name 
        
    class Meta:
        abstract = True
        
    
      
        


 

class SimpleCodeBase(models.Model): 

    name = models.CharField(null = False, blank =  False, max_length=30)
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    
    
    def __str__(self):
        return self.name 
        
    class Meta:
        abstract = True
        
    
      
        


 

class AppliedChartBase(models.Model): 

    chart = models.ForeignKey('charts.Chart', related_name='appliedChart')
        
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    @property   
    def chartDisplayName(self):
        return self.chart.__str__()
    
    
    def __str__(self):
        return self.chart+ "" 
        
    class Meta:
        abstract = True
        
    
      
        


 

class ChartBase(models.Model): 

            
        
    
    name = models.CharField(null = False, blank =  False, max_length=30)
    
    chronicCondition = models.ForeignKey('ddx.ChronicCondition', related_name='charts')
        
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    @property   
    def chronicConditionDisplayName(self):
        return self.chronicCondition.__str__()
    
    
    def __str__(self):
        return self.name 
        
    class Meta:
        abstract = True
        
    
      
        


 

class ChartItemBase(models.Model): 

    name = models.CharField(null = False, blank =  False, max_length=30)
    
    duration = models.PositiveIntegerField(null = False, blank =  True, )
    
    chart = models.ForeignKey('charts.Chart', related_name='chartItems')
        
    
    frequencyPeriod = models.CharField(null = False, blank =  True, max_length = 1 , choices = TimeEnumeration)
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    @property   
    def chartDisplayName(self):
        return self.chart.__str__()
    
    
    def __str__(self):
        return self.name 
        
    class Meta:
        abstract = True
        
    
      
        


 

class ChartProcedureBase(models.Model): 

    chartItem = models.ForeignKey('charts.ChartItem', related_name='chartProcedure')
        
    
    dueDate = models.DateField(null = False, blank =  True, )
    
    datePerformed = models.DateField(null = False, blank =  True, )
    
    remarks = models.TextField(null = False, blank =  True, )
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    @property   
    def chartItemDisplayName(self):
        return self.chartItem.__str__()
    
    
    def __str__(self):
        return self.remarks 
        
    class Meta:
        abstract = True
        
    
      
        


 

class InvoiceBase(models.Model): 

            
        
    
    notes = models.CharField(null = False, blank =  True, max_length=30)
    
    totalAmount = models.DecimalField(null = False, blank =  True, decimal_places=2, max_digits=9 )
    
    paidAmount = models.DecimalField(null = False, blank =  True, decimal_places=2, max_digits=9 )
    
    patient = models.ForeignKey('patients.Patient', related_name='invoice')
        
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    @property   
    def patientDisplayName(self):
        return self.patient.__str__()
    
    
    def __str__(self):
        return self.notes 
        
    class Meta:
        abstract = True
        
    
      
        


 

class ServiceBase(models.Model): 

    name = models.CharField(null = False, blank =  False, max_length=30)
    
    price = models.DecimalField(null = False, blank =  True, decimal_places=2, max_digits=9 )
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    
    
    def __str__(self):
        return self.name 
        
    class Meta:
        abstract = True
        
    
      
        


 

class InvoiceItemBase(models.Model): 

    units = models.PositiveIntegerField(null = False, blank =  True, )
    
    service = models.ForeignKey('billing.Service', related_name='invoiceItem')
        
    
    invoice = models.ForeignKey('billing.Invoice', related_name='invoiceItems')
        
    
    appliedPrice = models.DecimalField(null = False, blank =  True, decimal_places=2, max_digits=9 )
    
    total = models.DecimalField(null = False, blank =  True, decimal_places=2, max_digits=9 )
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    @property   
    def serviceDisplayName(self):
        return self.service.__str__()
    @property   
    def invoiceDisplayName(self):
        return self.invoice.__str__()
    
    
    def __str__(self):
        return self.units+ "" 
        
    class Meta:
        abstract = True
        
    
      
        


 

class AppointmentBase(models.Model): 

    start = models.DateTimeField(null = False, blank =  True, )
    
    end = models.DateTimeField(null = False, blank =  True, )
    
    remarks = models.TextField(null = False, blank =  True, )
    
    units = models.PositiveIntegerField(null = False, blank =  True, )
    
    patient = models.ForeignKey('patients.Patient', related_name='appointment')
        
    
    employee = models.ForeignKey('employees.Employee', related_name='appointment')
        
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    @property   
    def patientDisplayName(self):
        return self.patient.__str__()
    @property   
    def employeeDisplayName(self):
        return self.employee.__str__()
    
    
    def __str__(self):
        return self.remarks 
        
    class Meta:
        abstract = True
        
    
      
        


 

class AdmissionBase(models.Model): 

    admissionNote = models.TextField(null = False, blank =  True, )
    
    dischargeDate = models.DateField(null = False, blank =  True, )
    
    dischargeNote = models.TextField(null = False, blank =  True, )
    
    dischargeCode = models.CharField(null = False, blank =  True, max_length = 1 , choices = DischargeCode)
    
    currentBed = models.CharField(null = False, blank =  True, max_length=30)
    
    isCurrent = models.NullBooleanField(null = False, blank =  True, )
    
    invoice = models.ForeignKey('billing.Invoice', related_name='admission')
        
    
            
        
    
            
        
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    @property   
    def invoiceDisplayName(self):
        return self.invoice.__str__()
    
    
    def __str__(self):
        return self.admissionNote 
        
    class Meta:
        abstract = True
        
    
      
        


 

class BedStayBase(models.Model): 

    fromDate = models.DateField(null = False, blank =  True, )
    
    toDate = models.DateField(null = False, blank =  True, )
    
    admission = models.ForeignKey('admission.Admission', related_name='bedStays')
        
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    @property   
    def admissionDisplayName(self):
        return self.admission.__str__()
    
    
    def __str__(self):
        return self.fromDate+ "" 
        
    class Meta:
        abstract = True
        
    
      
        


 

class EmployeeBase(PersonBase): 

    active = models.NullBooleanField(null = False, blank =  True, )
    
        
    appUser =    models.OneToOneField("users.AppUser",  null = True,blank=True,  related_name="appUser")
        
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    @property   
    def appUserDisplayName(self):
        return self.appUser.__str__()
    
    
    def __str__(self):
        return super().__str__() 
        
    class Meta:
        abstract = True
        
    
      
        


 

class OrderTemplateBase(models.Model): 

 
    @property   
    def displayName(self):
        return self.__str__()
        
    
    
    def __str__(self):
        return self.Empty class - no display name possible 
        
    class Meta:
        abstract = True
        
    
      
        


 

class OrderBase(models.Model): 

    orderTemplate = models.ForeignKey('physicianOrder.OrderTemplate', related_name='order')
        
    
    patient = models.ForeignKey('patients.Patient', related_name='order')
        
    
 
    @property   
    def displayName(self):
        return self.__str__()
        
    @property   
    def orderTemplateDisplayName(self):
        return self.orderTemplate.__str__()
    @property   
    def patientDisplayName(self):
        return self.patient.__str__()
    
    
    def __str__(self):
        return self.orderTemplate+ "" 
        
    class Meta:
        abstract = True
        
    
      
        

  