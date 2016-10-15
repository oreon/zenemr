

import * as React from 'react';
import * as ReactDOM from 'react-dom';

import BaseCrudComponent from '../commons/BaseComponent';
import AppState from '../commons/AppState';
import LookupService  from '../commons/LookupService';


export function createSchema(){ 
 
 return {
    title: "Prescription Template",
    type: "object",
    required: [  'name' 
],
    properties: {
    

name:{ type: "string", title: "Name",  	
},



directivesForPatient:{ type: "string", title: "Directives For Patient",  	
},


    
prescriptionItemTemplates: {
            title: "Prescription Item Templates",
            type: "array",
            required: [
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



frequency:{ type: "integer", title: "Frequency",   

 'enum': LookupService.getLookup('frequencys').map(x => x.id   ),
 'enumNames': LookupService.getLookup('frequencys').map(x => x.displayName)


	
},



strength:{ type: "string", title: "Strength",  	
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



remarks:{ type: "string", title: "Remarks",  	
},



brandName:{ type: "string", title: "Brand Name",  	
},


  
prescriptionTemplate: {
      "type": "number",
    },

 
                 
                }
            }
        },

    }
 };

}

export const prescriptionTemplateUISchema = {
 	

name: {  'ui:placeholder': "Name" },



directivesForPatient: { 'ui:widget': "textarea" , 'ui:placeholder': "Directives For Patient" },


    
prescriptionItemTemplates: {
 	items:{
         

drug: {  'ui:placeholder': "Drug" },



qty: {  'ui:placeholder': "Qty" },



frequency: {  'ui:placeholder': "Frequency" },



strength: {  'ui:placeholder': "Strength" },



route: {  'ui:placeholder': "Route" },



duration: { 'ui:widget': "updown" , 'ui:placeholder': "Duration" },



remarks: {  'ui:placeholder': "Remarks" },



brandName: {  'ui:placeholder': "Brand Name" },


  
prescriptionTemplate: {
      "ui:widget": "hidden"
    },

 
         
     }
 },

 }







export const prescriptionTemplateHeaders = [
 
 
 {property:"name",title:"Name" }
 ,
 
 {property:"directivesForPatient",title:"Directives For Patient" }
      
 ]

export class PrescriptionTemplateStore extends AppState {
    constructor(url: string, headers: any, formSchema: any, uiSchema: any) {
        super(url, headers, formSchema, uiSchema);
    }
}

export default class PrescriptionTemplateWrapper extends React.Component<any, any> {

    data = new PrescriptionTemplateStore('prescriptionTemplates', prescriptionTemplateHeaders,
    createSchema(), prescriptionTemplateUISchema);

    render() {
        return (
            <BaseCrudComponent data={this.data} />
        );
    }
}

