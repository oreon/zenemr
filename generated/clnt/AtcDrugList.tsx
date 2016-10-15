

import {SimpleForm, SimpleList, EditViewBase, SimpleView } from '../commons/BaseComponent'

import * as React from 'react';
import * as ReactDOM from 'react-dom';

import AppState from '../commons/AppState';
import LookupService  from '../commons/LookupService';
import DataService from '../commons/httpService';
import { browserHistory, hashHistory } from 'react-router'
import {Layout} from '../index' 

import {Table, TableBody, TableRow, TableRowColumn} from 'material-ui/Table';

import {Tabs, Tab} from 'material-ui/Tabs';



import {atcDrugHeaders, createSchema, atcDrugUISchema} from './AtcDrug'





export class AtcDrugListWrapper extends React.Component<any, any> {

  render() {
    return (
      <Layout>
       <AtcDrugList/>
      </Layout>
    )
  }
}

export class AtcDrugList extends React.Component<any, any> {

  response: any

  constructor(props) {
    super(props);
    this.state = { response: {} };
    this.renderExtra = this.renderExtra.bind(this)
  }

  async load() {
    this.response = await DataService.load('atcDrugs');
    this.setState({ records: this.response.data.results })
  }

  componentDidMount() {
    console.log("waiting for atcDrugs")
    try {
      if(!this.props.records)
      	this.load();
    } catch (err) {
      this.response.data = []
      console.log(err);
    }
  }

  renderExtra(record: any) {
  	
  		
    if ( !( record.subcategories ) )
      return null;
      
     if ( !( record.subcategories.length ) )
      return null;

 
    return (<TableRow key={record.id + "E"}>
      <TableRowColumn colSpan={3} key='DET'> 
          <AtcDrugList records={record.subcategories} 
          nested={true}  
          container={'parent_displayName'}
          containerId={record.id}
           prev={this.props.location?this.props.location.pathName:null }
          
           />
		  
      
      </TableRowColumn>
    </TableRow>)
    
  }

 render() {
    
    let records = this.props.nested ? this.props.records : this.state.records

    if(!records )
      return (<p>Loading...</p>)

    return (
     
      <div>
        
        <SimpleList headers= {atcDrugHeaders} editLink={'AtcDrug'}
          renderExtra = {this.renderExtra}
          records = { records } nested={this.props.nested}
          container={this.props.container} uneditable={this.props.uneditable}
          containerId={this.props.containerId}
          prev={this.props.prev}
          />
      </div>
      
    )
  }
}

export class AtcDrugView extends EditViewBase {

  renderExtra(record: any) { <p> IN render </p> }
  
  constructor(props) {
    super(props);
    this.state = { record: {}, error: {}, message: {} };
    this.entityName = 'atcDrugs';
    //this.onSubmit = this.onSubmit.bind(this)
  }
  
  render() {
  
    let record = this.state.record
    return (
     <Layout>
       <SimpleView  headers= {atcDrugHeaders} renderExtra={this.renderExtra}
       record={record}   entityName='AtcDrug' /> 
       
       <Tabs>
       	  <Tab label="AtcDrug" >
          <AtcDrugList records={record.subcategories} 
          nested={true}  
          container={'parent_displayName'}
          containerId={record.id}
           prev={this.props.location?this.props.location.pathName:null }
          
           />
           </Tab>
		  
         </Tabs>
      </Layout>
    )	

  }
}


export const container = 'parent'



export class AtcDrugEdit extends EditViewBase {

  constructor(props) {
    super(props);
    this.state = { record: {}, error: {}, message: {} };
    this.entityName = 'atcDrugs';
    this.onSubmit = this.onSubmit.bind(this)
  }

  async onSubmit(formData) {
  	if(container &&  this.props.params.parent)
    	formData[container] = this.props.params.parent 
    try {
      await DataService.onSubmit('atcDrugs', formData)
      
      //if(!this.props.prev)
     hashHistory.push('/admin/AtcDrugList?msg=success')
      //else 
      // hashHistory.push(this.props.prev)
      
      //this.setState({ message: 'Record successfully created' })
    } catch (error) {
      console.log(error);
      this.setState({ error: error.response.data, record: formData })
    }
  }

  render() {
    return (
     <Layout>
      <div>
        {JSON.stringify(this.state.error) }
        <SimpleForm formData={this.state.record} currentError={this.state.error}
          formSchema={createSchema() }  uiSchema={atcDrugUISchema}
          onSubmit={this.onSubmit}  />
      </div>
     </Layout>
    );
  }
}

