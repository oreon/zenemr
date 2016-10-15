

import * as React from 'react';
import * as ReactDOM from 'react-dom';

import BaseCrudComponent from '../commons/BaseComponent';
import AppState from '../commons/AppState';
import LookupService  from '../commons/LookupService';


export function createSchema(){ 
 
 return {
    title: "Patient Finding",
    type: "object",
    required: [ 
],
    properties: {
    

finding:{ type: "integer", title: "Finding",   

 'enum': LookupService.getLookup('findings').map(x => x.id   ),
 'enumNames': LookupService.getLookup('findings').map(x => x.displayName)


	
},


  
patientDiffDx: {
      "type": "number",
    },


    
    }
 };

}

export const patientFindingUISchema = {
 	

finding: {  'ui:placeholder': "Finding" },


  
patientDiffDx: {
      "ui:widget": "hidden"
    },


    
 }







export const patientFindingHeaders = [
 
 
 {property:"finding_displayName",title:"Finding" }
 ,
 
 {property:"patientDiffDx_displayName",title:"Patient Diff Dx" }
      
 ]

export class PatientFindingStore extends AppState {
    constructor(url: string, headers: any, formSchema: any, uiSchema: any) {
        super(url, headers, formSchema, uiSchema);
    }
}

export default class PatientFindingWrapper extends React.Component<any, any> {

    data = new PatientFindingStore('patientFindings', patientFindingHeaders,
    createSchema(), patientFindingUISchema);

    render() {
        return (
            <BaseCrudComponent data={this.data} />
        );
    }
}

