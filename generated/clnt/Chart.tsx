

import * as React from 'react';
import * as ReactDOM from 'react-dom';

import BaseCrudComponent from '../commons/BaseComponent';
import AppState from '../commons/AppState';
import LookupService  from '../commons/LookupService';


export function createSchema(){ 
 
 return {
    title: "Chart",
    type: "object",
    required: [  'name' 
],
    properties: {
    

name:{ type: "string", title: "Name",  	
},



chronicCondition:{ type: "integer", title: "Chronic Condition",   

 'enum': LookupService.getLookup('chronicConditions').map(x => x.id   ),
 'enumNames': LookupService.getLookup('chronicConditions').map(x => x.displayName)


	
},


    
chartItems: {
            title: "Chart Items",
            type: "array",
            required: [ 'name' 
],
            items: {
                "type": "object",
                "properties": {
                 

name:{ type: "string", title: "Name",  	
},



duration:{ type: "integer", title: "Duration",  	
},


  
chart: {
      "type": "number",
    },



frequencyPeriod:{ type: "string", title: "Frequency Period",   
'enum' : [
'','0' ,'1' ,'2' ,'3' ,'4'   
],
'enumNames' : [
'Select','HOUR' ,'DAY' ,'WEEK' ,'MONTH' ,'YEAR'   
]
	
},

 
                 
                }
            }
        },

    }
 };

}

export const chartUISchema = {
 	

name: {  'ui:placeholder': "Name" },



chronicCondition: {  'ui:placeholder': "Chronic Condition" },


    
chartItems: {
 	items:{
         

name: {  'ui:placeholder': "Name" },



duration: { 'ui:widget': "updown" , 'ui:placeholder': "Duration" },


  
chart: {
      "ui:widget": "hidden"
    },



frequencyPeriod: {  'ui:placeholder': "Frequency Period" },

 
         
     }
 },

 }







export const chartHeaders = [
 
 
 {property:"name",title:"Name" }
 ,
 
 {property:"chronicCondition_displayName",title:"Chronic Condition" }
      
 ]

export class ChartStore extends AppState {
    constructor(url: string, headers: any, formSchema: any, uiSchema: any) {
        super(url, headers, formSchema, uiSchema);
    }
}

export default class ChartWrapper extends React.Component<any, any> {

    data = new ChartStore('charts', chartHeaders,
    createSchema(), chartUISchema);

    render() {
        return (
            <BaseCrudComponent data={this.data} />
        );
    }
}

