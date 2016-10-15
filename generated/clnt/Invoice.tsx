

import * as React from 'react';
import * as ReactDOM from 'react-dom';

import BaseCrudComponent from '../commons/BaseComponent';
import AppState from '../commons/AppState';
import LookupService  from '../commons/LookupService';


export function createSchema(){ 
 
 return {
    title: "Invoice",
    type: "object",
    required: [ 
],
    properties: {
    

notes:{ type: "string", title: "Notes",  	
},



totalAmount:{ type: "number", title: "Total Amount",  	
},



paidAmount:{ type: "number", title: "Paid Amount",  	
},



patient:{ type: "integer", title: "Patient",   

 'enum': LookupService.getLookup('patients').map(x => x.id   ),
 'enumNames': LookupService.getLookup('patients').map(x => x.displayName)


	
},


    
invoiceItems: {
            title: "Invoice Items",
            type: "array",
            required: [ 'appliedPrice' 
],
            items: {
                "type": "object",
                "properties": {
                 

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
            }
        },

    }
 };

}

export const invoiceUISchema = {
 	

notes: {  'ui:placeholder': "Notes" },



totalAmount: {  'ui:placeholder': "Total Amount" },



paidAmount: {  'ui:placeholder': "Paid Amount" },



patient: {  'ui:placeholder': "Patient" },


    
invoiceItems: {
 	items:{
         

units: { 'ui:widget': "updown" , 'ui:placeholder': "Units" },



service: {  'ui:placeholder': "Service" },


  
invoice: {
      "ui:widget": "hidden"
    },



appliedPrice: {  'ui:placeholder': "Applied Price" },



total: {  'ui:placeholder': "Total" },

 
         
     }
 },

 }







export const invoiceHeaders = [
 
 
 {property:"notes",title:"Notes" }
 ,
 
 {property:"totalAmount",title:"Total Amount" }
 ,
 
 {property:"paidAmount",title:"Paid Amount" }
 ,
 
 {property:"patient_displayName",title:"Patient" }
      
 ]

export class InvoiceStore extends AppState {
    constructor(url: string, headers: any, formSchema: any, uiSchema: any) {
        super(url, headers, formSchema, uiSchema);
    }
}

export default class InvoiceWrapper extends React.Component<any, any> {

    data = new InvoiceStore('invoices', invoiceHeaders,
    createSchema(), invoiceUISchema);

    render() {
        return (
            <BaseCrudComponent data={this.data} />
        );
    }
}

