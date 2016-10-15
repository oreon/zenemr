

import * as React from 'react';
import * as ReactDOM from 'react-dom';

import BaseCrudComponent from '../commons/BaseComponent';
import AppState from '../commons/AppState';
import LookupService  from '../commons/LookupService';


export function createSchema(){ 
 
 return {
    title: "Condition Category",
    type: "object",
    required: [  'name' 
],
    properties: {
    

name:{ type: "string", title: "Name",  	
},


    
    }
 };

}

export const conditionCategoryUISchema = {
 	

name: {  'ui:placeholder': "Name" },


    
 }







export const conditionCategoryHeaders = [
 
 
 {property:"name",title:"Name" }
      
 ]

export class ConditionCategoryStore extends AppState {
    constructor(url: string, headers: any, formSchema: any, uiSchema: any) {
        super(url, headers, formSchema, uiSchema);
    }
}

export default class ConditionCategoryWrapper extends React.Component<any, any> {

    data = new ConditionCategoryStore('conditionCategorys', conditionCategoryHeaders,
    createSchema(), conditionCategoryUISchema);

    render() {
        return (
            <BaseCrudComponent data={this.data} />
        );
    }
}

