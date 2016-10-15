

import * as React from 'react';
import * as ReactDOM from 'react-dom';

import BaseCrudComponent from '../commons/BaseComponent';
import AppState from '../commons/AppState';
import LookupService  from '../commons/LookupService';


export function createSchema(){ 
 
 return {
    title: "Encounter",
    type: "object",
    required: [ 
],
    properties: {
    

reason:{ type: "string", title: "Reason",  	
},



patient:{ type: "integer", title: "Patient",   

 'enum': LookupService.getLookup('patients').map(x => x.id   ),
 'enumNames': LookupService.getLookup('patients').map(x => x.displayName)


	
},



labTests:{ type: "array", title: "Lab Tests",   

    "items":{
 'enum': LookupService.getLookup('labTests').map(x => x.id .toString()  ),
 'enumNames': LookupService.getLookup('labTests').map(x => x.displayName)
    },
    "uniqueItems": true

	
},



prescription:{ type: "integer", title: "Prescription",   

 'enum': LookupService.getLookup('prescriptions').map(x => x.id   ),
 'enumNames': LookupService.getLookup('prescriptions').map(x => x.displayName)


	
},



admission:{ type: "integer", title: "Admission",   

 'enum': LookupService.getLookup('admissions').map(x => x.id   ),
 'enumNames': LookupService.getLookup('admissions').map(x => x.displayName)


	
},


    
    }
 };

}

export const encounterUISchema = {
 	

reason: { 'ui:widget': "textarea" , 'ui:placeholder': "Reason" },



patient: {  'ui:placeholder': "Patient" },



labTests: {  'ui:placeholder': "Lab Tests" },



prescription: {  'ui:placeholder': "Prescription" },



admission: {  'ui:placeholder': "Admission" },


    
 }







export const encounterHeaders = [
 
 
 {property:"reason",title:"Reason" }
 ,
 
 {property:"patient_displayName",title:"Patient" }
 ,
 
 {property:"prescription_displayName",title:"Prescription" }
 ,
 
 {property:"admission_displayName",title:"Admission" }
      
 ]

export class EncounterStore extends AppState {
    constructor(url: string, headers: any, formSchema: any, uiSchema: any) {
        super(url, headers, formSchema, uiSchema);
    }
}

export default class EncounterWrapper extends React.Component<any, any> {

    data = new EncounterStore('encounters', encounterHeaders,
    createSchema(), encounterUISchema);

    render() {
        return (
            <BaseCrudComponent data={this.data} />
        );
    }
}

