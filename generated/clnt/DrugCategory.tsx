

import * as React from 'react';
import * as ReactDOM from 'react-dom';

import BaseCrudComponent from '../commons/BaseComponent';
import AppState from '../commons/AppState';
import LookupService  from '../commons/LookupService';


export function createSchema(){ 
 
 return {
    title: "Drug Category",
    type: "object",
    required: [  'name' 
],
    properties: {
    

name:{ type: "string", title: "Name",  	
},



drugs:{ type: "array", title: "Drugs",   

    "items":{
 'enum': LookupService.getLookup('drugs').map(x => x.id .toString()  ),
 'enumNames': LookupService.getLookup('drugs').map(x => x.displayName)
    },
    "uniqueItems": true

	
},


    
    }
 };

}

export const drugCategoryUISchema = {
 	

name: {  'ui:placeholder': "Name" },



drugs: {  'ui:placeholder': "Drugs" },


    
 }







export const drugCategoryHeaders = [
 
 
 {property:"name",title:"Name" }
      
 ]

export class DrugCategoryStore extends AppState {
    constructor(url: string, headers: any, formSchema: any, uiSchema: any) {
        super(url, headers, formSchema, uiSchema);
    }
}

export default class DrugCategoryWrapper extends React.Component<any, any> {

    data = new DrugCategoryStore('drugCategorys', drugCategoryHeaders,
    createSchema(), drugCategoryUISchema);

    render() {
        return (
            <BaseCrudComponent data={this.data} />
        );
    }
}

