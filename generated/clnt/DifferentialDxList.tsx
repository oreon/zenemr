

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



import {differentialDxHeaders, createSchema, differentialDxUISchema} from './DifferentialDx'





export class DifferentialDxListWrapper extends React.Component<any, any> {

  render() {
    return (
      <Layout>
       <DifferentialDxList/>
      </Layout>
    )
  }
}

export class DifferentialDxList extends React.Component<any, any> {

  response: any

  constructor(props) {
    super(props);
    this.state = { response: {} };
    this.renderExtra = this.renderExtra.bind(this)
  }

  async load() {
    this.response = await DataService.load('differentialDxs');
    this.setState({ records: this.response.data.results })
  }

  componentDidMount() {
    console.log("waiting for differentialDxs")
    try {
      if(!this.props.records)
      	this.load();
    } catch (err) {
      this.response.data = []
      console.log(err);
    }
  }

  renderExtra(record: any) {
  	
  		return null
  	
  }

 render() {
    
    let records = this.props.nested ? this.props.records : this.state.records

    if(!records )
      return (<p>Loading...</p>)

    return (
     
      <div>
        
        <SimpleList headers= {differentialDxHeaders} editLink={'DifferentialDx'}
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

export class DifferentialDxView extends EditViewBase {

  renderExtra(record: any) { <p> IN render </p> }
  
  constructor(props) {
    super(props);
    this.state = { record: {}, error: {}, message: {} };
    this.entityName = 'differentialDxs';
    //this.onSubmit = this.onSubmit.bind(this)
  }
  
  render() {
  
    let record = this.state.record
    return (
     <Layout>
       <SimpleView  headers= {differentialDxHeaders} renderExtra={this.renderExtra}
       record={record}   entityName='DifferentialDx' /> 
       
       <Tabs>
        
         </Tabs>
      </Layout>
    )	

  }
}


export const container = 'finding'



export class DifferentialDxEdit extends EditViewBase {

  constructor(props) {
    super(props);
    this.state = { record: {}, error: {}, message: {} };
    this.entityName = 'differentialDxs';
    this.onSubmit = this.onSubmit.bind(this)
  }

  async onSubmit(formData) {
  	if(container &&  this.props.params.parent)
    	formData[container] = this.props.params.parent 
    try {
      await DataService.onSubmit('differentialDxs', formData)
      
      //if(!this.props.prev)
     hashHistory.push('/admin/DifferentialDxList?msg=success')
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
          formSchema={createSchema() }  uiSchema={differentialDxUISchema}
          onSubmit={this.onSubmit}  />
      </div>
     </Layout>
    );
  }
}

