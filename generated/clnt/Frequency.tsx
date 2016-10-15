

import * as React from 'react';
import * as ReactDOM from 'react-dom';

import BaseCrudComponent from '../commons/BaseComponent';
import AppState from '../commons/AppState';
import LookupService  from '../commons/LookupService';


export function createSchema(){ 
 
 return {
    title: "Frequency",
    type: "object",
    required: [  'name' 
],
    properties: {
    

name:{ type: "string", title: "Name",  	
},



qtyPerDay:{ type: "integer", title: "Qty Per Day",  	
},



remarkts:{ type: "string", title: "Remarkts",  	
},


    
    }
 };

}

export const frequencyUISchema = {
 	

name: {  'ui:placeholder': "Name" },



qtyPerDay: { 'ui:widget': "updown" , 'ui:placeholder': "Qty Per Day" },



remarkts: { 'ui:widget': "textarea" , 'ui:placeholder': "Remarkts" },


    
 }







export const frequencyHeaders = [
 
 
 {property:"name",title:"Name" }
 ,
 
 {property:"qtyPerDay",title:"Qty Per Day" }
 ,
 
 {property:"remarkts",title:"Remarkts" }
      
 ]

export class FrequencyStore extends AppState {
    constructor(url: string, headers: any, formSchema: any, uiSchema: any) {
        super(url, headers, formSchema, uiSchema);
    }
}

export default class FrequencyWrapper extends React.Component<any, any> {

    data = new FrequencyStore('frequencys', frequencyHeaders,
    createSchema(), frequencyUISchema);

    render() {
        return (
            <BaseCrudComponent data={this.data} />
        );
    }
}

