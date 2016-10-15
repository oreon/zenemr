

import * as React from 'react';
import * as ReactDOM from 'react-dom';

import BaseCrudComponent from '../commons/BaseComponent';
import AppState from '../commons/AppState';
import LookupService  from '../commons/LookupService';


export function createSchema(){ 
 
 return {
    title: "Condition Finding",
    type: "object",
    required: [ 
],
    properties: {
    

disease:{ type: "integer", title: "Disease",   

 'enum': LookupService.getLookup('diseases').map(x => x.id   ),
 'enumNames': LookupService.getLookup('diseases').map(x => x.displayName)


	
},



falsePositive:{ type: "boolean", title: "False Positive",  	
},


    
    }
 };

}

export const conditionFindingUISchema = {
 	

disease: {  'ui:placeholder': "Disease" },



falsePositive: {  'ui:placeholder': "False Positive" },


    
 }







export const conditionFindingHeaders = [
 
 
 {property:"disease_displayName",title:"Disease" }
 ,
 
 {property:"falsePositive",title:"False Positive" }
      
 ]

export class ConditionFindingStore extends AppState {
    constructor(url: string, headers: any, formSchema: any, uiSchema: any) {
        super(url, headers, formSchema, uiSchema);
    }
}

export default class ConditionFindingWrapper extends React.Component<any, any> {

    data = new ConditionFindingStore('conditionFindings', conditionFindingHeaders,
    createSchema(), conditionFindingUISchema);

    render() {
        return (
            <BaseCrudComponent data={this.data} />
        );
    }
}

