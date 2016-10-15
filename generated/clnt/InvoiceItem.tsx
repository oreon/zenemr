

import * as React from 'react';
import * as ReactDOM from 'react-dom';

import BaseCrudComponent from '../commons/BaseComponent';
import AppState from '../commons/AppState';
import LookupService  from '../commons/LookupService';


export function createSchema(){ 
 
 return {
    title: "Invoice Item",
    type: "object",
    required: [  'appliedPrice' 
],
    properties: {
    

units:{ type: "integer", title: "Units",  	
},



service:{ type: "integer", title: "Service",   

 'enum': LookupService.getLookup('services').map(x => x.id   ),
 'enumNames': LookupService.getLookup('services').map(x => x.displayName)


	
},


  
invoice: {
      "type": "number",
    },



appliedPrice:{ type: "number", title: "Applied Price",  	
},



total:{ type: "number", title: "Total",  	
},


    
    }
 };

}

export const invoiceItemUISchema = {
 	

units: { 'ui:widget': "updown" , 'ui:placeholder': "Units" },



service: {  'ui:placeholder': "Service" },


  
invoice: {
      "ui:widget": "hidden"
    },



appliedPrice: {  'ui:placeholder': "Applied Price" },



total: {  'ui:placeholder': "Total" },


    
 }







export const invoiceItemHeaders = [
 
 
 {property:"units",title:"Units" }
 ,
 
 {property:"service_displayName",title:"Service" }
 ,
 
 {property:"invoice_displayName",title:"Invoice" }
 ,
 
 {property:"appliedPrice",title:"Applied Price" }
 ,
 
 {property:"total",title:"Total" }
      
 ]

export class InvoiceItemStore extends AppState {
    constructor(url: string, headers: any, formSchema: any, uiSchema: any) {
        super(url, headers, formSchema, uiSchema);
    }
}

export default class InvoiceItemWrapper extends React.Component<any, any> {

    data = new InvoiceItemStore('invoiceItems', invoiceItemHeaders,
    createSchema(), invoiceItemUISchema);

    render() {
        return (
            <BaseCrudComponent data={this.data} />
        );
    }
}

