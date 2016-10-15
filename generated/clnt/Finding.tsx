

import * as React from 'react';
import * as ReactDOM from 'react-dom';

import BaseCrudComponent from '../commons/BaseComponent';
import AppState from '../commons/AppState';
import LookupService  from '../commons/LookupService';


export function createSchema(){ 
 
 return {
    title: "Finding",
    type: "object",
    required: [  'name' 
],
    properties: {
    

name:{ type: "string", title: "Name",  	
},


    
differentialDxs: {
            title: "Differential Dxs",
            type: "array",
            required: [ 'name' 
],
            items: {
                "type": "object",
                "properties": {
                 

name:{ type: "string", title: "Name",  	
},



dxCategory:{ type: "integer", title: "Dx Category",   

 'enum': LookupService.getLookup('dxCategorys').map(x => x.id   ),
 'enumNames': LookupService.getLookup('dxCategorys').map(x => x.displayName)


	
},


  
finding: {
      "type": "number",
    },

 
                 
                }
            }
        },

    }
 };

}

export const findingUISchema = {
 	

name: {  'ui:placeholder': "Name" },


    
differentialDxs: {
 	items:{
         

name: {  'ui:placeholder': "Name" },



dxCategory: {  'ui:placeholder': "Dx Category" },


  
finding: {
      "ui:widget": "hidden"
    },

 
         
     }
 },

 }







export const findingHeaders = [
 
 
 {property:"name",title:"Name" }
      
 ]

export class FindingStore extends AppState {
    constructor(url: string, headers: any, formSchema: any, uiSchema: any) {
        super(url, headers, formSchema, uiSchema);
    }
}

export default class FindingWrapper extends React.Component<any, any> {

    data = new FindingStore('findings', findingHeaders,
    createSchema(), findingUISchema);

    render() {
        return (
            <BaseCrudComponent data={this.data} />
        );
    }
}

