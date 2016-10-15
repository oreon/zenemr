

import * as React from 'react';
import * as ReactDOM from 'react-dom';

import BaseCrudComponent from '../commons/BaseComponent';
import AppState from '../commons/AppState';
import LookupService  from '../commons/LookupService';


export function createSchema(){ 
 
 return {
    title: "Setting Group",
    type: "object",
    required: [  'name' 
],
    properties: {
    

name:{ type: "string", title: "Name",  	
},


    
settingNames: {
            title: "Setting Names",
            type: "array",
            required: [ 'name' , 'defaultValue' 
],
            items: {
                "type": "object",
                "properties": {
                 

name:{ type: "string", title: "Name",  	
},


  
settingGroup: {
      "type": "number",
    },



defaultValue:{ type: "string", title: "Default Value",  	
},

 
                 
                }
            }
        },

    }
 };

}

export const settingGroupUISchema = {
 	

name: {  'ui:placeholder': "Name" },


    
settingNames: {
 	items:{
         

name: {  'ui:placeholder': "Name" },


  
settingGroup: {
      "ui:widget": "hidden"
    },



defaultValue: {  'ui:placeholder': "Default Value" },

 
         
     }
 },

 }







export const settingGroupHeaders = [
 
 
 {property:"name",title:"Name" }
      
 ]

export class SettingGroupStore extends AppState {
    constructor(url: string, headers: any, formSchema: any, uiSchema: any) {
        super(url, headers, formSchema, uiSchema);
    }
}

export default class SettingGroupWrapper extends React.Component<any, any> {

    data = new SettingGroupStore('settingGroups', settingGroupHeaders,
    createSchema(), settingGroupUISchema);

    render() {
        return (
            <BaseCrudComponent data={this.data} />
        );
    }
}

