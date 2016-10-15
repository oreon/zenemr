
	 	 
	 	
	import {AppUserListWrapper,AppUserEdit,AppUserView} from './admin/AppUserList';

	import {AppRoleListWrapper,AppRoleEdit,AppRoleView} from './admin/AppRoleList';

	import {GroupListWrapper,GroupEdit,GroupView} from './admin/GroupList';

	import {PatientListWrapper,PatientEdit,PatientView} from './admin/PatientList';

	import {VaccinationListWrapper,VaccinationEdit,VaccinationView} from './admin/VaccinationList';

	import {EncounterListWrapper,EncounterEdit,EncounterView} from './admin/EncounterList';

	import {VaccineListWrapper,VaccineEdit,VaccineView} from './admin/VaccineList';

	import {LabTestListWrapper,LabTestEdit,LabTestView} from './admin/LabTestList';

	import {TestResultsListWrapper,TestResultsEdit,TestResultsView} from './admin/TestResultsList';

	import {ResultRowListWrapper,ResultRowEdit,ResultRowView} from './admin/ResultRowList';

	import {FacilityListWrapper,FacilityEdit,FacilityView} from './admin/FacilityList';

	import {RoomListWrapper,RoomEdit,RoomView} from './admin/RoomList';

	import {BedListWrapper,BedEdit,BedView} from './admin/BedList';

	import {WardListWrapper,WardEdit,WardView} from './admin/WardList';

	import {RoomTypeListWrapper,RoomTypeEdit,RoomTypeView} from './admin/RoomTypeList';

	import {UnusualOccurenceListWrapper,UnusualOccurenceEdit,UnusualOccurenceView} from './admin/UnusualOccurenceList';

	import {OccurenceTypeListWrapper,OccurenceTypeEdit,OccurenceTypeView} from './admin/OccurenceTypeList';

	import {SettingsListWrapper,SettingsEdit,SettingsView} from './admin/SettingsList';

	import {SettingListWrapper,SettingEdit,SettingView} from './admin/SettingList';

	import {SettingNameListWrapper,SettingNameEdit,SettingNameView} from './admin/SettingNameList';

	import {SettingGroupListWrapper,SettingGroupEdit,SettingGroupView} from './admin/SettingGroupList';

	import {PrescriptionTemplateListWrapper,PrescriptionTemplateEdit,PrescriptionTemplateView} from './admin/PrescriptionTemplateList';

	import {PrescriptionListWrapper,PrescriptionEdit,PrescriptionView} from './admin/PrescriptionList';

	import {PrescriptionItemListWrapper,PrescriptionItemEdit,PrescriptionItemView} from './admin/PrescriptionItemList';

	import {PrescriptionItemTemplateListWrapper,PrescriptionItemTemplateEdit,PrescriptionItemTemplateView} from './admin/PrescriptionItemTemplateList';

	import {FrequencyListWrapper,FrequencyEdit,FrequencyView} from './admin/FrequencyList';

	import {AtcDrugListWrapper,AtcDrugEdit,AtcDrugView} from './admin/AtcDrugList';

	import {DrugListWrapper,DrugEdit,DrugView} from './admin/DrugList';

	import {DrugInteractionListWrapper,DrugInteractionEdit,DrugInteractionView} from './admin/DrugInteractionList';

	import {DrugCategoryListWrapper,DrugCategoryEdit,DrugCategoryView} from './admin/DrugCategoryList';

	import {FindingListWrapper,FindingEdit,FindingView} from './admin/FindingList';

	import {PhysicalFindingListWrapper,PhysicalFindingEdit,PhysicalFindingView} from './admin/PhysicalFindingList';

	import {LabFindingListWrapper,LabFindingEdit,LabFindingView} from './admin/LabFindingList';

	import {DiseaseListWrapper,DiseaseEdit,DiseaseView} from './admin/DiseaseList';

	import {ConditionFindingListWrapper,ConditionFindingEdit,ConditionFindingView} from './admin/ConditionFindingList';

	import {ConditionCategoryListWrapper,ConditionCategoryEdit,ConditionCategoryView} from './admin/ConditionCategoryList';

	import {DifferentialDxListWrapper,DifferentialDxEdit,DifferentialDxView} from './admin/DifferentialDxList';

	import {DxCategoryListWrapper,DxCategoryEdit,DxCategoryView} from './admin/DxCategoryList';

	import {PatientFindingListWrapper,PatientFindingEdit,PatientFindingView} from './admin/PatientFindingList';

	import {PatientDiffDxListWrapper,PatientDiffDxEdit,PatientDiffDxView} from './admin/PatientDiffDxList';

	import {DxTestListWrapper,DxTestEdit,DxTestView} from './admin/DxTestList';

	import {ChronicConditionListWrapper,ChronicConditionEdit,ChronicConditionView} from './admin/ChronicConditionList';

	import {CodeListWrapper,CodeEdit,CodeView} from './admin/CodeList';

	import {ChapterListWrapper,ChapterEdit,ChapterView} from './admin/ChapterList';

	import {SectionListWrapper,SectionEdit,SectionView} from './admin/SectionList';

	import {SimpleCodeListWrapper,SimpleCodeEdit,SimpleCodeView} from './admin/SimpleCodeList';

	import {AppliedChartListWrapper,AppliedChartEdit,AppliedChartView} from './admin/AppliedChartList';

	import {ChartListWrapper,ChartEdit,ChartView} from './admin/ChartList';

	import {ChartItemListWrapper,ChartItemEdit,ChartItemView} from './admin/ChartItemList';

	import {ChartProcedureListWrapper,ChartProcedureEdit,ChartProcedureView} from './admin/ChartProcedureList';

	import {InvoiceListWrapper,InvoiceEdit,InvoiceView} from './admin/InvoiceList';

	import {ServiceListWrapper,ServiceEdit,ServiceView} from './admin/ServiceList';

	import {InvoiceItemListWrapper,InvoiceItemEdit,InvoiceItemView} from './admin/InvoiceItemList';

	import {AppointmentListWrapper,AppointmentEdit,AppointmentView} from './admin/AppointmentList';

	import {AdmissionListWrapper,AdmissionEdit,AdmissionView} from './admin/AdmissionList';

	import {BedStayListWrapper,BedStayEdit,BedStayView} from './admin/BedStayList';

	import {EmployeeListWrapper,EmployeeEdit,EmployeeView} from './admin/EmployeeList';

	import {OrderTemplateListWrapper,OrderTemplateEdit,OrderTemplateView} from './admin/OrderTemplateList';

	import {OrderListWrapper,OrderEdit,OrderView} from './admin/OrderList';

	 	
	 	export const lookups = [ 'AppUser' , 'AppRole' , 'Group' , 'Patient' , 'Vaccination' , 'Encounter' , 'Vaccine' , 'LabTest' , 'TestResults' , 'ResultRow' , 'Facility' , 'Room' , 'Bed' , 'Ward' , 'RoomType' , 'UnusualOccurence' , 'OccurenceType' , 'Settings' , 'Setting' , 'SettingName' , 'SettingGroup' , 'PrescriptionTemplate' , 'Prescription' , 'PrescriptionItem' , 'PrescriptionItemTemplate' , 'Frequency' , 'AtcDrug' , 'Drug' , 'DrugInteraction' , 'DrugCategory' , 'Finding' , 'PhysicalFinding' , 'LabFinding' , 'Disease' , 'ConditionFinding' , 'ConditionCategory' , 'DifferentialDx' , 'DxCategory' , 'PatientFinding' , 'PatientDiffDx' , 'DxTest' , 'ChronicCondition' , 'Code' , 'Chapter' , 'Section' , 'SimpleCode' , 'AppliedChart' , 'Chart' , 'ChartItem' , 'ChartProcedure' , 'Invoice' , 'Service' , 'InvoiceItem' , 'Appointment' , 'Admission' , 'BedStay' , 'Employee' , 'OrderTemplate' , 'Order' ]
	 	
	 	
    
 
  
 <Route path="/admin/AppUserList" component={AppUserListWrapper} />
 
 <Route path="/admin/AppUserView/:id" component={AppUserView} />

<Route path="/admin/AppUserEdit" component={AppUserEdit}>
    <Route path="/admin/AppUserEdit/:id" component={AppUserEdit} >
        <Route path="/admin/AppUserEdit/:id/:parent" component={AppUserEdit} />
    </Route>
</Route>
 
 <Route path="/admin/AppRoleList" component={AppRoleListWrapper} />
 
 <Route path="/admin/AppRoleView/:id" component={AppRoleView} />

<Route path="/admin/AppRoleEdit" component={AppRoleEdit}>
    <Route path="/admin/AppRoleEdit/:id" component={AppRoleEdit} >
        <Route path="/admin/AppRoleEdit/:id/:parent" component={AppRoleEdit} />
    </Route>
</Route>
 
 <Route path="/admin/GroupList" component={GroupListWrapper} />
 
 <Route path="/admin/GroupView/:id" component={GroupView} />

<Route path="/admin/GroupEdit" component={GroupEdit}>
    <Route path="/admin/GroupEdit/:id" component={GroupEdit} >
        <Route path="/admin/GroupEdit/:id/:parent" component={GroupEdit} />
    </Route>
</Route>
   
 
  
 <Route path="/admin/PatientList" component={PatientListWrapper} />
 
 <Route path="/admin/PatientView/:id" component={PatientView} />

<Route path="/admin/PatientEdit" component={PatientEdit}>
    <Route path="/admin/PatientEdit/:id" component={PatientEdit} >
        <Route path="/admin/PatientEdit/:id/:parent" component={PatientEdit} />
    </Route>
</Route>
 
 <Route path="/admin/VaccinationList" component={VaccinationListWrapper} />
 
 <Route path="/admin/VaccinationView/:id" component={VaccinationView} />

<Route path="/admin/VaccinationEdit" component={VaccinationEdit}>
    <Route path="/admin/VaccinationEdit/:id" component={VaccinationEdit} >
        <Route path="/admin/VaccinationEdit/:id/:parent" component={VaccinationEdit} />
    </Route>
</Route>
 
 <Route path="/admin/EncounterList" component={EncounterListWrapper} />
 
 <Route path="/admin/EncounterView/:id" component={EncounterView} />

<Route path="/admin/EncounterEdit" component={EncounterEdit}>
    <Route path="/admin/EncounterEdit/:id" component={EncounterEdit} >
        <Route path="/admin/EncounterEdit/:id/:parent" component={EncounterEdit} />
    </Route>
</Route>
 
 <Route path="/admin/VaccineList" component={VaccineListWrapper} />
 
 <Route path="/admin/VaccineView/:id" component={VaccineView} />

<Route path="/admin/VaccineEdit" component={VaccineEdit}>
    <Route path="/admin/VaccineEdit/:id" component={VaccineEdit} >
        <Route path="/admin/VaccineEdit/:id/:parent" component={VaccineEdit} />
    </Route>
</Route>
 
 <Route path="/admin/LabTestList" component={LabTestListWrapper} />
 
 <Route path="/admin/LabTestView/:id" component={LabTestView} />

<Route path="/admin/LabTestEdit" component={LabTestEdit}>
    <Route path="/admin/LabTestEdit/:id" component={LabTestEdit} >
        <Route path="/admin/LabTestEdit/:id/:parent" component={LabTestEdit} />
    </Route>
</Route>
 
 <Route path="/admin/TestResultsList" component={TestResultsListWrapper} />
 
 <Route path="/admin/TestResultsView/:id" component={TestResultsView} />

<Route path="/admin/TestResultsEdit" component={TestResultsEdit}>
    <Route path="/admin/TestResultsEdit/:id" component={TestResultsEdit} >
        <Route path="/admin/TestResultsEdit/:id/:parent" component={TestResultsEdit} />
    </Route>
</Route>
 
 <Route path="/admin/ResultRowList" component={ResultRowListWrapper} />
 
 <Route path="/admin/ResultRowView/:id" component={ResultRowView} />

<Route path="/admin/ResultRowEdit" component={ResultRowEdit}>
    <Route path="/admin/ResultRowEdit/:id" component={ResultRowEdit} >
        <Route path="/admin/ResultRowEdit/:id/:parent" component={ResultRowEdit} />
    </Route>
</Route>
   
 
  
 <Route path="/admin/FacilityList" component={FacilityListWrapper} />
 
 <Route path="/admin/FacilityView/:id" component={FacilityView} />

<Route path="/admin/FacilityEdit" component={FacilityEdit}>
    <Route path="/admin/FacilityEdit/:id" component={FacilityEdit} >
        <Route path="/admin/FacilityEdit/:id/:parent" component={FacilityEdit} />
    </Route>
</Route>
 
 <Route path="/admin/RoomList" component={RoomListWrapper} />
 
 <Route path="/admin/RoomView/:id" component={RoomView} />

<Route path="/admin/RoomEdit" component={RoomEdit}>
    <Route path="/admin/RoomEdit/:id" component={RoomEdit} >
        <Route path="/admin/RoomEdit/:id/:parent" component={RoomEdit} />
    </Route>
</Route>
 
 <Route path="/admin/BedList" component={BedListWrapper} />
 
 <Route path="/admin/BedView/:id" component={BedView} />

<Route path="/admin/BedEdit" component={BedEdit}>
    <Route path="/admin/BedEdit/:id" component={BedEdit} >
        <Route path="/admin/BedEdit/:id/:parent" component={BedEdit} />
    </Route>
</Route>
 
 <Route path="/admin/WardList" component={WardListWrapper} />
 
 <Route path="/admin/WardView/:id" component={WardView} />

<Route path="/admin/WardEdit" component={WardEdit}>
    <Route path="/admin/WardEdit/:id" component={WardEdit} >
        <Route path="/admin/WardEdit/:id/:parent" component={WardEdit} />
    </Route>
</Route>
 
 <Route path="/admin/RoomTypeList" component={RoomTypeListWrapper} />
 
 <Route path="/admin/RoomTypeView/:id" component={RoomTypeView} />

<Route path="/admin/RoomTypeEdit" component={RoomTypeEdit}>
    <Route path="/admin/RoomTypeEdit/:id" component={RoomTypeEdit} >
        <Route path="/admin/RoomTypeEdit/:id/:parent" component={RoomTypeEdit} />
    </Route>
</Route>
   
 
  
 <Route path="/admin/UnusualOccurenceList" component={UnusualOccurenceListWrapper} />
 
 <Route path="/admin/UnusualOccurenceView/:id" component={UnusualOccurenceView} />

<Route path="/admin/UnusualOccurenceEdit" component={UnusualOccurenceEdit}>
    <Route path="/admin/UnusualOccurenceEdit/:id" component={UnusualOccurenceEdit} >
        <Route path="/admin/UnusualOccurenceEdit/:id/:parent" component={UnusualOccurenceEdit} />
    </Route>
</Route>
 
 <Route path="/admin/OccurenceTypeList" component={OccurenceTypeListWrapper} />
 
 <Route path="/admin/OccurenceTypeView/:id" component={OccurenceTypeView} />

<Route path="/admin/OccurenceTypeEdit" component={OccurenceTypeEdit}>
    <Route path="/admin/OccurenceTypeEdit/:id" component={OccurenceTypeEdit} >
        <Route path="/admin/OccurenceTypeEdit/:id/:parent" component={OccurenceTypeEdit} />
    </Route>
</Route>
   
 
  
 <Route path="/admin/SettingsList" component={SettingsListWrapper} />
 
 <Route path="/admin/SettingsView/:id" component={SettingsView} />

<Route path="/admin/SettingsEdit" component={SettingsEdit}>
    <Route path="/admin/SettingsEdit/:id" component={SettingsEdit} >
        <Route path="/admin/SettingsEdit/:id/:parent" component={SettingsEdit} />
    </Route>
</Route>
 
 <Route path="/admin/SettingList" component={SettingListWrapper} />
 
 <Route path="/admin/SettingView/:id" component={SettingView} />

<Route path="/admin/SettingEdit" component={SettingEdit}>
    <Route path="/admin/SettingEdit/:id" component={SettingEdit} >
        <Route path="/admin/SettingEdit/:id/:parent" component={SettingEdit} />
    </Route>
</Route>
 
 <Route path="/admin/SettingNameList" component={SettingNameListWrapper} />
 
 <Route path="/admin/SettingNameView/:id" component={SettingNameView} />

<Route path="/admin/SettingNameEdit" component={SettingNameEdit}>
    <Route path="/admin/SettingNameEdit/:id" component={SettingNameEdit} >
        <Route path="/admin/SettingNameEdit/:id/:parent" component={SettingNameEdit} />
    </Route>
</Route>
 
 <Route path="/admin/SettingGroupList" component={SettingGroupListWrapper} />
 
 <Route path="/admin/SettingGroupView/:id" component={SettingGroupView} />

<Route path="/admin/SettingGroupEdit" component={SettingGroupEdit}>
    <Route path="/admin/SettingGroupEdit/:id" component={SettingGroupEdit} >
        <Route path="/admin/SettingGroupEdit/:id/:parent" component={SettingGroupEdit} />
    </Route>
</Route>
   
 
  
 <Route path="/admin/PrescriptionTemplateList" component={PrescriptionTemplateListWrapper} />
 
 <Route path="/admin/PrescriptionTemplateView/:id" component={PrescriptionTemplateView} />

<Route path="/admin/PrescriptionTemplateEdit" component={PrescriptionTemplateEdit}>
    <Route path="/admin/PrescriptionTemplateEdit/:id" component={PrescriptionTemplateEdit} >
        <Route path="/admin/PrescriptionTemplateEdit/:id/:parent" component={PrescriptionTemplateEdit} />
    </Route>
</Route>
 
 <Route path="/admin/PrescriptionList" component={PrescriptionListWrapper} />
 
 <Route path="/admin/PrescriptionView/:id" component={PrescriptionView} />

<Route path="/admin/PrescriptionEdit" component={PrescriptionEdit}>
    <Route path="/admin/PrescriptionEdit/:id" component={PrescriptionEdit} >
        <Route path="/admin/PrescriptionEdit/:id/:parent" component={PrescriptionEdit} />
    </Route>
</Route>
 
 <Route path="/admin/PrescriptionItemList" component={PrescriptionItemListWrapper} />
 
 <Route path="/admin/PrescriptionItemView/:id" component={PrescriptionItemView} />

<Route path="/admin/PrescriptionItemEdit" component={PrescriptionItemEdit}>
    <Route path="/admin/PrescriptionItemEdit/:id" component={PrescriptionItemEdit} >
        <Route path="/admin/PrescriptionItemEdit/:id/:parent" component={PrescriptionItemEdit} />
    </Route>
</Route>
 
 <Route path="/admin/PrescriptionItemTemplateList" component={PrescriptionItemTemplateListWrapper} />
 
 <Route path="/admin/PrescriptionItemTemplateView/:id" component={PrescriptionItemTemplateView} />

<Route path="/admin/PrescriptionItemTemplateEdit" component={PrescriptionItemTemplateEdit}>
    <Route path="/admin/PrescriptionItemTemplateEdit/:id" component={PrescriptionItemTemplateEdit} >
        <Route path="/admin/PrescriptionItemTemplateEdit/:id/:parent" component={PrescriptionItemTemplateEdit} />
    </Route>
</Route>
 
 <Route path="/admin/FrequencyList" component={FrequencyListWrapper} />
 
 <Route path="/admin/FrequencyView/:id" component={FrequencyView} />

<Route path="/admin/FrequencyEdit" component={FrequencyEdit}>
    <Route path="/admin/FrequencyEdit/:id" component={FrequencyEdit} >
        <Route path="/admin/FrequencyEdit/:id/:parent" component={FrequencyEdit} />
    </Route>
</Route>
   
 
  
 <Route path="/admin/AtcDrugList" component={AtcDrugListWrapper} />
 
 <Route path="/admin/AtcDrugView/:id" component={AtcDrugView} />

<Route path="/admin/AtcDrugEdit" component={AtcDrugEdit}>
    <Route path="/admin/AtcDrugEdit/:id" component={AtcDrugEdit} >
        <Route path="/admin/AtcDrugEdit/:id/:parent" component={AtcDrugEdit} />
    </Route>
</Route>
 
 <Route path="/admin/DrugList" component={DrugListWrapper} />
 
 <Route path="/admin/DrugView/:id" component={DrugView} />

<Route path="/admin/DrugEdit" component={DrugEdit}>
    <Route path="/admin/DrugEdit/:id" component={DrugEdit} >
        <Route path="/admin/DrugEdit/:id/:parent" component={DrugEdit} />
    </Route>
</Route>
 
 <Route path="/admin/DrugInteractionList" component={DrugInteractionListWrapper} />
 
 <Route path="/admin/DrugInteractionView/:id" component={DrugInteractionView} />

<Route path="/admin/DrugInteractionEdit" component={DrugInteractionEdit}>
    <Route path="/admin/DrugInteractionEdit/:id" component={DrugInteractionEdit} >
        <Route path="/admin/DrugInteractionEdit/:id/:parent" component={DrugInteractionEdit} />
    </Route>
</Route>
 
 <Route path="/admin/DrugCategoryList" component={DrugCategoryListWrapper} />
 
 <Route path="/admin/DrugCategoryView/:id" component={DrugCategoryView} />

<Route path="/admin/DrugCategoryEdit" component={DrugCategoryEdit}>
    <Route path="/admin/DrugCategoryEdit/:id" component={DrugCategoryEdit} >
        <Route path="/admin/DrugCategoryEdit/:id/:parent" component={DrugCategoryEdit} />
    </Route>
</Route>
   
 
  
 <Route path="/admin/FindingList" component={FindingListWrapper} />
 
 <Route path="/admin/FindingView/:id" component={FindingView} />

<Route path="/admin/FindingEdit" component={FindingEdit}>
    <Route path="/admin/FindingEdit/:id" component={FindingEdit} >
        <Route path="/admin/FindingEdit/:id/:parent" component={FindingEdit} />
    </Route>
</Route>
 
 <Route path="/admin/PhysicalFindingList" component={PhysicalFindingListWrapper} />
 
 <Route path="/admin/PhysicalFindingView/:id" component={PhysicalFindingView} />

<Route path="/admin/PhysicalFindingEdit" component={PhysicalFindingEdit}>
    <Route path="/admin/PhysicalFindingEdit/:id" component={PhysicalFindingEdit} >
        <Route path="/admin/PhysicalFindingEdit/:id/:parent" component={PhysicalFindingEdit} />
    </Route>
</Route>
 
 <Route path="/admin/LabFindingList" component={LabFindingListWrapper} />
 
 <Route path="/admin/LabFindingView/:id" component={LabFindingView} />

<Route path="/admin/LabFindingEdit" component={LabFindingEdit}>
    <Route path="/admin/LabFindingEdit/:id" component={LabFindingEdit} >
        <Route path="/admin/LabFindingEdit/:id/:parent" component={LabFindingEdit} />
    </Route>
</Route>
 
 <Route path="/admin/DiseaseList" component={DiseaseListWrapper} />
 
 <Route path="/admin/DiseaseView/:id" component={DiseaseView} />

<Route path="/admin/DiseaseEdit" component={DiseaseEdit}>
    <Route path="/admin/DiseaseEdit/:id" component={DiseaseEdit} >
        <Route path="/admin/DiseaseEdit/:id/:parent" component={DiseaseEdit} />
    </Route>
</Route>
 
 <Route path="/admin/ConditionFindingList" component={ConditionFindingListWrapper} />
 
 <Route path="/admin/ConditionFindingView/:id" component={ConditionFindingView} />

<Route path="/admin/ConditionFindingEdit" component={ConditionFindingEdit}>
    <Route path="/admin/ConditionFindingEdit/:id" component={ConditionFindingEdit} >
        <Route path="/admin/ConditionFindingEdit/:id/:parent" component={ConditionFindingEdit} />
    </Route>
</Route>
 
 <Route path="/admin/ConditionCategoryList" component={ConditionCategoryListWrapper} />
 
 <Route path="/admin/ConditionCategoryView/:id" component={ConditionCategoryView} />

<Route path="/admin/ConditionCategoryEdit" component={ConditionCategoryEdit}>
    <Route path="/admin/ConditionCategoryEdit/:id" component={ConditionCategoryEdit} >
        <Route path="/admin/ConditionCategoryEdit/:id/:parent" component={ConditionCategoryEdit} />
    </Route>
</Route>
 
 <Route path="/admin/DifferentialDxList" component={DifferentialDxListWrapper} />
 
 <Route path="/admin/DifferentialDxView/:id" component={DifferentialDxView} />

<Route path="/admin/DifferentialDxEdit" component={DifferentialDxEdit}>
    <Route path="/admin/DifferentialDxEdit/:id" component={DifferentialDxEdit} >
        <Route path="/admin/DifferentialDxEdit/:id/:parent" component={DifferentialDxEdit} />
    </Route>
</Route>
 
 <Route path="/admin/DxCategoryList" component={DxCategoryListWrapper} />
 
 <Route path="/admin/DxCategoryView/:id" component={DxCategoryView} />

<Route path="/admin/DxCategoryEdit" component={DxCategoryEdit}>
    <Route path="/admin/DxCategoryEdit/:id" component={DxCategoryEdit} >
        <Route path="/admin/DxCategoryEdit/:id/:parent" component={DxCategoryEdit} />
    </Route>
</Route>
 
 <Route path="/admin/PatientFindingList" component={PatientFindingListWrapper} />
 
 <Route path="/admin/PatientFindingView/:id" component={PatientFindingView} />

<Route path="/admin/PatientFindingEdit" component={PatientFindingEdit}>
    <Route path="/admin/PatientFindingEdit/:id" component={PatientFindingEdit} >
        <Route path="/admin/PatientFindingEdit/:id/:parent" component={PatientFindingEdit} />
    </Route>
</Route>
 
 <Route path="/admin/PatientDiffDxList" component={PatientDiffDxListWrapper} />
 
 <Route path="/admin/PatientDiffDxView/:id" component={PatientDiffDxView} />

<Route path="/admin/PatientDiffDxEdit" component={PatientDiffDxEdit}>
    <Route path="/admin/PatientDiffDxEdit/:id" component={PatientDiffDxEdit} >
        <Route path="/admin/PatientDiffDxEdit/:id/:parent" component={PatientDiffDxEdit} />
    </Route>
</Route>
 
 <Route path="/admin/DxTestList" component={DxTestListWrapper} />
 
 <Route path="/admin/DxTestView/:id" component={DxTestView} />

<Route path="/admin/DxTestEdit" component={DxTestEdit}>
    <Route path="/admin/DxTestEdit/:id" component={DxTestEdit} >
        <Route path="/admin/DxTestEdit/:id/:parent" component={DxTestEdit} />
    </Route>
</Route>
 
 <Route path="/admin/ChronicConditionList" component={ChronicConditionListWrapper} />
 
 <Route path="/admin/ChronicConditionView/:id" component={ChronicConditionView} />

<Route path="/admin/ChronicConditionEdit" component={ChronicConditionEdit}>
    <Route path="/admin/ChronicConditionEdit/:id" component={ChronicConditionEdit} >
        <Route path="/admin/ChronicConditionEdit/:id/:parent" component={ChronicConditionEdit} />
    </Route>
</Route>
   
 
  
 <Route path="/admin/CodeList" component={CodeListWrapper} />
 
 <Route path="/admin/CodeView/:id" component={CodeView} />

<Route path="/admin/CodeEdit" component={CodeEdit}>
    <Route path="/admin/CodeEdit/:id" component={CodeEdit} >
        <Route path="/admin/CodeEdit/:id/:parent" component={CodeEdit} />
    </Route>
</Route>
 
 <Route path="/admin/ChapterList" component={ChapterListWrapper} />
 
 <Route path="/admin/ChapterView/:id" component={ChapterView} />

<Route path="/admin/ChapterEdit" component={ChapterEdit}>
    <Route path="/admin/ChapterEdit/:id" component={ChapterEdit} >
        <Route path="/admin/ChapterEdit/:id/:parent" component={ChapterEdit} />
    </Route>
</Route>
 
 <Route path="/admin/SectionList" component={SectionListWrapper} />
 
 <Route path="/admin/SectionView/:id" component={SectionView} />

<Route path="/admin/SectionEdit" component={SectionEdit}>
    <Route path="/admin/SectionEdit/:id" component={SectionEdit} >
        <Route path="/admin/SectionEdit/:id/:parent" component={SectionEdit} />
    </Route>
</Route>
 
 <Route path="/admin/SimpleCodeList" component={SimpleCodeListWrapper} />
 
 <Route path="/admin/SimpleCodeView/:id" component={SimpleCodeView} />

<Route path="/admin/SimpleCodeEdit" component={SimpleCodeEdit}>
    <Route path="/admin/SimpleCodeEdit/:id" component={SimpleCodeEdit} >
        <Route path="/admin/SimpleCodeEdit/:id/:parent" component={SimpleCodeEdit} />
    </Route>
</Route>
   
 
  
 <Route path="/admin/AppliedChartList" component={AppliedChartListWrapper} />
 
 <Route path="/admin/AppliedChartView/:id" component={AppliedChartView} />

<Route path="/admin/AppliedChartEdit" component={AppliedChartEdit}>
    <Route path="/admin/AppliedChartEdit/:id" component={AppliedChartEdit} >
        <Route path="/admin/AppliedChartEdit/:id/:parent" component={AppliedChartEdit} />
    </Route>
</Route>
 
 <Route path="/admin/ChartList" component={ChartListWrapper} />
 
 <Route path="/admin/ChartView/:id" component={ChartView} />

<Route path="/admin/ChartEdit" component={ChartEdit}>
    <Route path="/admin/ChartEdit/:id" component={ChartEdit} >
        <Route path="/admin/ChartEdit/:id/:parent" component={ChartEdit} />
    </Route>
</Route>
 
 <Route path="/admin/ChartItemList" component={ChartItemListWrapper} />
 
 <Route path="/admin/ChartItemView/:id" component={ChartItemView} />

<Route path="/admin/ChartItemEdit" component={ChartItemEdit}>
    <Route path="/admin/ChartItemEdit/:id" component={ChartItemEdit} >
        <Route path="/admin/ChartItemEdit/:id/:parent" component={ChartItemEdit} />
    </Route>
</Route>
 
 <Route path="/admin/ChartProcedureList" component={ChartProcedureListWrapper} />
 
 <Route path="/admin/ChartProcedureView/:id" component={ChartProcedureView} />

<Route path="/admin/ChartProcedureEdit" component={ChartProcedureEdit}>
    <Route path="/admin/ChartProcedureEdit/:id" component={ChartProcedureEdit} >
        <Route path="/admin/ChartProcedureEdit/:id/:parent" component={ChartProcedureEdit} />
    </Route>
</Route>
   
 
  
 <Route path="/admin/InvoiceList" component={InvoiceListWrapper} />
 
 <Route path="/admin/InvoiceView/:id" component={InvoiceView} />

<Route path="/admin/InvoiceEdit" component={InvoiceEdit}>
    <Route path="/admin/InvoiceEdit/:id" component={InvoiceEdit} >
        <Route path="/admin/InvoiceEdit/:id/:parent" component={InvoiceEdit} />
    </Route>
</Route>
 
 <Route path="/admin/ServiceList" component={ServiceListWrapper} />
 
 <Route path="/admin/ServiceView/:id" component={ServiceView} />

<Route path="/admin/ServiceEdit" component={ServiceEdit}>
    <Route path="/admin/ServiceEdit/:id" component={ServiceEdit} >
        <Route path="/admin/ServiceEdit/:id/:parent" component={ServiceEdit} />
    </Route>
</Route>
 
 <Route path="/admin/InvoiceItemList" component={InvoiceItemListWrapper} />
 
 <Route path="/admin/InvoiceItemView/:id" component={InvoiceItemView} />

<Route path="/admin/InvoiceItemEdit" component={InvoiceItemEdit}>
    <Route path="/admin/InvoiceItemEdit/:id" component={InvoiceItemEdit} >
        <Route path="/admin/InvoiceItemEdit/:id/:parent" component={InvoiceItemEdit} />
    </Route>
</Route>
   
 
  
 <Route path="/admin/AppointmentList" component={AppointmentListWrapper} />
 
 <Route path="/admin/AppointmentView/:id" component={AppointmentView} />

<Route path="/admin/AppointmentEdit" component={AppointmentEdit}>
    <Route path="/admin/AppointmentEdit/:id" component={AppointmentEdit} >
        <Route path="/admin/AppointmentEdit/:id/:parent" component={AppointmentEdit} />
    </Route>
</Route>
   
 
  
 <Route path="/admin/AdmissionList" component={AdmissionListWrapper} />
 
 <Route path="/admin/AdmissionView/:id" component={AdmissionView} />

<Route path="/admin/AdmissionEdit" component={AdmissionEdit}>
    <Route path="/admin/AdmissionEdit/:id" component={AdmissionEdit} >
        <Route path="/admin/AdmissionEdit/:id/:parent" component={AdmissionEdit} />
    </Route>
</Route>
 
 <Route path="/admin/BedStayList" component={BedStayListWrapper} />
 
 <Route path="/admin/BedStayView/:id" component={BedStayView} />

<Route path="/admin/BedStayEdit" component={BedStayEdit}>
    <Route path="/admin/BedStayEdit/:id" component={BedStayEdit} >
        <Route path="/admin/BedStayEdit/:id/:parent" component={BedStayEdit} />
    </Route>
</Route>
   
 
  
 <Route path="/admin/EmployeeList" component={EmployeeListWrapper} />
 
 <Route path="/admin/EmployeeView/:id" component={EmployeeView} />

<Route path="/admin/EmployeeEdit" component={EmployeeEdit}>
    <Route path="/admin/EmployeeEdit/:id" component={EmployeeEdit} >
        <Route path="/admin/EmployeeEdit/:id/:parent" component={EmployeeEdit} />
    </Route>
</Route>
   
 
  
 <Route path="/admin/OrderTemplateList" component={OrderTemplateListWrapper} />
 
 <Route path="/admin/OrderTemplateView/:id" component={OrderTemplateView} />

<Route path="/admin/OrderTemplateEdit" component={OrderTemplateEdit}>
    <Route path="/admin/OrderTemplateEdit/:id" component={OrderTemplateEdit} >
        <Route path="/admin/OrderTemplateEdit/:id/:parent" component={OrderTemplateEdit} />
    </Route>
</Route>
 
 <Route path="/admin/OrderList" component={OrderListWrapper} />
 
 <Route path="/admin/OrderView/:id" component={OrderView} />

<Route path="/admin/OrderEdit" component={OrderEdit}>
    <Route path="/admin/OrderEdit/:id" component={OrderEdit} >
        <Route path="/admin/OrderEdit/:id/:parent" component={OrderEdit} />
    </Route>
</Route>
   
 
	 