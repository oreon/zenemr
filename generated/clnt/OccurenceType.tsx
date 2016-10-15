

import * as React from 'react';
import * as ReactDOM from 'react-dom';

import BaseCrudComponent from '../commons/BaseComponent';
import AppState from '../commons/AppState';
import LookupService  from '../commons/LookupService';


export function createSchema(){ 
 
 return {
    title: "Occurence Type",
    type: "object",
    required: [  'name' 
],
    properties: {
    

name:{ type: "string", title: "Name",  	
},


    
    }
 };

}

export const occurenceTypeUISchema = {
 	

name: {  'ui:placeholder': "Name" },


    
 }







export const occurenceTypeHeaders = [
 
 
 {property:"name",title:"Name" }
      
 ]

export class OccurenceTypeStore extends AppState {
    constructor(url: string, headers: any, formSchema: any, uiSchema: any) {
        super(url, headers, formSchema, uiSchema);
    }
}

export default class OccurenceTypeWrapper extends React.Component<any, any> {

    data = new OccurenceTypeStore('occurenceTypes', occurenceTypeHeaders,
    createSchema(), occurenceTypeUISchema);

    render() {
        return (
            <BaseCrudComponent data={this.data} />
        );
    }
}

