

import * as React from 'react';
import * as ReactDOM from 'react-dom';

import BaseCrudComponent from '../commons/BaseComponent';
import AppState from '../commons/AppState';
import LookupService  from '../commons/LookupService';


export function createSchema(){ 
 
 return {
    title: "Order Template",
    type: "object",
    required: [ 
],
    properties: {
    
    
    }
 };

}

export const orderTemplateUISchema = {
 	
    
 }







export const orderTemplateHeaders = [
      
 ]

export class OrderTemplateStore extends AppState {
    constructor(url: string, headers: any, formSchema: any, uiSchema: any) {
        super(url, headers, formSchema, uiSchema);
    }
}

export default class OrderTemplateWrapper extends React.Component<any, any> {

    data = new OrderTemplateStore('orderTemplates', orderTemplateHeaders,
    createSchema(), orderTemplateUISchema);

    render() {
        return (
            <BaseCrudComponent data={this.data} />
        );
    }
}

