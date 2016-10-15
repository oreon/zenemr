

import * as React from 'react';
import * as ReactDOM from 'react-dom';

import BaseCrudComponent from '../commons/BaseComponent';
import AppState from '../commons/AppState';
import LookupService  from '../commons/LookupService';


export function createSchema(){ 
 
 return {
    title: "Chronic Condition",
    type: "object",
    required: [ 
],
    properties: {
    

name:{ type: "string", title: "Name",  	
},



charts:{ type: "integer", title: "Charts",   

 'enum': LookupService.getLookup('charts').map(x => x.id   ),
 'enumNames': LookupService.getLookup('charts').map(x => x.displayName)


	
},


    
    }
 };

}

export const chronicConditionUISchema = {
 	

name: {  'ui:placeholder': "Name" },



charts: {  'ui:placeholder': "Charts" },


    
 }







export const chronicConditionHeaders = [
 
 
 {property:"name",title:"Name" }
      
 ]

export class ChronicConditionStore extends AppState {
    constructor(url: string, headers: any, formSchema: any, uiSchema: any) {
        super(url, headers, formSchema, uiSchema);
    }
}

export default class ChronicConditionWrapper extends React.Component<any, any> {

    data = new ChronicConditionStore('chronicConditions', chronicConditionHeaders,
    createSchema(), chronicConditionUISchema);

    render() {
        return (
            <BaseCrudComponent data={this.data} />
        );
    }
}

