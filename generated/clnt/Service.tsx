

import * as React from 'react';
import * as ReactDOM from 'react-dom';

import BaseCrudComponent from '../commons/BaseComponent';
import AppState from '../commons/AppState';
import LookupService  from '../commons/LookupService';


export function createSchema(){ 
 
 return {
    title: "Service",
    type: "object",
    required: [  'name' , 'price' 
],
    properties: {
    

name:{ type: "string", title: "Name",  	
},



price:{ type: "number", title: "Price",  	
},


    
    }
 };

}

export const serviceUISchema = {
 	

name: {  'ui:placeholder': "Name" },



price: {  'ui:placeholder': "Price" },


    
 }







export const serviceHeaders = [
 
 
 {property:"name",title:"Name" }
 ,
 
 {property:"price",title:"Price" }
      
 ]

export class ServiceStore extends AppState {
    constructor(url: string, headers: any, formSchema: any, uiSchema: any) {
        super(url, headers, formSchema, uiSchema);
    }
}

export default class ServiceWrapper extends React.Component<any, any> {

    data = new ServiceStore('services', serviceHeaders,
    createSchema(), serviceUISchema);

    render() {
        return (
            <BaseCrudComponent data={this.data} />
        );
    }
}

