

import * as React from 'react';
import * as ReactDOM from 'react-dom';

import BaseCrudComponent from '../commons/BaseComponent';
import AppState from '../commons/AppState';
import LookupService  from '../commons/LookupService';


export function createSchema(){ 
 
 return {
    title: "Room Type",
    type: "object",
    required: [  'name' 
],
    properties: {
    

name:{ type: "string", title: "Name",  	
},



description:{ type: "string", title: "Description",  	
},



rate:{ type: "number", title: "Rate",  	
},



numberOfBeds:{ type: "integer", title: "Number Of Beds",  	
},


    
    }
 };

}

export const roomTypeUISchema = {
 	

name: {  'ui:placeholder': "Name" },



description: { 'ui:widget': "textarea" , 'ui:placeholder': "Description" },



rate: {  'ui:placeholder': "Rate" },



numberOfBeds: { 'ui:widget': "updown" , 'ui:placeholder': "Number Of Beds" },


    
 }







export const roomTypeHeaders = [
 
 
 {property:"name",title:"Name" }
 ,
 
 {property:"description",title:"Description" }
 ,
 
 {property:"rate",title:"Rate" }
 ,
 
 {property:"numberOfBeds",title:"Number Of Beds" }
      
 ]

export class RoomTypeStore extends AppState {
    constructor(url: string, headers: any, formSchema: any, uiSchema: any) {
        super(url, headers, formSchema, uiSchema);
    }
}

export default class RoomTypeWrapper extends React.Component<any, any> {

    data = new RoomTypeStore('roomTypes', roomTypeHeaders,
    createSchema(), roomTypeUISchema);

    render() {
        return (
            <BaseCrudComponent data={this.data} />
        );
    }
}

