

import * as React from 'react';
import * as ReactDOM from 'react-dom';

import BaseCrudComponent from '../commons/BaseComponent';
import AppState from '../commons/AppState';
import LookupService  from '../commons/LookupService';


export function createSchema(){ 
 
 return {
    title: "Differential Dx",
    type: "object",
    required: [  'name' 
],
    properties: {
    

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
 };

}

export const differentialDxUISchema = {
 	

name: {  'ui:placeholder': "Name" },



dxCategory: {  'ui:placeholder': "Dx Category" },


  
finding: {
      "ui:widget": "hidden"
    },


    
 }







export const differentialDxHeaders = [
 
 
 {property:"name",title:"Name" }
 ,
 
 {property:"dxCategory_displayName",title:"Dx Category" }
 ,
 
 {property:"finding_displayName",title:"Finding" }
      
 ]

export class DifferentialDxStore extends AppState {
    constructor(url: string, headers: any, formSchema: any, uiSchema: any) {
        super(url, headers, formSchema, uiSchema);
    }
}

export default class DifferentialDxWrapper extends React.Component<any, any> {

    data = new DifferentialDxStore('differentialDxs', differentialDxHeaders,
    createSchema(), differentialDxUISchema);

    render() {
        return (
            <BaseCrudComponent data={this.data} />
        );
    }
}

