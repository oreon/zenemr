

import * as React from 'react';
import * as ReactDOM from 'react-dom';

import BaseCrudComponent from '../commons/BaseComponent';
import AppState from '../commons/AppState';
import LookupService  from '../commons/LookupService';


export function createSchema(){ 
 
 return {
    title: "Chart Procedure",
    type: "object",
    required: [ 
],
    properties: {
    

chartItem:{ type: "integer", title: "Chart Item",   

 'enum': LookupService.getLookup('chartItems').map(x => x.id   ),
 'enumNames': LookupService.getLookup('chartItems').map(x => x.displayName)


	
},



dueDate:{ type: "string", title: "Due Date",   "format": "date"	
},



datePerformed:{ type: "string", title: "Date Performed",   "format": "date"	
},



remarks:{ type: "string", title: "Remarks",  	
},


    
    }
 };

}

export const chartProcedureUISchema = {
 	

chartItem: {  'ui:placeholder': "Chart Item" },



dueDate: {  'ui:placeholder': "Due Date" },



datePerformed: {  'ui:placeholder': "Date Performed" },



remarks: { 'ui:widget': "textarea" , 'ui:placeholder': "Remarks" },


    
 }







export const chartProcedureHeaders = [
 
 
 {property:"chartItem_displayName",title:"Chart Item" }
 ,
 
 {property:"dueDate",title:"Due Date" }
 ,
 
 {property:"datePerformed",title:"Date Performed" }
 ,
 
 {property:"remarks",title:"Remarks" }
      
 ]

export class ChartProcedureStore extends AppState {
    constructor(url: string, headers: any, formSchema: any, uiSchema: any) {
        super(url, headers, formSchema, uiSchema);
    }
}

export default class ChartProcedureWrapper extends React.Component<any, any> {

    data = new ChartProcedureStore('chartProcedures', chartProcedureHeaders,
    createSchema(), chartProcedureUISchema);

    render() {
        return (
            <BaseCrudComponent data={this.data} />
        );
    }
}

