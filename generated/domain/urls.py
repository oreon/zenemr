
from rest_framework import routers
from .views import *


router = routers.SimpleRouter(trailing_slash=False)

  
router.register(r'appUsers', AppUserViewSet)
router.register(r'appUsersWritable', AppUserWritableViewSet)
router.register(r'appUsersComplete', AppUserCompleteViewSet)
router.register(r'appUsersLookup', AppUserLookupViewSet)
  
router.register(r'appRoles', AppRoleViewSet)
router.register(r'appRolesWritable', AppRoleWritableViewSet)
router.register(r'appRolesComplete', AppRoleCompleteViewSet)
router.register(r'appRolesLookup', AppRoleLookupViewSet)
  
router.register(r'groups', GroupViewSet)
router.register(r'groupsWritable', GroupWritableViewSet)
router.register(r'groupsComplete', GroupCompleteViewSet)
router.register(r'groupsLookup', GroupLookupViewSet)
  
router.register(r'patients', PatientViewSet)
router.register(r'patientsWritable', PatientWritableViewSet)
router.register(r'patientsComplete', PatientCompleteViewSet)
router.register(r'patientsLookup', PatientLookupViewSet)
  
router.register(r'vaccinations', VaccinationViewSet)
router.register(r'vaccinationsWritable', VaccinationWritableViewSet)
router.register(r'vaccinationsComplete', VaccinationCompleteViewSet)
router.register(r'vaccinationsLookup', VaccinationLookupViewSet)
  
router.register(r'encounters', EncounterViewSet)
router.register(r'encountersWritable', EncounterWritableViewSet)
router.register(r'encountersComplete', EncounterCompleteViewSet)
router.register(r'encountersLookup', EncounterLookupViewSet)
  
router.register(r'vaccines', VaccineViewSet)
router.register(r'vaccinesWritable', VaccineWritableViewSet)
router.register(r'vaccinesComplete', VaccineCompleteViewSet)
router.register(r'vaccinesLookup', VaccineLookupViewSet)
  
router.register(r'labTests', LabTestViewSet)
router.register(r'labTestsWritable', LabTestWritableViewSet)
router.register(r'labTestsComplete', LabTestCompleteViewSet)
router.register(r'labTestsLookup', LabTestLookupViewSet)
  
router.register(r'testResultses', TestResultsViewSet)
router.register(r'testResultsesWritable', TestResultsWritableViewSet)
router.register(r'testResultsesComplete', TestResultsCompleteViewSet)
router.register(r'testResultsesLookup', TestResultsLookupViewSet)
  
router.register(r'resultRows', ResultRowViewSet)
router.register(r'resultRowsWritable', ResultRowWritableViewSet)
router.register(r'resultRowsComplete', ResultRowCompleteViewSet)
router.register(r'resultRowsLookup', ResultRowLookupViewSet)
  
router.register(r'facilitys', FacilityViewSet)
router.register(r'facilitysWritable', FacilityWritableViewSet)
router.register(r'facilitysComplete', FacilityCompleteViewSet)
router.register(r'facilitysLookup', FacilityLookupViewSet)
  
router.register(r'rooms', RoomViewSet)
router.register(r'roomsWritable', RoomWritableViewSet)
router.register(r'roomsComplete', RoomCompleteViewSet)
router.register(r'roomsLookup', RoomLookupViewSet)
  
router.register(r'beds', BedViewSet)
router.register(r'bedsWritable', BedWritableViewSet)
router.register(r'bedsComplete', BedCompleteViewSet)
router.register(r'bedsLookup', BedLookupViewSet)
  
router.register(r'wards', WardViewSet)
router.register(r'wardsWritable', WardWritableViewSet)
router.register(r'wardsComplete', WardCompleteViewSet)
router.register(r'wardsLookup', WardLookupViewSet)
  
router.register(r'roomTypes', RoomTypeViewSet)
router.register(r'roomTypesWritable', RoomTypeWritableViewSet)
router.register(r'roomTypesComplete', RoomTypeCompleteViewSet)
router.register(r'roomTypesLookup', RoomTypeLookupViewSet)
  
router.register(r'unusualOccurences', UnusualOccurenceViewSet)
router.register(r'unusualOccurencesWritable', UnusualOccurenceWritableViewSet)
router.register(r'unusualOccurencesComplete', UnusualOccurenceCompleteViewSet)
router.register(r'unusualOccurencesLookup', UnusualOccurenceLookupViewSet)
  
router.register(r'occurenceTypes', OccurenceTypeViewSet)
router.register(r'occurenceTypesWritable', OccurenceTypeWritableViewSet)
router.register(r'occurenceTypesComplete', OccurenceTypeCompleteViewSet)
router.register(r'occurenceTypesLookup', OccurenceTypeLookupViewSet)
  
router.register(r'settingses', SettingsViewSet)
router.register(r'settingsesWritable', SettingsWritableViewSet)
router.register(r'settingsesComplete', SettingsCompleteViewSet)
router.register(r'settingsesLookup', SettingsLookupViewSet)
  
router.register(r'settings', SettingViewSet)
router.register(r'settingsWritable', SettingWritableViewSet)
router.register(r'settingsComplete', SettingCompleteViewSet)
router.register(r'settingsLookup', SettingLookupViewSet)
  
router.register(r'settingNames', SettingNameViewSet)
router.register(r'settingNamesWritable', SettingNameWritableViewSet)
router.register(r'settingNamesComplete', SettingNameCompleteViewSet)
router.register(r'settingNamesLookup', SettingNameLookupViewSet)
  
router.register(r'settingGroups', SettingGroupViewSet)
router.register(r'settingGroupsWritable', SettingGroupWritableViewSet)
router.register(r'settingGroupsComplete', SettingGroupCompleteViewSet)
router.register(r'settingGroupsLookup', SettingGroupLookupViewSet)
  
router.register(r'prescriptionTemplates', PrescriptionTemplateViewSet)
router.register(r'prescriptionTemplatesWritable', PrescriptionTemplateWritableViewSet)
router.register(r'prescriptionTemplatesComplete', PrescriptionTemplateCompleteViewSet)
router.register(r'prescriptionTemplatesLookup', PrescriptionTemplateLookupViewSet)
  
router.register(r'prescriptions', PrescriptionViewSet)
router.register(r'prescriptionsWritable', PrescriptionWritableViewSet)
router.register(r'prescriptionsComplete', PrescriptionCompleteViewSet)
router.register(r'prescriptionsLookup', PrescriptionLookupViewSet)
  
router.register(r'prescriptionItems', PrescriptionItemViewSet)
router.register(r'prescriptionItemsWritable', PrescriptionItemWritableViewSet)
router.register(r'prescriptionItemsComplete', PrescriptionItemCompleteViewSet)
router.register(r'prescriptionItemsLookup', PrescriptionItemLookupViewSet)
  
router.register(r'prescriptionItemTemplates', PrescriptionItemTemplateViewSet)
router.register(r'prescriptionItemTemplatesWritable', PrescriptionItemTemplateWritableViewSet)
router.register(r'prescriptionItemTemplatesComplete', PrescriptionItemTemplateCompleteViewSet)
router.register(r'prescriptionItemTemplatesLookup', PrescriptionItemTemplateLookupViewSet)
  
router.register(r'frequencys', FrequencyViewSet)
router.register(r'frequencysWritable', FrequencyWritableViewSet)
router.register(r'frequencysComplete', FrequencyCompleteViewSet)
router.register(r'frequencysLookup', FrequencyLookupViewSet)
  
router.register(r'atcDrugs', AtcDrugViewSet)
router.register(r'atcDrugsWritable', AtcDrugWritableViewSet)
router.register(r'atcDrugsComplete', AtcDrugCompleteViewSet)
router.register(r'atcDrugsLookup', AtcDrugLookupViewSet)
  
router.register(r'drugs', DrugViewSet)
router.register(r'drugsWritable', DrugWritableViewSet)
router.register(r'drugsComplete', DrugCompleteViewSet)
router.register(r'drugsLookup', DrugLookupViewSet)
  
router.register(r'drugInteractions', DrugInteractionViewSet)
router.register(r'drugInteractionsWritable', DrugInteractionWritableViewSet)
router.register(r'drugInteractionsComplete', DrugInteractionCompleteViewSet)
router.register(r'drugInteractionsLookup', DrugInteractionLookupViewSet)
  
router.register(r'drugCategorys', DrugCategoryViewSet)
router.register(r'drugCategorysWritable', DrugCategoryWritableViewSet)
router.register(r'drugCategorysComplete', DrugCategoryCompleteViewSet)
router.register(r'drugCategorysLookup', DrugCategoryLookupViewSet)
  
router.register(r'findings', FindingViewSet)
router.register(r'findingsWritable', FindingWritableViewSet)
router.register(r'findingsComplete', FindingCompleteViewSet)
router.register(r'findingsLookup', FindingLookupViewSet)
  
router.register(r'physicalFindings', PhysicalFindingViewSet)
router.register(r'physicalFindingsWritable', PhysicalFindingWritableViewSet)
router.register(r'physicalFindingsComplete', PhysicalFindingCompleteViewSet)
router.register(r'physicalFindingsLookup', PhysicalFindingLookupViewSet)
  
router.register(r'labFindings', LabFindingViewSet)
router.register(r'labFindingsWritable', LabFindingWritableViewSet)
router.register(r'labFindingsComplete', LabFindingCompleteViewSet)
router.register(r'labFindingsLookup', LabFindingLookupViewSet)
  
router.register(r'diseases', DiseaseViewSet)
router.register(r'diseasesWritable', DiseaseWritableViewSet)
router.register(r'diseasesComplete', DiseaseCompleteViewSet)
router.register(r'diseasesLookup', DiseaseLookupViewSet)
  
router.register(r'conditionFindings', ConditionFindingViewSet)
router.register(r'conditionFindingsWritable', ConditionFindingWritableViewSet)
router.register(r'conditionFindingsComplete', ConditionFindingCompleteViewSet)
router.register(r'conditionFindingsLookup', ConditionFindingLookupViewSet)
  
router.register(r'conditionCategorys', ConditionCategoryViewSet)
router.register(r'conditionCategorysWritable', ConditionCategoryWritableViewSet)
router.register(r'conditionCategorysComplete', ConditionCategoryCompleteViewSet)
router.register(r'conditionCategorysLookup', ConditionCategoryLookupViewSet)
  
router.register(r'differentialDxs', DifferentialDxViewSet)
router.register(r'differentialDxsWritable', DifferentialDxWritableViewSet)
router.register(r'differentialDxsComplete', DifferentialDxCompleteViewSet)
router.register(r'differentialDxsLookup', DifferentialDxLookupViewSet)
  
router.register(r'dxCategorys', DxCategoryViewSet)
router.register(r'dxCategorysWritable', DxCategoryWritableViewSet)
router.register(r'dxCategorysComplete', DxCategoryCompleteViewSet)
router.register(r'dxCategorysLookup', DxCategoryLookupViewSet)
  
router.register(r'patientFindings', PatientFindingViewSet)
router.register(r'patientFindingsWritable', PatientFindingWritableViewSet)
router.register(r'patientFindingsComplete', PatientFindingCompleteViewSet)
router.register(r'patientFindingsLookup', PatientFindingLookupViewSet)
  
router.register(r'patientDiffDxs', PatientDiffDxViewSet)
router.register(r'patientDiffDxsWritable', PatientDiffDxWritableViewSet)
router.register(r'patientDiffDxsComplete', PatientDiffDxCompleteViewSet)
router.register(r'patientDiffDxsLookup', PatientDiffDxLookupViewSet)
  
router.register(r'dxTests', DxTestViewSet)
router.register(r'dxTestsWritable', DxTestWritableViewSet)
router.register(r'dxTestsComplete', DxTestCompleteViewSet)
router.register(r'dxTestsLookup', DxTestLookupViewSet)
  
router.register(r'chronicConditions', ChronicConditionViewSet)
router.register(r'chronicConditionsWritable', ChronicConditionWritableViewSet)
router.register(r'chronicConditionsComplete', ChronicConditionCompleteViewSet)
router.register(r'chronicConditionsLookup', ChronicConditionLookupViewSet)
  
router.register(r'codes', CodeViewSet)
router.register(r'codesWritable', CodeWritableViewSet)
router.register(r'codesComplete', CodeCompleteViewSet)
router.register(r'codesLookup', CodeLookupViewSet)
  
router.register(r'chapters', ChapterViewSet)
router.register(r'chaptersWritable', ChapterWritableViewSet)
router.register(r'chaptersComplete', ChapterCompleteViewSet)
router.register(r'chaptersLookup', ChapterLookupViewSet)
  
router.register(r'sections', SectionViewSet)
router.register(r'sectionsWritable', SectionWritableViewSet)
router.register(r'sectionsComplete', SectionCompleteViewSet)
router.register(r'sectionsLookup', SectionLookupViewSet)
  
router.register(r'simpleCodes', SimpleCodeViewSet)
router.register(r'simpleCodesWritable', SimpleCodeWritableViewSet)
router.register(r'simpleCodesComplete', SimpleCodeCompleteViewSet)
router.register(r'simpleCodesLookup', SimpleCodeLookupViewSet)
  
router.register(r'appliedCharts', AppliedChartViewSet)
router.register(r'appliedChartsWritable', AppliedChartWritableViewSet)
router.register(r'appliedChartsComplete', AppliedChartCompleteViewSet)
router.register(r'appliedChartsLookup', AppliedChartLookupViewSet)
  
router.register(r'charts', ChartViewSet)
router.register(r'chartsWritable', ChartWritableViewSet)
router.register(r'chartsComplete', ChartCompleteViewSet)
router.register(r'chartsLookup', ChartLookupViewSet)
  
router.register(r'chartItems', ChartItemViewSet)
router.register(r'chartItemsWritable', ChartItemWritableViewSet)
router.register(r'chartItemsComplete', ChartItemCompleteViewSet)
router.register(r'chartItemsLookup', ChartItemLookupViewSet)
  
router.register(r'chartProcedures', ChartProcedureViewSet)
router.register(r'chartProceduresWritable', ChartProcedureWritableViewSet)
router.register(r'chartProceduresComplete', ChartProcedureCompleteViewSet)
router.register(r'chartProceduresLookup', ChartProcedureLookupViewSet)
  
router.register(r'invoices', InvoiceViewSet)
router.register(r'invoicesWritable', InvoiceWritableViewSet)
router.register(r'invoicesComplete', InvoiceCompleteViewSet)
router.register(r'invoicesLookup', InvoiceLookupViewSet)
  
router.register(r'services', ServiceViewSet)
router.register(r'servicesWritable', ServiceWritableViewSet)
router.register(r'servicesComplete', ServiceCompleteViewSet)
router.register(r'servicesLookup', ServiceLookupViewSet)
  
router.register(r'invoiceItems', InvoiceItemViewSet)
router.register(r'invoiceItemsWritable', InvoiceItemWritableViewSet)
router.register(r'invoiceItemsComplete', InvoiceItemCompleteViewSet)
router.register(r'invoiceItemsLookup', InvoiceItemLookupViewSet)
  
router.register(r'appointments', AppointmentViewSet)
router.register(r'appointmentsWritable', AppointmentWritableViewSet)
router.register(r'appointmentsComplete', AppointmentCompleteViewSet)
router.register(r'appointmentsLookup', AppointmentLookupViewSet)
  
router.register(r'admissions', AdmissionViewSet)
router.register(r'admissionsWritable', AdmissionWritableViewSet)
router.register(r'admissionsComplete', AdmissionCompleteViewSet)
router.register(r'admissionsLookup', AdmissionLookupViewSet)
  
router.register(r'bedStays', BedStayViewSet)
router.register(r'bedStaysWritable', BedStayWritableViewSet)
router.register(r'bedStaysComplete', BedStayCompleteViewSet)
router.register(r'bedStaysLookup', BedStayLookupViewSet)
  
router.register(r'employees', EmployeeViewSet)
router.register(r'employeesWritable', EmployeeWritableViewSet)
router.register(r'employeesComplete', EmployeeCompleteViewSet)
router.register(r'employeesLookup', EmployeeLookupViewSet)
  
router.register(r'orderTemplates', OrderTemplateViewSet)
router.register(r'orderTemplatesWritable', OrderTemplateWritableViewSet)
router.register(r'orderTemplatesComplete', OrderTemplateCompleteViewSet)
router.register(r'orderTemplatesLookup', OrderTemplateLookupViewSet)
  
router.register(r'orders', OrderViewSet)
router.register(r'ordersWritable', OrderWritableViewSet)
router.register(r'ordersComplete', OrderCompleteViewSet)
router.register(r'ordersLookup', OrderLookupViewSet)

    
