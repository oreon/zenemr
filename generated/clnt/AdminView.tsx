
	 import * as React from 'react';
	import * as ReactDOM from 'react-dom';
	import { Router, Route, hashHistory, Link  } from 'react-router'

export class AdminView extends React.Component<{}, {}> {
  render() {
    return (
      <div>
	 	
  <h1> domain </h1>
  <ul> 
  
   </ul>
   <hr/>
 
  <h1> users </h1>
  <ul> 
  
  <li><Link to="/admin/AppUserList">AppUser</Link></li>
   
  <li><Link to="/admin/AppRoleList">AppRole</Link></li>
   
  <li><Link to="/admin/GroupList">Group</Link></li>
   
   </ul>
   <hr/>
 
  <h1> patients </h1>
  <ul> 
  
  <li><Link to="/admin/PatientList">Patient</Link></li>
   
  <li><Link to="/admin/VaccinationList">Vaccination</Link></li>
   
  <li><Link to="/admin/EncounterList">Encounter</Link></li>
   
  <li><Link to="/admin/VaccineList">Vaccine</Link></li>
   
  <li><Link to="/admin/LabTestList">LabTest</Link></li>
   
  <li><Link to="/admin/TestResultsList">TestResults</Link></li>
   
  <li><Link to="/admin/ResultRowList">ResultRow</Link></li>
   
   </ul>
   <hr/>
 
  <h1> facility </h1>
  <ul> 
  
  <li><Link to="/admin/FacilityList">Facility</Link></li>
   
  <li><Link to="/admin/RoomList">Room</Link></li>
   
  <li><Link to="/admin/BedList">Bed</Link></li>
   
  <li><Link to="/admin/WardList">Ward</Link></li>
   
  <li><Link to="/admin/RoomTypeList">RoomType</Link></li>
   
   </ul>
   <hr/>
 
  <h1> unusualoccurences </h1>
  <ul> 
  
  <li><Link to="/admin/UnusualOccurenceList">UnusualOccurence</Link></li>
   
  <li><Link to="/admin/OccurenceTypeList">OccurenceType</Link></li>
   
   </ul>
   <hr/>
 
  <h1> settings </h1>
  <ul> 
  
  <li><Link to="/admin/SettingsList">Settings</Link></li>
   
  <li><Link to="/admin/SettingList">Setting</Link></li>
   
  <li><Link to="/admin/SettingNameList">SettingName</Link></li>
   
  <li><Link to="/admin/SettingGroupList">SettingGroup</Link></li>
   
   </ul>
   <hr/>
 
  <h1> prescription </h1>
  <ul> 
  
  <li><Link to="/admin/PrescriptionTemplateList">PrescriptionTemplate</Link></li>
   
  <li><Link to="/admin/PrescriptionList">Prescription</Link></li>
   
  <li><Link to="/admin/PrescriptionItemList">PrescriptionItem</Link></li>
   
  <li><Link to="/admin/PrescriptionItemTemplateList">PrescriptionItemTemplate</Link></li>
   
  <li><Link to="/admin/FrequencyList">Frequency</Link></li>
   
   </ul>
   <hr/>
 
  <h1> drugs </h1>
  <ul> 
  
  <li><Link to="/admin/AtcDrugList">AtcDrug</Link></li>
   
  <li><Link to="/admin/DrugList">Drug</Link></li>
   
  <li><Link to="/admin/DrugInteractionList">DrugInteraction</Link></li>
   
  <li><Link to="/admin/DrugCategoryList">DrugCategory</Link></li>
   
   </ul>
   <hr/>
 
  <h1> ddx </h1>
  <ul> 
  
  <li><Link to="/admin/FindingList">Finding</Link></li>
   
  <li><Link to="/admin/PhysicalFindingList">PhysicalFinding</Link></li>
   
  <li><Link to="/admin/LabFindingList">LabFinding</Link></li>
   
  <li><Link to="/admin/DiseaseList">Disease</Link></li>
   
  <li><Link to="/admin/ConditionFindingList">ConditionFinding</Link></li>
   
  <li><Link to="/admin/ConditionCategoryList">ConditionCategory</Link></li>
   
  <li><Link to="/admin/DifferentialDxList">DifferentialDx</Link></li>
   
  <li><Link to="/admin/DxCategoryList">DxCategory</Link></li>
   
  <li><Link to="/admin/PatientFindingList">PatientFinding</Link></li>
   
  <li><Link to="/admin/PatientDiffDxList">PatientDiffDx</Link></li>
   
  <li><Link to="/admin/DxTestList">DxTest</Link></li>
   
  <li><Link to="/admin/ChronicConditionList">ChronicCondition</Link></li>
   
   </ul>
   <hr/>
 
  <h1> codes </h1>
  <ul> 
  
  <li><Link to="/admin/CodeList">Code</Link></li>
   
  <li><Link to="/admin/ChapterList">Chapter</Link></li>
   
  <li><Link to="/admin/SectionList">Section</Link></li>
   
  <li><Link to="/admin/SimpleCodeList">SimpleCode</Link></li>
   
   </ul>
   <hr/>
 
  <h1> charts </h1>
  <ul> 
  
  <li><Link to="/admin/AppliedChartList">AppliedChart</Link></li>
   
  <li><Link to="/admin/ChartList">Chart</Link></li>
   
  <li><Link to="/admin/ChartItemList">ChartItem</Link></li>
   
  <li><Link to="/admin/ChartProcedureList">ChartProcedure</Link></li>
   
   </ul>
   <hr/>
 
  <h1> billing </h1>
  <ul> 
  
  <li><Link to="/admin/InvoiceList">Invoice</Link></li>
   
  <li><Link to="/admin/ServiceList">Service</Link></li>
   
  <li><Link to="/admin/InvoiceItemList">InvoiceItem</Link></li>
   
   </ul>
   <hr/>
 
  <h1> appointment </h1>
  <ul> 
  
  <li><Link to="/admin/AppointmentList">Appointment</Link></li>
   
   </ul>
   <hr/>
 
  <h1> admission </h1>
  <ul> 
  
  <li><Link to="/admin/AdmissionList">Admission</Link></li>
   
  <li><Link to="/admin/BedStayList">BedStay</Link></li>
   
   </ul>
   <hr/>
 
  <h1> employees </h1>
  <ul> 
  
  <li><Link to="/admin/EmployeeList">Employee</Link></li>
   
   </ul>
   <hr/>
 
  <h1> physicianOrder </h1>
  <ul> 
  
  <li><Link to="/admin/OrderTemplateList">OrderTemplate</Link></li>
   
  <li><Link to="/admin/OrderList">Order</Link></li>
   
   </ul>
   <hr/>
 
	  </div>
	 )}
}	 
 