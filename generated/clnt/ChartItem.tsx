

import * as React from 'react';
import * as ReactDOM from 'react-dom';

import BaseCrudComponent from '../commons/BaseComponent';
import AppState from '../commons/AppState';
import LookupService  from '../commons/LookupService';


export function createSchema(){ 
 
 return {
    title: "Chart Item",
    type: "object",
    required: [  'name' 
],
    properties: {
    

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
 };

}

export const chartItemUISchema = {
 	

name: {  'ui:placeholder': "Name" },



duration: { 'ui:widget': "updown" , 'ui:placeholder': "Duration" },


  
chart: {
      "ui:widget": "hidden"
    },



frequencyPeriod: {  'ui:placeholder': "Frequency Period" },


    
 }







export const chartItemHeaders = [
 
 
 {property:"name",title:"Name" }
 ,
 
 {property:"duration",title:"Duration" }
 ,
 
 {property:"chart_displayName",title:"Chart" }
 ,
 
 {property:"frequencyPeriod",title:"Frequency Period" }
      
 ]

export class ChartItemStore extends AppState {
    constructor(url: string, headers: any, formSchema: any, uiSchema: any) {
        super(url, headers, formSchema, uiSchema);
    }
}

export default class ChartItemWrapper extends React.Component<any, any> {

    data = new ChartItemStore('chartItems', chartItemHeaders,
    createSchema(), chartItemUISchema);

    render() {
        return (
            <BaseCrudComponent data={this.data} />
        );
    }
}

