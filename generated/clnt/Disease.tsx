

import * as React from 'react';
import * as ReactDOM from 'react-dom';

import BaseCrudComponent from '../commons/BaseComponent';
import AppState from '../commons/AppState';
import LookupService  from '../commons/LookupService';


export function createSchema(){ 
 
 return {
    title: "Disease",
    type: "object",
    required: [  'name' 
],
    properties: {
    

gender:{ type: "string", title: "Gender",   
'enum' : [
'','0' ,'1'   
],
'enumNames' : [
'Select','F' ,'M'   
]
	
},



name:{ type: "string", title: "Name",  	
},



differentialDiagnoses:{ type: "integer", title: "Differential Diagnoses",   

 'enum': LookupService.getLookup('diseases').map(x => x.id   ),
 'enumNames': LookupService.getLookup('diseases').map(x => x.displayName)


	
},



relatedDisease:{ type: "integer", title: "Related Disease",   

 'enum': LookupService.getLookup('diseases').map(x => x.id   ),
 'enumNames': LookupService.getLookup('diseases').map(x => x.displayName)


	
},



conditionCategory:{ type: "integer", title: "Condition Category",   

 'enum': LookupService.getLookup('conditionCategorys').map(x => x.id   ),
 'enumNames': LookupService.getLookup('conditionCategorys').map(x => x.displayName)


	
},


    
    }
 };

}

export const diseaseUISchema = {
 	

gender: {  'ui:placeholder': "Gender" },



name: {  'ui:placeholder': "Name" },



differentialDiagnoses: {  'ui:placeholder': "Differential Diagnoses" },



relatedDisease: {  'ui:placeholder': "Related Disease" },



conditionCategory: {  'ui:placeholder': "Condition Category" },


    
 }







export const diseaseHeaders = [
 
 
 {property:"gender",title:"Gender" }
 ,
 
 {property:"name",title:"Name" }
 ,
 
 {property:"relatedDisease_displayName",title:"Related Disease" }
 ,
 
 {property:"conditionCategory_displayName",title:"Condition Category" }
      
 ]

export class DiseaseStore extends AppState {
    constructor(url: string, headers: any, formSchema: any, uiSchema: any) {
        super(url, headers, formSchema, uiSchema);
    }
}

export default class DiseaseWrapper extends React.Component<any, any> {

    data = new DiseaseStore('diseases', diseaseHeaders,
    createSchema(), diseaseUISchema);

    render() {
        return (
            <BaseCrudComponent data={this.data} />
        );
    }
}

