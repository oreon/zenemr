

import * as React from 'react';
import * as ReactDOM from 'react-dom';

import BaseCrudComponent from '../commons/BaseComponent';
import AppState from '../commons/AppState';
import LookupService  from '../commons/LookupService';


export function createSchema(){ 
 
 return {
    title: "Admission",
    type: "object",
    required: [ 
],
    properties: {
    

admissionNote:{ type: "string", title: "Admission Note",  	
},



dischargeDate:{ type: "string", title: "Discharge Date",   "format": "date"	
},



dischargeNote:{ type: "string", title: "Discharge Note",  	
},



dischargeCode:{ type: "string", title: "Discharge Code",   
'enum' : [
'','0' ,'1' ,'2'   
],
'enumNames' : [
'Select','Deceased' ,'Referred' ,'Normal'   
]
	
},



currentBed:{ type: "string", title: "Current Bed",  	
},



isCurrent:{ type: "boolean", title: "Is Current",  	
},



invoice:{ type: "integer", title: "Invoice",   

 'enum': LookupService.getLookup('invoices').map(x => x.id   ),
 'enumNames': LookupService.getLookup('invoices').map(x => x.displayName)


	
},



encounter:{ type: "integer", title: "Encounter",   

 'enum': LookupService.getLookup('encounters').map(x => x.id   ),
 'enumNames': LookupService.getLookup('encounters').map(x => x.displayName)


	
},


    
bedStays: {
            title: "Bed Stays",
            type: "array",
            required: [
],
            items: {
                "type": "object",
                "properties": {
                 

fromDate:{ type: "string", title: "From Date",   "format": "date"	
},



toDate:{ type: "string", title: "To Date",   "format": "date"	
},


  
admission: {
      "type": "number",
    },

 
                 
                }
            }
        },

    }
 };

}

export const admissionUISchema = {
 	

admissionNote: { 'ui:widget': "textarea" , 'ui:placeholder': "Admission Note" },



dischargeDate: {  'ui:placeholder': "Discharge Date" },



dischargeNote: { 'ui:widget': "textarea" , 'ui:placeholder': "Discharge Note" },



dischargeCode: {  'ui:placeholder': "Discharge Code" },



currentBed: {  'ui:placeholder': "Current Bed" },



isCurrent: {  'ui:placeholder': "Is Current" },



invoice: {  'ui:placeholder': "Invoice" },



encounter: {  'ui:placeholder': "Encounter" },


    
bedStays: {
 	items:{
         

fromDate: {  'ui:placeholder': "From Date" },



toDate: {  'ui:placeholder': "To Date" },


  
admission: {
      "ui:widget": "hidden"
    },

 
         
     }
 },

 }







export const admissionHeaders = [
 
 
 {property:"admissionNote",title:"Admission Note" }
 ,
 
 {property:"dischargeDate",title:"Discharge Date" }
 ,
 
 {property:"dischargeNote",title:"Discharge Note" }
 ,
 
 {property:"dischargeCode",title:"Discharge Code" }
 ,
 
 {property:"currentBed",title:"Current Bed" }
 ,
 
 {property:"isCurrent",title:"Is Current" }
 ,
 
 {property:"invoice_displayName",title:"Invoice" }
      
 ]

export class AdmissionStore extends AppState {
    constructor(url: string, headers: any, formSchema: any, uiSchema: any) {
        super(url, headers, formSchema, uiSchema);
    }
}

export default class AdmissionWrapper extends React.Component<any, any> {

    data = new AdmissionStore('admissions', admissionHeaders,
    createSchema(), admissionUISchema);

    render() {
        return (
            <BaseCrudComponent data={this.data} />
        );
    }
}

