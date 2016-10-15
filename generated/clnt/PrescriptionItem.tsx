

import * as React from 'react';
import * as ReactDOM from 'react-dom';

import BaseCrudComponent from '../commons/BaseComponent';
import AppState from '../commons/AppState';
import LookupService  from '../commons/LookupService';


export function createSchema(){ 
 
 return {
    title: "Prescription Item",
    type: "object",
    required: [  'qty' , 'strength' , 'duration' 
],
    properties: {
    

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
 };

}

export const prescriptionItemUISchema = {
 	

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







export const prescriptionItemHeaders = [
 
 
 {property:"drug_displayName",title:"Drug" }
 ,
 
 {property:"qty",title:"Qty" }
 ,
 
 {property:"strength",title:"Strength" }
 ,
 
 {property:"prescription_displayName",title:"Prescription" }
 ,
 
 {property:"route",title:"Route" }
 ,
 
 {property:"duration",title:"Duration" }
 ,
 
 {property:"frequency_displayName",title:"Frequency" }
 ,
 
 {property:"remarks",title:"Remarks" }
 ,
 
 {property:"brandName",title:"Brand Name" }
      
 ]

export class PrescriptionItemStore extends AppState {
    constructor(url: string, headers: any, formSchema: any, uiSchema: any) {
        super(url, headers, formSchema, uiSchema);
    }
}

export default class PrescriptionItemWrapper extends React.Component<any, any> {

    data = new PrescriptionItemStore('prescriptionItems', prescriptionItemHeaders,
    createSchema(), prescriptionItemUISchema);

    render() {
        return (
            <BaseCrudComponent data={this.data} />
        );
    }
}

