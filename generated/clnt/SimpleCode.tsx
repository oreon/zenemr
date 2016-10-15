

import * as React from 'react';
import * as ReactDOM from 'react-dom';

import BaseCrudComponent from '../commons/BaseComponent';
import AppState from '../commons/AppState';
import LookupService  from '../commons/LookupService';


export function createSchema(){ 
 
 return {
    title: "Simple Code",
    type: "object",
    required: [  'name' 
],
    properties: {
    

name:{ type: "string", title: "Name",  	
},


    
    }
 };

}

export const simpleCodeUISchema = {
 	

name: {  'ui:placeholder': "Name" },


    
 }







export const simpleCodeHeaders = [
 
 
 {property:"name",title:"Name" }
      
 ]

export class SimpleCodeStore extends AppState {
    constructor(url: string, headers: any, formSchema: any, uiSchema: any) {
        super(url, headers, formSchema, uiSchema);
    }
}

export default class SimpleCodeWrapper extends React.Component<any, any> {

    data = new SimpleCodeStore('simpleCodes', simpleCodeHeaders,
    createSchema(), simpleCodeUISchema);

    render() {
        return (
            <BaseCrudComponent data={this.data} />
        );
    }
}

