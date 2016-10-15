

import * as React from 'react';
import * as ReactDOM from 'react-dom';

import BaseCrudComponent from '../commons/BaseComponent';
import AppState from '../commons/AppState';
import LookupService  from '../commons/LookupService';


export function createSchema(){ 
 
 return {
    title: "Bed",
    type: "object",
    required: [  'name' 
],
    properties: {
    
  
room: {
      "type": "number",
    },



name:{ type: "string", title: "Name",  	
},


    
    }
 };

}

export const bedUISchema = {
 	
  
room: {
      "ui:widget": "hidden"
    },



name: {  'ui:placeholder': "Name" },


    
 }







export const bedHeaders = [
 
 
 {property:"room_displayName",title:"Room" }
 ,
 
 {property:"name",title:"Name" }
      
 ]

export class BedStore extends AppState {
    constructor(url: string, headers: any, formSchema: any, uiSchema: any) {
        super(url, headers, formSchema, uiSchema);
    }
}

export default class BedWrapper extends React.Component<any, any> {

    data = new BedStore('beds', bedHeaders,
    createSchema(), bedUISchema);

    render() {
        return (
            <BaseCrudComponent data={this.data} />
        );
    }
}

