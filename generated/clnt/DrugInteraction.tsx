

import * as React from 'react';
import * as ReactDOM from 'react-dom';

import BaseCrudComponent from '../commons/BaseComponent';
import AppState from '../commons/AppState';
import LookupService  from '../commons/LookupService';


export function createSchema(){ 
 
 return {
    title: "Drug Interaction",
    type: "object",
    required: [ 
],
    properties: {
    

description:{ type: "string", title: "Description",  	
},


  
drug: {
      "type": "number",
    },



interactingDrug:{ type: "integer", title: "Interacting Drug",   

 'enum': LookupService.getLookup('drugs').map(x => x.id   ),
 'enumNames': LookupService.getLookup('drugs').map(x => x.displayName)


	
},



severity:{ type: "string", title: "Severity",   
'enum' : [
'','0' ,'1' ,'2'   
],
'enumNames' : [
'Select','MILD' ,'MODERATE' ,'SEVERE'   
]
	
},


    
    }
 };

}

export const drugInteractionUISchema = {
 	

description: { 'ui:widget': "textarea" , 'ui:placeholder': "Description" },


  
drug: {
      "ui:widget": "hidden"
    },



interactingDrug: {  'ui:placeholder': "Interacting Drug" },



severity: {  'ui:placeholder': "Severity" },


    
 }







export const drugInteractionHeaders = [
 
 
 {property:"description",title:"Description" }
 ,
 
 {property:"drug_displayName",title:"Drug" }
 ,
 
 {property:"interactingDrug_displayName",title:"Interacting Drug" }
 ,
 
 {property:"severity",title:"Severity" }
      
 ]

export class DrugInteractionStore extends AppState {
    constructor(url: string, headers: any, formSchema: any, uiSchema: any) {
        super(url, headers, formSchema, uiSchema);
    }
}

export default class DrugInteractionWrapper extends React.Component<any, any> {

    data = new DrugInteractionStore('drugInteractions', drugInteractionHeaders,
    createSchema(), drugInteractionUISchema);

    render() {
        return (
            <BaseCrudComponent data={this.data} />
        );
    }
}

