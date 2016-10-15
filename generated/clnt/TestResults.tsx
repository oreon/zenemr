

import * as React from 'react';
import * as ReactDOM from 'react-dom';

import BaseCrudComponent from '../commons/BaseComponent';
import AppState from '../commons/AppState';
import LookupService  from '../commons/LookupService';


export function createSchema(){ 
 
 return {
    title: "Test Results",
    type: "object",
    required: [ 
],
    properties: {
    

patient:{ type: "integer", title: "Patient",   

 'enum': LookupService.getLookup('patients').map(x => x.id   ),
 'enumNames': LookupService.getLookup('patients').map(x => x.displayName)


	
},



labTest:{ type: "integer", title: "Lab Test",   

 'enum': LookupService.getLookup('labTests').map(x => x.id   ),
 'enumNames': LookupService.getLookup('labTests').map(x => x.displayName)


	
},


    
resultRows: {
            title: "Result Rows",
            type: "array",
            required: [ 'name' 
],
            items: {
                "type": "object",
                "properties": {
                 
  
testResults: {
      "type": "number",
    },



name:{ type: "string", title: "Name",  	
},



value:{ type: "number", title: "Value",  	
},

 
                 
                }
            }
        },

    }
 };

}

export const testResultsUISchema = {
 	

patient: {  'ui:placeholder': "Patient" },



labTest: {  'ui:placeholder': "Lab Test" },


    
resultRows: {
 	items:{
         
  
testResults: {
      "ui:widget": "hidden"
    },



name: {  'ui:placeholder': "Name" },



value: {  'ui:placeholder': "Value" },

 
         
     }
 },

 }







export const testResultsHeaders = [
 
 
 {property:"patient_displayName",title:"Patient" }
 ,
 
 {property:"labTest_displayName",title:"Lab Test" }
      
 ]

export class TestResultsStore extends AppState {
    constructor(url: string, headers: any, formSchema: any, uiSchema: any) {
        super(url, headers, formSchema, uiSchema);
    }
}

export default class TestResultsWrapper extends React.Component<any, any> {

    data = new TestResultsStore('testResultses', testResultsHeaders,
    createSchema(), testResultsUISchema);

    render() {
        return (
            <BaseCrudComponent data={this.data} />
        );
    }
}

