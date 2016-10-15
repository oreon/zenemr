

import * as React from 'react';
import * as ReactDOM from 'react-dom';

import BaseCrudComponent from '../commons/BaseComponent';
import AppState from '../commons/AppState';
import LookupService  from '../commons/LookupService';


export function createSchema(){ 
 
 return {
    title: "Lab Test",
    type: "object",
    required: [  'name' 
],
    properties: {
    

name:{ type: "string", title: "Name",  	
},



encounters:{ type: "string", title: "Encounters",   


	
},


    
    }
 };

}

export const labTestUISchema = {
 	

name: {  'ui:placeholder': "Name" },



encounters: {  'ui:placeholder': "Encounters" },


    
 }







export const labTestHeaders = [
 
 
 {property:"name",title:"Name" }
      
 ]

export class LabTestStore extends AppState {
    constructor(url: string, headers: any, formSchema: any, uiSchema: any) {
        super(url, headers, formSchema, uiSchema);
    }
}

export default class LabTestWrapper extends React.Component<any, any> {

    data = new LabTestStore('labTests', labTestHeaders,
    createSchema(), labTestUISchema);

    render() {
        return (
            <BaseCrudComponent data={this.data} />
        );
    }
}

