

import * as React from 'react';
import * as ReactDOM from 'react-dom';

import BaseCrudComponent from '../commons/BaseComponent';
import AppState from '../commons/AppState';
import LookupService  from '../commons/LookupService';


export function createSchema(){ 
 
 return {
    title: "Settings",
    type: "object",
    required: [ 
],
    properties: {
    
    
    }
 };

}

export const settingsUISchema = {
 	
    
 }







export const settingsHeaders = [
      
 ]

export class SettingsStore extends AppState {
    constructor(url: string, headers: any, formSchema: any, uiSchema: any) {
        super(url, headers, formSchema, uiSchema);
    }
}

export default class SettingsWrapper extends React.Component<any, any> {

    data = new SettingsStore('settingses', settingsHeaders,
    createSchema(), settingsUISchema);

    render() {
        return (
            <BaseCrudComponent data={this.data} />
        );
    }
}

