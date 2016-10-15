

import * as React from 'react';
import * as ReactDOM from 'react-dom';

import BaseCrudComponent from '../commons/BaseComponent';
import AppState from '../commons/AppState';
import LookupService  from '../commons/LookupService';


export function createSchema(){ 
 
 return {
    title: "Room",
    type: "object",
    required: [  'name' 
],
    properties: {
    

name:{ type: "string", title: "Name",  	
},



roomType:{ type: "integer", title: "Room Type",   

 'enum': LookupService.getLookup('roomTypes').map(x => x.id   ),
 'enumNames': LookupService.getLookup('roomTypes').map(x => x.displayName)


	
},


  
ward: {
      "type": "number",
    },


    
beds: {
            title: "Beds",
            type: "array",
            required: [ 'name' 
],
            items: {
                "type": "object",
                "properties": {
                 
  
room: {
      "type": "number",
    },



name:{ type: "string", title: "Name",  	
},

 
                 
                }
            }
        },

    }
 };

}

export const roomUISchema = {
 	

name: {  'ui:placeholder': "Name" },



roomType: {  'ui:placeholder': "Room Type" },


  
ward: {
      "ui:widget": "hidden"
    },


    
beds: {
 	items:{
         
  
room: {
      "ui:widget": "hidden"
    },



name: {  'ui:placeholder': "Name" },

 
         
     }
 },

 }







export const roomHeaders = [
 
 
 {property:"name",title:"Name" }
 ,
 
 {property:"roomType_displayName",title:"Room Type" }
 ,
 
 {property:"ward_displayName",title:"Ward" }
      
 ]

export class RoomStore extends AppState {
    constructor(url: string, headers: any, formSchema: any, uiSchema: any) {
        super(url, headers, formSchema, uiSchema);
    }
}

export default class RoomWrapper extends React.Component<any, any> {

    data = new RoomStore('rooms', roomHeaders,
    createSchema(), roomUISchema);

    render() {
        return (
            <BaseCrudComponent data={this.data} />
        );
    }
}

