

import * as React from 'react';
import * as ReactDOM from 'react-dom';

import BaseCrudComponent from '../commons/BaseComponent';
import AppState from '../commons/AppState';
import LookupService  from '../commons/LookupService';


export function createSchema(){ 
 
 return {
    title: "Prescription",
    type: "object",
    required: [ 
],
    properties: {
    

active:{ type: "boolean", title: "Active",  	
},



directivesForPatient:{ type: "string", title: "Directives For Patient",  	
},



drugs:{ type: "string", title: "Drugs",  	
},



startDate:{ type: "string", title: "Start Date",   "format": "date"	
},



endDate:{ type: "string", title: "End Date",   "format": "date"	
},



encounter:{ type: "integer", title: "Encounter",   

 'enum': LookupService.getLookup('encounters').map(x => x.id   ),
 'enumNames': LookupService.getLookup('encounters').map(x => x.displayName)


	
},


    
prescriptionItems: {
            title: "Prescription Items",
            type: "array",
            required: [ 'qty' , 'strength' , 'duration' 
],
            items: {
                "type": "object",
                "properties": {
                 

drug:{ type: "integer", title: "Drug",   

 'enum': LookupService.getLookup('drugs').map(x => x.id   ),
 'enumNames': LookupService.getLookup('drugs').map(x => x.displayName)


	
},



qty:{ type: "number", title: "Qty",  	
},



strength:{ type: "string", title: "Strength",  	
},


  
prescription: {
      "type": "number",
    },



route:{ type: "string", title: "Route",   
'enum' : [
'','0' ,'1' ,'2' ,'3' ,'4'   
],
'enumNames' : [
'Select','PO' ,'IV' ,'IM' ,'SC' ,'TOPICAL'   
]
	
},



duration:{ type: "integer", title: "Duration",  	
},



frequency:{ type: "integer", title: "Frequency",   

 'enum': LookupService.getLookup('frequencys').map(x => x.id   ),
 'enumNames': LookupService.getLookup('frequencys').map(x => x.displayName)


	
},



remarks:{ type: "string", title: "Remarks",  	
},



brandName:{ type: "string", title: "Brand Name",  	
},

 
                 
                }
            }
        },

    }
 };

}

export const prescriptionUISchema = {
 	

active: {  'ui:placeholder': "Active" },



directivesForPatient: { 'ui:widget': "textarea" , 'ui:placeholder': "Directives For Patient" },



drugs: {  'ui:placeholder': "Drugs" },



startDate: {  'ui:placeholder': "Start Date" },



endDate: {  'ui:placeholder': "End Date" },



encounter: {  'ui:placeholder': "Encounter" },


    
prescriptionItems: {
 	items:{
         

drug: {  'ui:placeholder': "Drug" },



qty: {  'ui:placeholder': "Qty" },



strength: {  'ui:placeholder': "Strength" },


  
prescription: {
      "ui:widget": "hidden"
    },



route: {  'ui:placeholder': "Route" },



duration: { 'ui:widget': "updown" , 'ui:placeholder': "Duration" },



frequency: {  'ui:placeholder': "Frequency" },



remarks: {  'ui:placeholder': "Remarks" },



brandName: {  'ui:placeholder': "Brand Name" },

 
         
     }
 },

 }







export const prescriptionHeaders = [
 
 
 {property:"active",title:"Active" }
 ,
 
 {property:"directivesForPatient",title:"Directives For Patient" }
 ,
 
 {property:"drugs",title:"Drugs" }
 ,
 
 {property:"startDate",title:"Start Date" }
 ,
 
 {property:"endDate",title:"End Date" }
 ,
 
 {property:"encounter_displayName",title:"Encounter" }
      
 ]

export class PrescriptionStore extends AppState {
    constructor(url: string, headers: any, formSchema: any, uiSchema: any) {
        super(url, headers, formSchema, uiSchema);
    }
}

export default class PrescriptionWrapper extends React.Component<any, any> {

    data = new PrescriptionStore('prescriptions', prescriptionHeaders,
    createSchema(), prescriptionUISchema);

    render() {
        return (
            <BaseCrudComponent data={this.data} />
        );
    }
}

