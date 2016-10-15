

import * as React from 'react';
import * as ReactDOM from 'react-dom';

import BaseCrudComponent from '../commons/BaseComponent';
import AppState from '../commons/AppState';
import LookupService  from '../commons/LookupService';


export function createSchema(){ 
 
 return {
    title: "Setting Name",
    type: "object",
    required: [  'name' , 'defaultValue' 
],
    properties: {
    

name:{ type: "string", title: "Name",  	
},


  
settingGroup: {
      "type": "number",
    },



defaultValue:{ type: "string", title: "Default Value",  	
},


    
    }
 };

}

export const settingNameUISchema = {
 	

name: {  'ui:placeholder': "Name" },


  
settingGroup: {
      "ui:widget": "hidden"
    },



defaultValue: {  'ui:placeholder': "Default Value" },


    
 }







export const settingNameHeaders = [
 
 
 {property:"name",title:"Name" }
 ,
 
 {property:"settingGroup_displayName",title:"Setting Group" }
 ,
 
 {property:"defaultValue",title:"Default Value" }
      
 ]

export class SettingNameStore extends AppState {
    constructor(url: string, headers: any, formSchema: any, uiSchema: any) {
        super(url, headers, formSchema, uiSchema);
    }
}

export default class SettingNameWrapper extends React.Component<any, any> {

    data = new SettingNameStore('settingNames', settingNameHeaders,
    createSchema(), settingNameUISchema);

    render() {
        return (
            <BaseCrudComponent data={this.data} />
        );
    }
}

