

import * as React from 'react';
import * as ReactDOM from 'react-dom';

import BaseCrudComponent from '../commons/BaseComponent';
import AppState from '../commons/AppState';
import LookupService  from '../commons/LookupService';


export function createSchema(){ 
 
 return {
    title: "Physical Finding",
    type: "object",
    required: [  'name' 
],
    properties: {
    

name:{ type: "string", title: "Name",  	
},



icdCode:{ type: "string", title: "Icd Code",  	
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

export const physicalFindingUISchema = {
 	

name: {  'ui:placeholder': "Name" },



icdCode: {  'ui:placeholder': "Icd Code" },


    
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







export const physicalFindingHeaders = [
 
 
 {property:"name",title:"Name" }
 ,
 
 {property:"icdCode",title:"Icd Code" }
      
 ]

export class PhysicalFindingStore extends AppState {
    constructor(url: string, headers: any, formSchema: any, uiSchema: any) {
        super(url, headers, formSchema, uiSchema);
    }
}

export default class PhysicalFindingWrapper extends React.Component<any, any> {

    data = new PhysicalFindingStore('physicalFindings', physicalFindingHeaders,
    createSchema(), physicalFindingUISchema);

    render() {
        return (
            <BaseCrudComponent data={this.data} />
        );
    }
}

