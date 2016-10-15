

import * as React from 'react';
import * as ReactDOM from 'react-dom';

import BaseCrudComponent from '../commons/BaseComponent';
import AppState from '../commons/AppState';
import LookupService  from '../commons/LookupService';


export function createSchema(){ 
 
 return {
    title: "Drug",
    type: "object",
    required: [  'name' 
],
    properties: {
    

name:{ type: "string", title: "Name",  	
},



absorption:{ type: "string", title: "Absorption",  	
},



biotransformation:{ type: "string", title: "Biotransformation",  	
},



atcCodes:{ type: "string", title: "Atc Codes",  	
},



contraIndication:{ type: "string", title: "Contra Indication",  	
},



description:{ type: "string", title: "Description",  	
},



dosageForm:{ type: "string", title: "Dosage Form",  	
},



foodInteractions:{ type: "string", title: "Food Interactions",  	
},



halfLife:{ type: "string", title: "Half Life",  	
},



indication:{ type: "string", title: "Indication",  	
},



halfLifeNumberOfHours:{ type: "number", title: "Half Life Number Of Hours",  	
},



mechanismOfAction:{ type: "string", title: "Mechanism Of Action",  	
},



patientInfo:{ type: "string", title: "Patient Info",  	
},



pharmacology:{ type: "string", title: "Pharmacology",  	
},



drugCategorys:{ type: "string", title: "Drug Categorys",   


	
},



toxicity:{ type: "string", title: "Toxicity",  	
},



routeOfElimination:{ type: "string", title: "Route Of Elimination",  	
},



volumeOfDistribution:{ type: "string", title: "Volume Of Distribution",  	
},



drugBankId:{ type: "string", title: "Drug Bank Id",  	
},



categories:{ type: "string", title: "Categories",  	
},


    
drugInteractions: {
            title: "Drug Interactions",
            type: "array",
            required: [
],
            items: {
                "type": "object",
                "properties": {
                 

description:{ type: "string", title: "Description",  	
},


  
drug: {
      "type": "number",
    },



interactingDrug:{ type: "integer", title: "Interacting Drug",   

 'enum': LookupService.getLookup('drugs').map(x => x.id   ),
 'enumNames': LookupService.getLookup('drugs').map(x => x.displayName)


	
},



severity:{ type: "string", title: "Severity",   
'enum' : [
'','0' ,'1' ,'2'   
],
'enumNames' : [
'Select','MILD' ,'MODERATE' ,'SEVERE'   
]
	
},

 
                 
                }
            }
        },

    }
 };

}

export const drugUISchema = {
 	

name: {  'ui:placeholder': "Name" },



absorption: { 'ui:widget': "textarea" , 'ui:placeholder': "Absorption" },



biotransformation: { 'ui:widget': "textarea" , 'ui:placeholder': "Biotransformation" },



atcCodes: {  'ui:placeholder': "Atc Codes" },



contraIndication: { 'ui:widget': "textarea" , 'ui:placeholder': "Contra Indication" },



description: { 'ui:widget': "textarea" , 'ui:placeholder': "Description" },



dosageForm: {  'ui:placeholder': "Dosage Form" },



foodInteractions: { 'ui:widget': "textarea" , 'ui:placeholder': "Food Interactions" },



halfLife: { 'ui:widget': "textarea" , 'ui:placeholder': "Half Life" },



indication: { 'ui:widget': "textarea" , 'ui:placeholder': "Indication" },



halfLifeNumberOfHours: {  'ui:placeholder': "Half Life Number Of Hours" },



mechanismOfAction: { 'ui:widget': "textarea" , 'ui:placeholder': "Mechanism Of Action" },



patientInfo: { 'ui:widget': "textarea" , 'ui:placeholder': "Patient Info" },



pharmacology: { 'ui:widget': "textarea" , 'ui:placeholder': "Pharmacology" },



drugCategorys: {  'ui:placeholder': "Drug Categorys" },



toxicity: { 'ui:widget': "textarea" , 'ui:placeholder': "Toxicity" },



routeOfElimination: { 'ui:widget': "textarea" , 'ui:placeholder': "Route Of Elimination" },



volumeOfDistribution: {  'ui:placeholder': "Volume Of Distribution" },



drugBankId: {  'ui:placeholder': "Drug Bank Id" },



categories: {  'ui:placeholder': "Categories" },


    
drugInteractions: {
 	items:{
         

description: { 'ui:widget': "textarea" , 'ui:placeholder': "Description" },


  
drug: {
      "ui:widget": "hidden"
    },



interactingDrug: {  'ui:placeholder': "Interacting Drug" },



severity: {  'ui:placeholder': "Severity" },

 
         
     }
 },

 }







export const drugHeaders = [
 
 
 {property:"name",title:"Name" }
 ,
 
 {property:"absorption",title:"Absorption" }
 ,
 
 {property:"biotransformation",title:"Biotransformation" }
 ,
 
 {property:"atcCodes",title:"Atc Codes" }
 ,
 
 {property:"contraIndication",title:"Contra Indication" }
 ,
 
 {property:"description",title:"Description" }
 ,
 
 {property:"dosageForm",title:"Dosage Form" }
 ,
 
 {property:"foodInteractions",title:"Food Interactions" }
 ,
 
 {property:"halfLife",title:"Half Life" }
 ,
 
 {property:"indication",title:"Indication" }
 ,
 
 {property:"halfLifeNumberOfHours",title:"Half Life Number Of Hours" }
 ,
 
 {property:"mechanismOfAction",title:"Mechanism Of Action" }
 ,
 
 {property:"patientInfo",title:"Patient Info" }
 ,
 
 {property:"pharmacology",title:"Pharmacology" }
 ,
 
 {property:"toxicity",title:"Toxicity" }
 ,
 
 {property:"routeOfElimination",title:"Route Of Elimination" }
 ,
 
 {property:"volumeOfDistribution",title:"Volume Of Distribution" }
 ,
 
 {property:"drugBankId",title:"Drug Bank Id" }
 ,
 
 {property:"categories",title:"Categories" }
      
 ]

export class DrugStore extends AppState {
    constructor(url: string, headers: any, formSchema: any, uiSchema: any) {
        super(url, headers, formSchema, uiSchema);
    }
}

export default class DrugWrapper extends React.Component<any, any> {

    data = new DrugStore('drugs', drugHeaders,
    createSchema(), drugUISchema);

    render() {
        return (
            <BaseCrudComponent data={this.data} />
        );
    }
}

