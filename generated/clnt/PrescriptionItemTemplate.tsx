

import * as React from 'react';
import * as ReactDOM from 'react-dom';

import BaseCrudComponent from '../commons/BaseComponent';
import AppState from '../commons/AppState';
import LookupService  from '../commons/LookupService';


export function createSchema(){ 
 
 return {
    title: "Prescription Item Template",
    type: "object",
    required: [ 
],
    properties: {
    

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
 };

}

export const prescriptionItemTemplateUISchema = {
 	

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







export const prescriptionItemTemplateHeaders = [
 
 
 {property:"drug_displayName",title:"Drug" }
 ,
 
 {property:"qty",title:"Qty" }
 ,
 
 {property:"frequency_displayName",title:"Frequency" }
 ,
 
 {property:"strength",title:"Strength" }
 ,
 
 {property:"route",title:"Route" }
 ,
 
 {property:"duration",title:"Duration" }
 ,
 
 {property:"remarks",title:"Remarks" }
 ,
 
 {property:"brandName",title:"Brand Name" }
 ,
 
 {property:"prescriptionTemplate_displayName",title:"Prescription Template" }
      
 ]

export class PrescriptionItemTemplateStore extends AppState {
    constructor(url: string, headers: any, formSchema: any, uiSchema: any) {
        super(url, headers, formSchema, uiSchema);
    }
}

export default class PrescriptionItemTemplateWrapper extends React.Component<any, any> {

    data = new PrescriptionItemTemplateStore('prescriptionItemTemplates', prescriptionItemTemplateHeaders,
    createSchema(), prescriptionItemTemplateUISchema);

    render() {
        return (
            <BaseCrudComponent data={this.data} />
        );
    }
}

