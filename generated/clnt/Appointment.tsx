

import * as React from 'react';
import * as ReactDOM from 'react-dom';

import BaseCrudComponent from '../commons/BaseComponent';
import AppState from '../commons/AppState';
import LookupService  from '../commons/LookupService';


export function createSchema(){ 
 
 return {
    title: "Appointment",
    type: "object",
    required: [  'start' 
],
    properties: {
    

start:{ type: "string", title: "Start",   "format": "date-time"	
},



end:{ type: "string", title: "End",   "format": "date-time"	
},



remarks:{ type: "string", title: "Remarks",  	
},



units:{ type: "integer", title: "Units",  	
},



patient:{ type: "integer", title: "Patient",   

 'enum': LookupService.getLookup('patients').map(x => x.id   ),
 'enumNames': LookupService.getLookup('patients').map(x => x.displayName)


	
},



employee:{ type: "integer", title: "Employee",   

 'enum': LookupService.getLookup('employees').map(x => x.id   ),
 'enumNames': LookupService.getLookup('employees').map(x => x.displayName)


	
},


    
    }
 };

}

export const appointmentUISchema = {
 	

start: {  'ui:placeholder': "Start" },



end: {  'ui:placeholder': "End" },



remarks: { 'ui:widget': "textarea" , 'ui:placeholder': "Remarks" },



units: { 'ui:widget': "updown" , 'ui:placeholder': "Units" },



patient: {  'ui:placeholder': "Patient" },



employee: {  'ui:placeholder': "Employee" },


    
 }







export const appointmentHeaders = [
 
 
 {property:"start",title:"Start" }
 ,
 
 {property:"end",title:"End" }
 ,
 
 {property:"remarks",title:"Remarks" }
 ,
 
 {property:"units",title:"Units" }
 ,
 
 {property:"patient_displayName",title:"Patient" }
 ,
 
 {property:"employee_displayName",title:"Employee" }
      
 ]

export class AppointmentStore extends AppState {
    constructor(url: string, headers: any, formSchema: any, uiSchema: any) {
        super(url, headers, formSchema, uiSchema);
    }
}

export default class AppointmentWrapper extends React.Component<any, any> {

    data = new AppointmentStore('appointments', appointmentHeaders,
    createSchema(), appointmentUISchema);

    render() {
        return (
            <BaseCrudComponent data={this.data} />
        );
    }
}

