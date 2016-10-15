

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



import {frequencyHeaders, createSchema, frequencyUISchema} from './Frequency'





export class FrequencyListWrapper extends React.Component<any, any> {

  render() {
    return (
      <Layout>
       <FrequencyList/>
      </Layout>
    )
  }
}

export class FrequencyList extends React.Component<any, any> {

  response: any

  constructor(props) {
    super(props);
    this.state = { response: {} };
    this.renderExtra = this.renderExtra.bind(this)
  }

  async load() {
    this.response = await DataService.load('frequencys');
    this.setState({ records: this.response.data.results })
  }

  componentDidMount() {
    console.log("waiting for frequencys")
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
        
        <SimpleList headers= {frequencyHeaders} editLink={'Frequency'}
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

export class FrequencyView extends EditViewBase {

  renderExtra(record: any) { <p> IN render </p> }
  
  constructor(props) {
    super(props);
    this.state = { record: {}, error: {}, message: {} };
    this.entityName = 'frequencys';
    //this.onSubmit = this.onSubmit.bind(this)
  }
  
  render() {
  
    let record = this.state.record
    return (
     <Layout>
       <SimpleView  headers= {frequencyHeaders} renderExtra={this.renderExtra}
       record={record}   entityName='Frequency' /> 
       
       <Tabs>
        
         </Tabs>
      </Layout>
    )	

  }
}


export const container = null



export class FrequencyEdit extends EditViewBase {

  constructor(props) {
    super(props);
    this.state = { record: {}, error: {}, message: {} };
    this.entityName = 'frequencys';
    this.onSubmit = this.onSubmit.bind(this)
  }

  async onSubmit(formData) {
  	if(container &&  this.props.params.parent)
    	formData[container] = this.props.params.parent 
    try {
      await DataService.onSubmit('frequencys', formData)
      
      //if(!this.props.prev)
     hashHistory.push('/admin/FrequencyList?msg=success')
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
          formSchema={createSchema() }  uiSchema={frequencyUISchema}
          onSubmit={this.onSubmit}  />
      </div>
     </Layout>
    );
  }
}

