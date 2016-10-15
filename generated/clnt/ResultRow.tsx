

import * as React from 'react';
import * as ReactDOM from 'react-dom';

import BaseCrudComponent from '../commons/BaseComponent';
import AppState from '../commons/AppState';
import LookupService  from '../commons/LookupService';


export function createSchema(){ 
 
 return {
    title: "Result Row",
    type: "object",
    required: [  'name' 
],
    properties: {
    
  
testResults: {
      "type": "number",
    },



name:{ type: "string", title: "Name",  	
},



value:{ type: "number", title: "Value",  	
},


    
    }
 };

}

export const resultRowUISchema = {
 	
  
testResults: {
      "ui:widget": "hidden"
    },



name: {  'ui:placeholder': "Name" },



value: {  'ui:placeholder': "Value" },


    
 }







export const resultRowHeaders = [
 
 
 {property:"testResults_displayName",title:"Test Results" }
 ,
 
 {property:"name",title:"Name" }
 ,
 
 {property:"value",title:"Value" }
      
 ]

export class ResultRowStore extends AppState {
    constructor(url: string, headers: any, formSchema: any, uiSchema: any) {
        super(url, headers, formSchema, uiSchema);
    }
}

export default class ResultRowWrapper extends React.Component<any, any> {

    data = new ResultRowStore('resultRows', resultRowHeaders,
    createSchema(), resultRowUISchema);

    render() {
        return (
            <BaseCrudComponent data={this.data} />
        );
    }
}

