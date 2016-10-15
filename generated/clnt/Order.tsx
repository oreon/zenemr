

import * as React from 'react';
import * as ReactDOM from 'react-dom';

import BaseCrudComponent from '../commons/BaseComponent';
import AppState from '../commons/AppState';
import LookupService  from '../commons/LookupService';


export function createSchema(){ 
 
 return {
    title: "Order",
    type: "object",
    required: [ 
],
    properties: {
    

orderTemplate:{ type: "integer", title: "Order Template",   

 'enum': LookupService.getLookup('orderTemplates').map(x => x.id   ),
 'enumNames': LookupService.getLookup('orderTemplates').map(x => x.displayName)


	
},



patient:{ type: "integer", title: "Patient",   

 'enum': LookupService.getLookup('patients').map(x => x.id   ),
 'enumNames': LookupService.getLookup('patients').map(x => x.displayName)


	
},


    
    }
 };

}

export const orderUISchema = {
 	

orderTemplate: {  'ui:placeholder': "Order Template" },



patient: {  'ui:placeholder': "Patient" },


    
 }







export const orderHeaders = [
 
 
 {property:"orderTemplate_displayName",title:"Order Template" }
 ,
 
 {property:"patient_displayName",title:"Patient" }
      
 ]

export class OrderStore extends AppState {
    constructor(url: string, headers: any, formSchema: any, uiSchema: any) {
        super(url, headers, formSchema, uiSchema);
    }
}

export default class OrderWrapper extends React.Component<any, any> {

    data = new OrderStore('orders', orderHeaders,
    createSchema(), orderUISchema);

    render() {
        return (
            <BaseCrudComponent data={this.data} />
        );
    }
}

