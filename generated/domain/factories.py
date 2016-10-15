
 
 # factories.py
import factory
from . import models



class  AppUserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. AppUser
        
        
    userName = factory.Sequence(lambda n: CharField) 
    
    password = factory.Sequence(lambda n: CharField) 
    
    enabled = factory.Sequence(lambda n: NullBooleanField) 
    
    groups =    models.ManyToManyField("users.Group",  blank=True,  related_name="groups")
            
        
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



class  AppRoleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. AppRole
        
        
    name = factory.Sequence(lambda n: CharField) 
    
    groups =    models.ManyToManyField("users.Group",  blank=True,  related_name="groups")
            
        
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



class  GroupFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. Group
        
        
    appUsers =    models.ManyToManyField("users.AppUser",  blank=True,  related_name="appUsers")
            
        
    
    appRoles =    models.ManyToManyField("users.AppRole",  blank=True,  related_name="appRoles")
            
        
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



class  PatientFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. Patient
        
        
    firstName = factory.Sequence(lambda n: CharField) 
    
    lastName = factory.Sequence(lambda n: CharField) 
    
    customerType = factory.Sequence(lambda n: CharField) 
    
            
        
    
            
        
    
            
        
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



class  VaccinationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. Vaccination
        
        
    review = factory.Sequence(lambda n: TextField) 
    
    rating = factory.Sequence(lambda n: PositiveIntegerField) 
    
    vaccine = factory.SubFactory(patients.VaccineFactory)
        
    
    patient = factory.SubFactory(patients.PatientFactory)
        
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



class  EncounterFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. Encounter
        
        
    reason = factory.Sequence(lambda n: TextField) 
    
    patient = factory.SubFactory(patients.PatientFactory)
        
    
    labTests =    models.ManyToManyField("patients.LabTest",  blank=True,  related_name="labTests")
            
        
    
        
    prescription =    models.OneToOneField("prescription.Prescription",  blank=True,  related_name="prescription")
        
    
    admission = factory.SubFactory(admission.AdmissionFactory)
        
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



class  VaccineFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. Vaccine
        
        
    name = factory.Sequence(lambda n: CharField) 
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



class  LabTestFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. LabTest
        
        
    name = factory.Sequence(lambda n: CharField) 
    
    encounters =    models.ManyToManyField("patients.Encounter",  blank=True,  related_name="encounters")
            
        
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



class  TestResultsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. TestResults
        
        
    patient = factory.SubFactory(patients.PatientFactory)
        
    
            
        
    
    labTest = factory.SubFactory(patients.LabTestFactory)
        
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



class  ResultRowFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. ResultRow
        
        
    testResults = factory.SubFactory(patients.TestResultsFactory)
        
    
    name = factory.Sequence(lambda n: CharField) 
    
    value = factory.Sequence(lambda n: CharField) 
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



class  FacilityFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. Facility
        
        
    name = factory.Sequence(lambda n: CharField) 
    
            
        
    
    isResidential = factory.Sequence(lambda n: NullBooleanField) 
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



class  RoomFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. Room
        
        
            
        
    
    name = factory.Sequence(lambda n: CharField) 
    
    roomType = factory.SubFactory(facility.RoomTypeFactory)
        
    
    ward = factory.SubFactory(facility.WardFactory)
        
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



class  BedFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. Bed
        
        
    room = factory.SubFactory(facility.RoomFactory)
        
    
    name = factory.Sequence(lambda n: CharField) 
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



class  WardFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. Ward
        
        
    facility = factory.SubFactory(facility.FacilityFactory)
        
    
            
        
    
    name = factory.Sequence(lambda n: CharField) 
    
    gender = factory.Sequence(lambda n: CharField) 
    
    maxAge = factory.Sequence(lambda n: PositiveIntegerField) 
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



class  RoomTypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. RoomType
        
        
    name = factory.Sequence(lambda n: CharField) 
    
    description = factory.Sequence(lambda n: TextField) 
    
    rate = factory.Sequence(lambda n: CharField) 
    
    numberOfBeds = factory.Sequence(lambda n: PositiveIntegerField) 
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



class  UnusualOccurenceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. UnusualOccurence
        
        
    occurenceType = factory.SubFactory(unusualoccurences.OccurenceTypeFactory)
        
    
    category = factory.Sequence(lambda n: CharField) 
    
    severity = factory.Sequence(lambda n: CharField) 
    
    description = factory.Sequence(lambda n: TextField) 
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



class  OccurenceTypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. OccurenceType
        
        
    name = factory.Sequence(lambda n: CharField) 
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



class  SettingsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. Settings
        
        
     

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



class  SettingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. Setting
        
        
    value = factory.Sequence(lambda n: CharField) 
    
    settingName = factory.SubFactory(settings.SettingNameFactory)
        
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



class  SettingNameFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. SettingName
        
        
    name = factory.Sequence(lambda n: CharField) 
    
    settingGroup = factory.SubFactory(settings.SettingGroupFactory)
        
    
    defaultValue = factory.Sequence(lambda n: CharField) 
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



class  SettingGroupFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. SettingGroup
        
        
    name = factory.Sequence(lambda n: CharField) 
    
            
        
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



class  PrescriptionTemplateFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. PrescriptionTemplate
        
        
    name = factory.Sequence(lambda n: CharField) 
    
    directivesForPatient = factory.Sequence(lambda n: TextField) 
    
            
        
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



class  PrescriptionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. Prescription
        
        
            
        
    
    active = factory.Sequence(lambda n: NullBooleanField) 
    
    directivesForPatient = factory.Sequence(lambda n: TextField) 
    
    drugs = factory.Sequence(lambda n: CharField) 
    
    startDate = factory.Sequence(lambda n: DateField) 
    
    endDate = factory.Sequence(lambda n: DateField) 
    
        
    encounter =    models.OneToOneField("patients.Encounter",  blank=True,  related_name="encounter")
        
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



class  PrescriptionItemFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. PrescriptionItem
        
        
    drug = factory.SubFactory(drugs.DrugFactory)
        
    
    qty = factory.Sequence(lambda n: CharField) 
    
    strength = factory.Sequence(lambda n: CharField) 
    
    prescription = factory.SubFactory(prescription.PrescriptionFactory)
        
    
    route = factory.Sequence(lambda n: CharField) 
    
    duration = factory.Sequence(lambda n: PositiveIntegerField) 
    
    frequency = factory.SubFactory(prescription.FrequencyFactory)
        
    
    remarks = factory.Sequence(lambda n: CharField) 
    
    brandName = factory.Sequence(lambda n: CharField) 
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



class  PrescriptionItemTemplateFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. PrescriptionItemTemplate
        
        
    drug = factory.SubFactory(drugs.DrugFactory)
        
    
    qty = factory.Sequence(lambda n: CharField) 
    
    frequency = factory.SubFactory(prescription.FrequencyFactory)
        
    
    strength = factory.Sequence(lambda n: CharField) 
    
    route = factory.Sequence(lambda n: CharField) 
    
    duration = factory.Sequence(lambda n: PositiveIntegerField) 
    
    remarks = factory.Sequence(lambda n: CharField) 
    
    brandName = factory.Sequence(lambda n: CharField) 
    
    prescriptionTemplate = factory.SubFactory(prescription.PrescriptionTemplateFactory)
        
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



class  FrequencyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. Frequency
        
        
    name = factory.Sequence(lambda n: CharField) 
    
    qtyPerDay = factory.Sequence(lambda n: PositiveIntegerField) 
    
    remarkts = factory.Sequence(lambda n: TextField) 
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



class  AtcDrugFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. AtcDrug
        
        
    code = factory.Sequence(lambda n: CharField) 
    
    name = factory.Sequence(lambda n: CharField) 
    
            
        
    
    drug = factory.SubFactory(drugs.DrugFactory)
        
    
    parent = factory.SubFactory(drugs.AtcDrugFactory)
        
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



class  DrugFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. Drug
        
        
    name = factory.Sequence(lambda n: CharField) 
    
    absorption = factory.Sequence(lambda n: TextField) 
    
    biotransformation = factory.Sequence(lambda n: TextField) 
    
    atcCodes = factory.Sequence(lambda n: CharField) 
    
    contraIndication = factory.Sequence(lambda n: TextField) 
    
    description = factory.Sequence(lambda n: TextField) 
    
    dosageForm = factory.Sequence(lambda n: CharField) 
    
    foodInteractions = factory.Sequence(lambda n: TextField) 
    
    halfLife = factory.Sequence(lambda n: TextField) 
    
    indication = factory.Sequence(lambda n: TextField) 
    
    halfLifeNumberOfHours = factory.Sequence(lambda n: CharField) 
    
    mechanismOfAction = factory.Sequence(lambda n: TextField) 
    
    patientInfo = factory.Sequence(lambda n: TextField) 
    
    pharmacology = factory.Sequence(lambda n: TextField) 
    
            
        
    
    drugCategorys =    models.ManyToManyField("drugs.DrugCategory",  blank=True,  related_name="drugCategorys")
            
        
    
    toxicity = factory.Sequence(lambda n: TextField) 
    
    routeOfElimination = factory.Sequence(lambda n: TextField) 
    
    volumeOfDistribution = factory.Sequence(lambda n: CharField) 
    
    drugBankId = factory.Sequence(lambda n: CharField) 
    
    categories = factory.Sequence(lambda n: CharField) 
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



class  DrugInteractionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. DrugInteraction
        
        
    description = factory.Sequence(lambda n: TextField) 
    
    drug = factory.SubFactory(drugs.DrugFactory)
        
    
    interactingDrug = factory.SubFactory(drugs.DrugFactory)
        
    
    severity = factory.Sequence(lambda n: CharField) 
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



class  DrugCategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. DrugCategory
        
        
    name = factory.Sequence(lambda n: CharField) 
    
    drugs =    models.ManyToManyField("drugs.Drug",  blank=True,  related_name="drugs")
            
        
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



class  FindingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. Finding
        
        
    name = factory.Sequence(lambda n: CharField) 
    
            
        
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



class  PhysicalFindingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. PhysicalFinding
        
        
    name = factory.Sequence(lambda n: CharField) 
    
            
        
    
    icdCode = factory.Sequence(lambda n: CharField) 
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



class  LabFindingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. LabFinding
        
        
    name = factory.Sequence(lambda n: CharField) 
    
            
        
    
    testName = factory.Sequence(lambda n: CharField) 
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



class  DiseaseFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. Disease
        
        
    gender = factory.Sequence(lambda n: CharField) 
    
    name = factory.Sequence(lambda n: CharField) 
    
            
        
    
    relatedDisease = factory.SubFactory(ddx.DiseaseFactory)
        
    
    conditionCategory = factory.SubFactory(ddx.ConditionCategoryFactory)
        
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



class  ConditionFindingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. ConditionFinding
        
        
    disease = factory.SubFactory(ddx.DiseaseFactory)
        
    
    falsePositive = factory.Sequence(lambda n: NullBooleanField) 
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



class  ConditionCategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. ConditionCategory
        
        
    name = factory.Sequence(lambda n: CharField) 
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



class  DifferentialDxFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. DifferentialDx
        
        
    name = factory.Sequence(lambda n: CharField) 
    
    dxCategory = factory.SubFactory(ddx.DxCategoryFactory)
        
    
    finding = factory.SubFactory(ddx.FindingFactory)
        
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



class  DxCategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. DxCategory
        
        
    name = factory.Sequence(lambda n: CharField) 
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



class  PatientFindingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. PatientFinding
        
        
    finding = factory.SubFactory(ddx.FindingFactory)
        
    
    patientDiffDx = factory.SubFactory(ddx.PatientDiffDxFactory)
        
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



class  PatientDiffDxFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. PatientDiffDx
        
        
            
        
    
    notes = factory.Sequence(lambda n: TextField) 
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



class  DxTestFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. DxTest
        
        
    name = factory.Sequence(lambda n: CharField) 
    
    description = factory.Sequence(lambda n: TextField) 
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



class  ChronicConditionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. ChronicCondition
        
        
    name = factory.Sequence(lambda n: CharField) 
    
            
        
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



class  CodeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. Code
        
        
    name = factory.Sequence(lambda n: CharField) 
    
    description = factory.Sequence(lambda n: TextField) 
    
    includes = factory.Sequence(lambda n: TextField) 
    
    notIncludedHere = factory.Sequence(lambda n: TextField) 
    
    codeFirst = factory.Sequence(lambda n: TextField) 
    
    section = factory.SubFactory(codes.SectionFactory)
        
    
    notCodedHere = factory.Sequence(lambda n: TextField) 
    
    codeAlso = factory.Sequence(lambda n: TextField) 
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



class  ChapterFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. Chapter
        
        
    name = factory.Sequence(lambda n: CharField) 
    
    description = factory.Sequence(lambda n: TextField) 
    
            
        
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



class  SectionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. Section
        
        
    name = factory.Sequence(lambda n: CharField) 
    
    description = factory.Sequence(lambda n: TextField) 
    
    chapter = factory.SubFactory(codes.ChapterFactory)
        
    
            
        
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



class  SimpleCodeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. SimpleCode
        
        
    name = factory.Sequence(lambda n: CharField) 
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



class  AppliedChartFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. AppliedChart
        
        
    chart = factory.SubFactory(charts.ChartFactory)
        
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



class  ChartFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. Chart
        
        
            
        
    
    name = factory.Sequence(lambda n: CharField) 
    
    chronicCondition = factory.SubFactory(ddx.ChronicConditionFactory)
        
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



class  ChartItemFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. ChartItem
        
        
    name = factory.Sequence(lambda n: CharField) 
    
    duration = factory.Sequence(lambda n: PositiveIntegerField) 
    
    chart = factory.SubFactory(charts.ChartFactory)
        
    
    frequencyPeriod = factory.Sequence(lambda n: CharField) 
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



class  ChartProcedureFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. ChartProcedure
        
        
    chartItem = factory.SubFactory(charts.ChartItemFactory)
        
    
    dueDate = factory.Sequence(lambda n: DateField) 
    
    datePerformed = factory.Sequence(lambda n: DateField) 
    
    remarks = factory.Sequence(lambda n: TextField) 
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



class  InvoiceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. Invoice
        
        
            
        
    
    notes = factory.Sequence(lambda n: CharField) 
    
    totalAmount = factory.Sequence(lambda n: DecimalField) 
    
    paidAmount = factory.Sequence(lambda n: DecimalField) 
    
    patient = factory.SubFactory(patients.PatientFactory)
        
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



class  ServiceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. Service
        
        
    name = factory.Sequence(lambda n: CharField) 
    
    price = factory.Sequence(lambda n: DecimalField) 
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



class  InvoiceItemFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. InvoiceItem
        
        
    units = factory.Sequence(lambda n: PositiveIntegerField) 
    
    service = factory.SubFactory(billing.ServiceFactory)
        
    
    invoice = factory.SubFactory(billing.InvoiceFactory)
        
    
    appliedPrice = factory.Sequence(lambda n: DecimalField) 
    
    total = factory.Sequence(lambda n: DecimalField) 
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



class  AppointmentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. Appointment
        
        
    start = factory.Sequence(lambda n: DateTimeField) 
    
    end = factory.Sequence(lambda n: DateTimeField) 
    
    remarks = factory.Sequence(lambda n: TextField) 
    
    units = factory.Sequence(lambda n: PositiveIntegerField) 
    
    patient = factory.SubFactory(patients.PatientFactory)
        
    
    employee = factory.SubFactory(employees.EmployeeFactory)
        
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



class  AdmissionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. Admission
        
        
    admissionNote = factory.Sequence(lambda n: TextField) 
    
    dischargeDate = factory.Sequence(lambda n: DateField) 
    
    dischargeNote = factory.Sequence(lambda n: TextField) 
    
    dischargeCode = factory.Sequence(lambda n: CharField) 
    
    currentBed = factory.Sequence(lambda n: CharField) 
    
    isCurrent = factory.Sequence(lambda n: NullBooleanField) 
    
    invoice = factory.SubFactory(billing.InvoiceFactory)
        
    
            
        
    
            
        
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



class  BedStayFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. BedStay
        
        
    fromDate = factory.Sequence(lambda n: DateField) 
    
    toDate = factory.Sequence(lambda n: DateField) 
    
    admission = factory.SubFactory(admission.AdmissionFactory)
        
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



class  EmployeeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. Employee
        
        
    firstName = factory.Sequence(lambda n: CharField) 
    
    lastName = factory.Sequence(lambda n: CharField) 
    
    active = factory.Sequence(lambda n: NullBooleanField) 
    
        
    appUser =    models.OneToOneField("users.AppUser",  blank=True,  related_name="appUser")
        
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



class  OrderTemplateFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. OrderTemplate
        
        
     

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



class  OrderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models. Order
        
        
    orderTemplate = factory.SubFactory(physicianOrder.OrderTemplateFactory)
        
    
    patient = factory.SubFactory(patients.PatientFactory)
        
    
 

    #first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    #group = factory.SubFactory(GroupFactory)



 