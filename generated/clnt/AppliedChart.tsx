

import * as React from 'react';
import * as ReactDOM from 'react-dom';

import BaseCrudComponent from '../commons/BaseComponent';
import AppState from '../commons/AppState';
import LookupService  from '../commons/LookupService';


export function createSchema(){ 
 
 return {
    title: "Applied Chart",
    type: "object",
    required: [ 
],
    properties: {
    

chart:{ type: "integer", title: "Chart",   

 'enum': LookupService.getLookup('charts').map(x => x.id   ),
 'enumNames': LookupService.getLookup('charts').map(x => x.displayName)


	
},


    
    }
 };

}

export const appliedChartUISchema = {
 	

chart: {  'ui:placeholder': "Chart" },


    
 }







export const appliedChartHeaders = [
 
 
 {property:"chart_displayName",title:"Chart" }
      
 ]

export class AppliedChartStore extends AppState {
    constructor(url: string, headers: any, formSchema: any, uiSchema: any) {
        super(url, headers, formSchema, uiSchema);
    }
}

export default class AppliedChartWrapper extends React.Component<any, any> {

    data = new AppliedChartStore('appliedCharts', appliedChartHeaders,
    createSchema(), appliedChartUISchema);

    render() {
        return (
            <BaseCrudComponent data={this.data} />
        );
    }
}

