

import * as React from 'react';
import * as ReactDOM from 'react-dom';

import BaseCrudComponent from '../commons/BaseComponent';
import AppState from '../commons/AppState';
import LookupService  from '../commons/LookupService';


export function createSchema(){ 
 
 return {
    title: "Vaccination",
    type: "object",
    required: [ 
],
    properties: {
    

review:{ type: "string", title: "Review",  	
},



rating:{ type: "integer", title: "Rating",  	
},



vaccine:{ type: "integer", title: "Vaccine",   

 'enum': LookupService.getLookup('vaccines').map(x => x.id   ),
 'enumNames': LookupService.getLookup('vaccines').map(x => x.displayName)


	
},



patient:{ type: "integer", title: "Patient",   

 'enum': LookupService.getLookup('patients').map(x => x.id   ),
 'enumNames': LookupService.getLookup('patients').map(x => x.displayName)


	
},


    
    }
 };

}

export const vaccinationUISchema = {
 	

review: { 'ui:widget': "textarea" , 'ui:placeholder': "Review" },



rating: { 'ui:widget': "updown" , 'ui:placeholder': "Rating" },



vaccine: {  'ui:placeholder': "Vaccine" },



patient: {  'ui:placeholder': "Patient" },


    
 }







export const vaccinationHeaders = [
 
 
 {property:"review",title:"Review" }
 ,
 
 {property:"rating",title:"Rating" }
 ,
 
 {property:"vaccine_displayName",title:"Vaccine" }
 ,
 
 {property:"patient_displayName",title:"Patient" }
      
 ]

export class VaccinationStore extends AppState {
    constructor(url: string, headers: any, formSchema: any, uiSchema: any) {
        super(url, headers, formSchema, uiSchema);
    }
}

export default class VaccinationWrapper extends React.Component<any, any> {

    data = new VaccinationStore('vaccinations', vaccinationHeaders,
    createSchema(), vaccinationUISchema);

    render() {
        return (
            <BaseCrudComponent data={this.data} />
        );
    }
}

