

import * as React from 'react';
import * as ReactDOM from 'react-dom';

import BaseCrudComponent from '../commons/BaseComponent';
import AppState from '../commons/AppState';
import LookupService  from '../commons/LookupService';


export function createSchema(){ 
 
 return {
    title: "Patient Diff Dx",
    type: "object",
    required: [ 
],
    properties: {
    

notes:{ type: "string", title: "Notes",  	
},


    
patientFindings: {
            title: "Patient Findings",
            type: "array",
            required: [
],
            items: {
                "type": "object",
                "properties": {
                 

finding:{ type: "integer", title: "Finding",   

 'enum': LookupService.getLookup('findings').map(x => x.id   ),
 'enumNames': LookupService.getLookup('findings').map(x => x.displayName)


	
},


  
patientDiffDx: {
      "type": "number",
    },

 
                 
                }
            }
        },

    }
 };

}

export const patientDiffDxUISchema = {
 	

notes: { 'ui:widget': "textarea" , 'ui:placeholder': "Notes" },


    
patientFindings: {
 	items:{
         

finding: {  'ui:placeholder': "Finding" },


  
patientDiffDx: {
      "ui:widget": "hidden"
    },

 
         
     }
 },

 }







export const patientDiffDxHeaders = [
 
 
 {property:"notes",title:"Notes" }
      
 ]

export class PatientDiffDxStore extends AppState {
    constructor(url: string, headers: any, formSchema: any, uiSchema: any) {
        super(url, headers, formSchema, uiSchema);
    }
}

export default class PatientDiffDxWrapper extends React.Component<any, any> {

    data = new PatientDiffDxStore('patientDiffDxs', patientDiffDxHeaders,
    createSchema(), patientDiffDxUISchema);

    render() {
        return (
            <BaseCrudComponent data={this.data} />
        );
    }
}

