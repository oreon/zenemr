

import * as React from 'react';
import * as ReactDOM from 'react-dom';

import BaseCrudComponent from '../commons/BaseComponent';
import AppState from '../commons/AppState';
import LookupService  from '../commons/LookupService';


export function createSchema(){ 
 
 return {
    title: "Setting",
    type: "object",
    required: [  'value' 
],
    properties: {
    

value:{ type: "string", title: "Value",  	
},



settingName:{ type: "integer", title: "Setting Name",   

 'enum': LookupService.getLookup('settingNames').map(x => x.id   ),
 'enumNames': LookupService.getLookup('settingNames').map(x => x.displayName)


	
},


    
    }
 };

}

export const settingUISchema = {
 	

value: {  'ui:placeholder': "Value" },



settingName: {  'ui:placeholder': "Setting Name" },


    
 }







export const settingHeaders = [
 
 
 {property:"value",title:"Value" }
 ,
 
 {property:"settingName_displayName",title:"Setting Name" }
      
 ]

export class SettingStore extends AppState {
    constructor(url: string, headers: any, formSchema: any, uiSchema: any) {
        super(url, headers, formSchema, uiSchema);
    }
}

export default class SettingWrapper extends React.Component<any, any> {

    data = new SettingStore('settings', settingHeaders,
    createSchema(), settingUISchema);

    render() {
        return (
            <BaseCrudComponent data={this.data} />
        );
    }
}

