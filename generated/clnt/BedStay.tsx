

import * as React from 'react';
import * as ReactDOM from 'react-dom';

import BaseCrudComponent from '../commons/BaseComponent';
import AppState from '../commons/AppState';
import LookupService  from '../commons/LookupService';


export function createSchema(){ 
 
 return {
    title: "Bed Stay",
    type: "object",
    required: [ 
],
    properties: {
    

fromDate:{ type: "string", title: "From Date",   "format": "date"	
},



toDate:{ type: "string", title: "To Date",   "format": "date"	
},


  
admission: {
      "type": "number",
    },


    
    }
 };

}

export const bedStayUISchema = {
 	

fromDate: {  'ui:placeholder': "From Date" },



toDate: {  'ui:placeholder': "To Date" },


  
admission: {
      "ui:widget": "hidden"
    },


    
 }







export const bedStayHeaders = [
 
 
 {property:"fromDate",title:"From Date" }
 ,
 
 {property:"toDate",title:"To Date" }
 ,
 
 {property:"admission_displayName",title:"Admission" }
      
 ]

export class BedStayStore extends AppState {
    constructor(url: string, headers: any, formSchema: any, uiSchema: any) {
        super(url, headers, formSchema, uiSchema);
    }
}

export default class BedStayWrapper extends React.Component<any, any> {

    data = new BedStayStore('bedStays', bedStayHeaders,
    createSchema(), bedStayUISchema);

    render() {
        return (
            <BaseCrudComponent data={this.data} />
        );
    }
}

