

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



import {labFindingHeaders, createSchema, labFindingUISchema} from './LabFinding'


	import { DifferentialDxList} from './DifferentialDxList';




export class LabFindingListWrapper extends React.Component<any, any> {

  render() {
    return (
      <Layout>
       <LabFindingList/>
      </Layout>
    )
  }
}

export class LabFindingList extends React.Component<any, any> {

  response: any

  constructor(props) {
    super(props);
    this.state = { response: {} };
    this.renderExtra = this.renderExtra.bind(this)
  }

  async load() {
    this.response = await DataService.load('labFindings');
    this.setState({ records: this.response.data.results })
  }

  componentDidMount() {
    console.log("waiting for labFindings")
    try {
      if(!this.props.records)
      	this.load();
    } catch (err) {
      this.response.data = []
      console.log(err);
    }
  }

  renderExtra(record: any) {
  	
  		
    if ( !( record.differentialDxs ) )
      return null;
      
     if ( !( record.differentialDxs.length ) )
      return null;

 
    return (<TableRow key={record.id + "E"}>
      <TableRowColumn colSpan={3} key='DET'> 
          <DifferentialDxList records={record.differentialDxs} 
          nested={true}  
          container={'finding_displayName'}
          containerId={record.id}
           prev={this.props.location?this.props.location.pathName:null }
           uneditable={true} 
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
        
        <SimpleList headers= {labFindingHeaders} editLink={'LabFinding'}
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

export class LabFindingView extends EditViewBase {

  renderExtra(record: any) { <p> IN render </p> }
  
  constructor(props) {
    super(props);
    this.state = { record: {}, error: {}, message: {} };
    this.entityName = 'labFindings';
    //this.onSubmit = this.onSubmit.bind(this)
  }
  
  render() {
  
    let record = this.state.record
    return (
     <Layout>
       <SimpleView  headers= {labFindingHeaders} renderExtra={this.renderExtra}
       record={record}   entityName='LabFinding' /> 
       
       <Tabs>
       	  <Tab label="DifferentialDx" >
          <DifferentialDxList records={record.differentialDxs} 
          nested={true}  
          container={'finding_displayName'}
          containerId={record.id}
           prev={this.props.location?this.props.location.pathName:null }
           uneditable={true} 
           />
           </Tab>
		  
         </Tabs>
      </Layout>
    )	

  }
}


export const container = null



export class LabFindingEdit extends EditViewBase {

  constructor(props) {
    super(props);
    this.state = { record: {}, error: {}, message: {} };
    this.entityName = 'labFindings';
    this.onSubmit = this.onSubmit.bind(this)
  }

  async onSubmit(formData) {
  	if(container &&  this.props.params.parent)
    	formData[container] = this.props.params.parent 
    try {
      await DataService.onSubmit('labFindings', formData)
      
      //if(!this.props.prev)
     hashHistory.push('/admin/LabFindingList?msg=success')
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
          formSchema={createSchema() }  uiSchema={labFindingUISchema}
          onSubmit={this.onSubmit}  />
      </div>
     </Layout>
    );
  }
}

