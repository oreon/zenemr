

import * as React from 'react';
import * as ReactDOM from 'react-dom';

import BaseCrudComponent from '../commons/BaseComponent';
import AppState from '../commons/AppState';
import LookupService  from '../commons/LookupService';


export function createSchema(){ 
 
 return {
    title: "Vaccine",
    type: "object",
    required: [  'name' 
],
    properties: {
    

name:{ type: "string", title: "Name",  	
},


    
    }
 };

}

export const vaccineUISchema = {
 	

name: {  'ui:placeholder': "Name" },


    
 }







export const vaccineHeaders = [
 
 
 {property:"name",title:"Name" }
      
 ]

export class VaccineStore extends AppState {
    constructor(url: string, headers: any, formSchema: any, uiSchema: any) {
        super(url, headers, formSchema, uiSchema);
    }
}

export default class VaccineWrapper extends React.Component<any, any> {

    data = new VaccineStore('vaccines', vaccineHeaders,
    createSchema(), vaccineUISchema);

    render() {
        return (
            <BaseCrudComponent data={this.data} />
        );
    }
}

