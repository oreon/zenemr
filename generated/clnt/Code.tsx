

import * as React from 'react';
import * as ReactDOM from 'react-dom';

import BaseCrudComponent from '../commons/BaseComponent';
import AppState from '../commons/AppState';
import LookupService  from '../commons/LookupService';


export function createSchema(){ 
 
 return {
    title: "Code",
    type: "object",
    required: [  'name' 
],
    properties: {
    

name:{ type: "string", title: "Name",  	
},



description:{ type: "string", title: "Description",  	
},



includes:{ type: "string", title: "Includes",  	
},



notIncludedHere:{ type: "string", title: "Not Included Here",  	
},



codeFirst:{ type: "string", title: "Code First",  	
},


  
section: {
      "type": "number",
    },



notCodedHere:{ type: "string", title: "Not Coded Here",  	
},



codeAlso:{ type: "string", title: "Code Also",  	
},


    
    }
 };

}

export const codeUISchema = {
 	

name: {  'ui:placeholder': "Name" },



description: { 'ui:widget': "textarea" , 'ui:placeholder': "Description" },



includes: { 'ui:widget': "textarea" , 'ui:placeholder': "Includes" },



notIncludedHere: { 'ui:widget': "textarea" , 'ui:placeholder': "Not Included Here" },



codeFirst: { 'ui:widget': "textarea" , 'ui:placeholder': "Code First" },


  
section: {
      "ui:widget": "hidden"
    },



notCodedHere: { 'ui:widget': "textarea" , 'ui:placeholder': "Not Coded Here" },



codeAlso: { 'ui:widget': "textarea" , 'ui:placeholder': "Code Also" },


    
 }







export const codeHeaders = [
 
 
 {property:"name",title:"Name" }
 ,
 
 {property:"description",title:"Description" }
 ,
 
 {property:"includes",title:"Includes" }
 ,
 
 {property:"notIncludedHere",title:"Not Included Here" }
 ,
 
 {property:"codeFirst",title:"Code First" }
 ,
 
 {property:"section_displayName",title:"Section" }
 ,
 
 {property:"notCodedHere",title:"Not Coded Here" }
 ,
 
 {property:"codeAlso",title:"Code Also" }
      
 ]

export class CodeStore extends AppState {
    constructor(url: string, headers: any, formSchema: any, uiSchema: any) {
        super(url, headers, formSchema, uiSchema);
    }
}

export default class CodeWrapper extends React.Component<any, any> {

    data = new CodeStore('codes', codeHeaders,
    createSchema(), codeUISchema);

    render() {
        return (
            <BaseCrudComponent data={this.data} />
        );
    }
}

