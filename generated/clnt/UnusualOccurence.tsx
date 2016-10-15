

import * as React from 'react';
import * as ReactDOM from 'react-dom';

import BaseCrudComponent from '../commons/BaseComponent';
import AppState from '../commons/AppState';
import LookupService  from '../commons/LookupService';


export function createSchema(){ 
 
 return {
    title: "Unusual Occurence",
    type: "object",
    required: [ 
],
    properties: {
    

occurenceType:{ type: "integer", title: "Occurence Type",   

 'enum': LookupService.getLookup('occurenceTypes').map(x => x.id   ),
 'enumNames': LookupService.getLookup('occurenceTypes').map(x => x.displayName)


	
},



category:{ type: "string", title: "Category",   
'enum' : [
'','0' ,'1' ,'2' ,'3' ,'4'   
],
'enumNames' : [
'Select','Radiation' ,'Chemotherapy' ,'Anesthesia' ,'Surgery' ,'Other'   
]
	
},



severity:{ type: "string", title: "Severity",   
'enum' : [
'','0' ,'1' ,'2'   
],
'enumNames' : [
'Select','Mild' ,'Moderate' ,'Critical'   
]
	
},



description:{ type: "string", title: "Description",  	
},


    
    }
 };

}

export const unusualOccurenceUISchema = {
 	

occurenceType: {  'ui:placeholder': "Occurence Type" },



category: {  'ui:placeholder': "Category" },



severity: {  'ui:placeholder': "Severity" },



description: { 'ui:widget': "textarea" , 'ui:placeholder': "Description" },


    
 }







export const unusualOccurenceHeaders = [
 
 
 {property:"occurenceType_displayName",title:"Occurence Type" }
 ,
 
 {property:"category",title:"Category" }
 ,
 
 {property:"severity",title:"Severity" }
 ,
 
 {property:"description",title:"Description" }
      
 ]

export class UnusualOccurenceStore extends AppState {
    constructor(url: string, headers: any, formSchema: any, uiSchema: any) {
        super(url, headers, formSchema, uiSchema);
    }
}

export default class UnusualOccurenceWrapper extends React.Component<any, any> {

    data = new UnusualOccurenceStore('unusualOccurences', unusualOccurenceHeaders,
    createSchema(), unusualOccurenceUISchema);

    render() {
        return (
            <BaseCrudComponent data={this.data} />
        );
    }
}

