

import * as React from 'react';
import * as ReactDOM from 'react-dom';

import BaseCrudComponent from '../commons/BaseComponent';
import AppState from '../commons/AppState';
import LookupService  from '../commons/LookupService';


export function createSchema(){ 
 
 return {
    title: "Dx Category",
    type: "object",
    required: [  'name' 
],
    properties: {
    

name:{ type: "string", title: "Name",  	
},


    
    }
 };

}

export const dxCategoryUISchema = {
 	

name: {  'ui:placeholder': "Name" },


    
 }







export const dxCategoryHeaders = [
 
 
 {property:"name",title:"Name" }
      
 ]

export class DxCategoryStore extends AppState {
    constructor(url: string, headers: any, formSchema: any, uiSchema: any) {
        super(url, headers, formSchema, uiSchema);
    }
}

export default class DxCategoryWrapper extends React.Component<any, any> {

    data = new DxCategoryStore('dxCategorys', dxCategoryHeaders,
    createSchema(), dxCategoryUISchema);

    render() {
        return (
            <BaseCrudComponent data={this.data} />
        );
    }
}

