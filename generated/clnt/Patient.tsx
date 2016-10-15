

import * as React from 'react';
import * as ReactDOM from 'react-dom';

import BaseCrudComponent from '../commons/BaseComponent';
import AppState from '../commons/AppState';
import LookupService  from '../commons/LookupService';


export function createSchema(){ 
 
 return {
    title: "Patient",
    type: "object",
    required: [  'firstName' , 'lastName' 
],
    properties: {
    

firstName:{ type: "string", title: "First Name",  	
},



lastName:{ type: "string", title: "Last Name",  	
},



customerType:{ type: "string", title: "Customer Type",   
'enum' : [
'','0' ,'1' ,'2'   
],
'enumNames' : [
'Select','BRONZE' ,'SILVER' ,'GOLD'   
]
	
},



encounter:{ type: "integer", title: "Encounter",   

 'enum': LookupService.getLookup('encounters').map(x => x.id   ),
 'enumNames': LookupService.getLookup('encounters').map(x => x.displayName)


	
},



vaccination:{ type: "integer", title: "Vaccination",   

 'enum': LookupService.getLookup('vaccinations').map(x => x.id   ),
 'enumNames': LookupService.getLookup('vaccinations').map(x => x.displayName)


	
},



testResults:{ type: "integer", title: "Test Results",   

 'enum': LookupService.getLookup('testResultses').map(x => x.id   ),
 'enumNames': LookupService.getLookup('testResultses').map(x => x.displayName)


	
},


    
    }
 };

}

export const patientUISchema = {
 	

firstName: {  'ui:placeholder': "First Name" },



lastName: {  'ui:placeholder': "Last Name" },



customerType: {  'ui:placeholder': "Customer Type" },



encounter: {  'ui:placeholder': "Encounter" },



vaccination: {  'ui:placeholder': "Vaccination" },



testResults: {  'ui:placeholder': "Test Results" },


    
 }







export const patientHeaders = [
 
 
 {property:"firstName",title:"First Name" }
 ,
 
 {property:"lastName",title:"Last Name" }
 ,
 
 {property:"customerType",title:"Customer Type" }
      
 ]

export class PatientStore extends AppState {
    constructor(url: string, headers: any, formSchema: any, uiSchema: any) {
        super(url, headers, formSchema, uiSchema);
    }
}

export default class PatientWrapper extends React.Component<any, any> {

    data = new PatientStore('patients', patientHeaders,
    createSchema(), patientUISchema);

    render() {
        return (
            <BaseCrudComponent data={this.data} />
        );
    }
}

