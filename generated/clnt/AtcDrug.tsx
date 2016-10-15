

import * as React from 'react';
import * as ReactDOM from 'react-dom';

import BaseCrudComponent from '../commons/BaseComponent';
import AppState from '../commons/AppState';
import LookupService  from '../commons/LookupService';


export function createSchema(){ 
 
 return {
    title: "Atc Drug",
    type: "object",
    required: [  'name' 
],
    properties: {
    

code:{ type: "string", title: "Code",  	
},



name:{ type: "string", title: "Name",  	
},



drug:{ type: "integer", title: "Drug",   

 'enum': LookupService.getLookup('drugs').map(x => x.id   ),
 'enumNames': LookupService.getLookup('drugs').map(x => x.displayName)


	
},


  
parent: {
      "type": "number",
    },


    
subcategories: {
            title: "Subcategories",
            type: "array",
            required: [ 'name' 
],
            items: {
                "type": "object",
                "properties": {
                 

code:{ type: "string", title: "Code",  	
},



name:{ type: "string", title: "Name",  	
},



drug:{ type: "integer", title: "Drug",   

 'enum': LookupService.getLookup('drugs').map(x => x.id   ),
 'enumNames': LookupService.getLookup('drugs').map(x => x.displayName)


	
},


  
parent: {
      "type": "number",
    },

 
                 
                }
            }
        },

    }
 };

}

export const atcDrugUISchema = {
 	

code: {  'ui:placeholder': "Code" },



name: {  'ui:placeholder': "Name" },



drug: {  'ui:placeholder': "Drug" },


  
parent: {
      "ui:widget": "hidden"
    },


    
subcategories: {
 	items:{
         

code: {  'ui:placeholder': "Code" },



name: {  'ui:placeholder': "Name" },



drug: {  'ui:placeholder': "Drug" },


  
parent: {
      "ui:widget": "hidden"
    },

 
         
     }
 },

 }







export const atcDrugHeaders = [
 
 
 {property:"code",title:"Code" }
 ,
 
 {property:"name",title:"Name" }
 ,
 
 {property:"drug_displayName",title:"Drug" }
 ,
 
 {property:"parent_displayName",title:"Parent" }
      
 ]

export class AtcDrugStore extends AppState {
    constructor(url: string, headers: any, formSchema: any, uiSchema: any) {
        super(url, headers, formSchema, uiSchema);
    }
}

export default class AtcDrugWrapper extends React.Component<any, any> {

    data = new AtcDrugStore('atcDrugs', atcDrugHeaders,
    createSchema(), atcDrugUISchema);

    render() {
        return (
            <BaseCrudComponent data={this.data} />
        );
    }
}

