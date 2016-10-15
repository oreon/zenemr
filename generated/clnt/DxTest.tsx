

import * as React from 'react';
import * as ReactDOM from 'react-dom';

import BaseCrudComponent from '../commons/BaseComponent';
import AppState from '../commons/AppState';
import LookupService  from '../commons/LookupService';


export function createSchema(){ 
 
 return {
    title: "Dx Test",
    type: "object",
    required: [  'name' 
],
    properties: {
    

name:{ type: "string", title: "Name",  	
},



description:{ type: "string", title: "Description",  	
},


    
    }
 };

}

export const dxTestUISchema = {
 	

name: {  'ui:placeholder': "Name" },



description: { 'ui:widget': "textarea" , 'ui:placeholder': "Description" },


    
 }







export const dxTestHeaders = [
 
 
 {property:"name",title:"Name" }
 ,
 
 {property:"description",title:"Description" }
      
 ]

export class DxTestStore extends AppState {
    constructor(url: string, headers: any, formSchema: any, uiSchema: any) {
        super(url, headers, formSchema, uiSchema);
    }
}

export default class DxTestWrapper extends React.Component<any, any> {

    data = new DxTestStore('dxTests', dxTestHeaders,
    createSchema(), dxTestUISchema);

    render() {
        return (
            <BaseCrudComponent data={this.data} />
        );
    }
}

