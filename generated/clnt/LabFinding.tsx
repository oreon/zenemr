

import * as React from 'react';
import * as ReactDOM from 'react-dom';

import BaseCrudComponent from '../commons/BaseComponent';
import AppState from '../commons/AppState';
import LookupService  from '../commons/LookupService';


export function createSchema(){ 
 
 return {
    title: "Lab Finding",
    type: "object",
    required: [  'name' , 'testName' 
],
    properties: {
    

name:{ type: "string", title: "Name",  	
},



testName:{ type: "string", title: "Test Name",  	
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

export const labFindingUISchema = {
 	

name: {  'ui:placeholder': "Name" },



testName: {  'ui:placeholder': "Test Name" },


    
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







export const labFindingHeaders = [
 
 
 {property:"name",title:"Name" }
 ,
 
 {property:"testName",title:"Test Name" }
      
 ]

export class LabFindingStore extends AppState {
    constructor(url: string, headers: any, formSchema: any, uiSchema: any) {
        super(url, headers, formSchema, uiSchema);
    }
}

export default class LabFindingWrapper extends React.Component<any, any> {

    data = new LabFindingStore('labFindings', labFindingHeaders,
    createSchema(), labFindingUISchema);

    render() {
        return (
            <BaseCrudComponent data={this.data} />
        );
    }
}

