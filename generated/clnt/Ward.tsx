

import * as React from 'react';
import * as ReactDOM from 'react-dom';

import BaseCrudComponent from '../commons/BaseComponent';
import AppState from '../commons/AppState';
import LookupService  from '../commons/LookupService';


export function createSchema(){ 
 
 return {
    title: "Ward",
    type: "object",
    required: [  'name' 
],
    properties: {
    
  
facility: {
      "type": "number",
    },



name:{ type: "string", title: "Name",  	
},



gender:{ type: "string", title: "Gender",   
'enum' : [
'','0' ,'1'   
],
'enumNames' : [
'Select','F' ,'M'   
]
	
},



maxAge:{ type: "integer", title: "Max Age",  	
},


    
rooms: {
            title: "Rooms",
            type: "array",
            required: [ 'name' 
],
            items: {
                "type": "object",
                "properties": {
                 

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
            }
        },

    }
 };

}

export const wardUISchema = {
 	
  
facility: {
      "ui:widget": "hidden"
    },



name: {  'ui:placeholder': "Name" },



gender: {  'ui:placeholder': "Gender" },



maxAge: { 'ui:widget': "updown" , 'ui:placeholder': "Max Age" },


    
rooms: {
 	items:{
         

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
 },

 }







export const wardHeaders = [
 
 
 {property:"facility_displayName",title:"Facility" }
 ,
 
 {property:"name",title:"Name" }
 ,
 
 {property:"gender",title:"Gender" }
 ,
 
 {property:"maxAge",title:"Max Age" }
      
 ]

export class WardStore extends AppState {
    constructor(url: string, headers: any, formSchema: any, uiSchema: any) {
        super(url, headers, formSchema, uiSchema);
    }
}

export default class WardWrapper extends React.Component<any, any> {

    data = new WardStore('wards', wardHeaders,
    createSchema(), wardUISchema);

    render() {
        return (
            <BaseCrudComponent data={this.data} />
        );
    }
}

