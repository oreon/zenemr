

import * as React from 'react';
import * as ReactDOM from 'react-dom';

import BaseCrudComponent from '../commons/BaseComponent';
import AppState from '../commons/AppState';
import LookupService  from '../commons/LookupService';


export function createSchema(){ 
 
 return {
    title: "Section",
    type: "object",
    required: [  'name' 
],
    properties: {
    

name:{ type: "string", title: "Name",  	
},



description:{ type: "string", title: "Description",  	
},


  
chapter: {
      "type": "number",
    },


    
codes: {
            title: "Codes",
            type: "array",
            required: [ 'name' 
],
            items: {
                "type": "object",
                "properties": {
                 

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
            }
        },

    }
 };

}

export const sectionUISchema = {
 	

name: {  'ui:placeholder': "Name" },



description: { 'ui:widget': "textarea" , 'ui:placeholder': "Description" },


  
chapter: {
      "ui:widget": "hidden"
    },


    
codes: {
 	items:{
         

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
 },

 }







export const sectionHeaders = [
 
 
 {property:"name",title:"Name" }
 ,
 
 {property:"description",title:"Description" }
 ,
 
 {property:"chapter_displayName",title:"Chapter" }
      
 ]

export class SectionStore extends AppState {
    constructor(url: string, headers: any, formSchema: any, uiSchema: any) {
        super(url, headers, formSchema, uiSchema);
    }
}

export default class SectionWrapper extends React.Component<any, any> {

    data = new SectionStore('sections', sectionHeaders,
    createSchema(), sectionUISchema);

    render() {
        return (
            <BaseCrudComponent data={this.data} />
        );
    }
}

