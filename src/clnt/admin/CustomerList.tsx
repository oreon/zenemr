

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



import {customerHeaders, createSchema, customerUISchema} from './Customer'


	import { CustomerOrderList} from './CustomerOrderList';

	import { CustomerReviewList} from './CustomerReviewList';




export class CustomerListWrapper extends React.Component<any, any> {

  render() {
    return (
      <Layout>
       <CustomerList/>
      </Layout>
    )
  }
}

export class CustomerList extends React.Component<any, any> {

  response: any

  constructor(props) {
    super(props);
    this.state = { response: {} };
    this.renderExtra = this.renderExtra.bind(this)
  }

  async load() {
    this.response = await DataService.load('customers');
    this.setState({ records: this.response.data.results })
  }

  componentDidMount() {
    console.log("waiting for customers")
    try {
      if(!this.props.records)
      	this.load();
    } catch (err) {
      this.response.data = []
      console.log(err);
    }
  }

  renderExtra(record: any) {
  	
  		
    if ( !( record.customerOrders || record.customerReviews ) )
      return null;
      
     if ( !( record.customerOrders.length || record.customerReviews.length ) )
      return null;

 
    return (<TableRow key={record.id + "E"}>
      <TableRowColumn colSpan={3} key='DET'> 
          <CustomerOrderList records={record.customerOrders} 
          nested={true}  
          container={'customer_displayName'}
          containerId={record.id}
           prev={this.props.location?this.props.location.pathName:null }
          
           />
          <CustomerReviewList records={record.customerReviews} 
          nested={true}  
          container={'customer_displayName'}
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
        
        <SimpleList headers= {customerHeaders} editLink={'Customer'}
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

export class CustomerView extends EditViewBase {

  renderExtra() { <p> IN render EXTRA </p> }
  
  constructor(props) {
    super(props);
    this.entityName = 'customers';
    this.state = { record: {}, error: {}, message: {} };
    //this.onSubmit = this.onSubmit.bind(this)
  }
  
  render() {
  
    let record = this.state.record
    return (
     <Layout>
       <SimpleView  headers= {customerHeaders} renderExtra={this.renderExtra}
       record={record}  entityName='Customer' /> 
       
       <Tabs>
       	  <Tab label="CustomerOrder" >
          <CustomerOrderList records={record.customerOrders} 
          nested={true}  
          container={'customer_displayName'}
          containerId={record.id}
           prev={this.props.location?this.props.location.pathName:null }
          
           />
           </Tab>
       	  <Tab label="CustomerReview" >
          <CustomerReviewList records={record.customerReviews} 
          nested={true}  
          container={'customer_displayName'}
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



export class CustomerEdit extends EditViewBase {

  constructor(props) {
    super(props);
    this.state = { record: {}, error: {}, message: {} };
    this.entityName = 'customers';
    this.onSubmit = this.onSubmit.bind(this)
  }

  async onSubmit(formData) {
  	if(container &&  this.props.params.parent)
    	formData[container] = this.props.params.parent 
    try {
      await DataService.onSubmit('customers', formData)
      
      //if(!this.props.prev)
     hashHistory.push('/admin/CustomerList?msg=success')
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
          formSchema={createSchema() }  uiSchema={customerUISchema}
          onSubmit={this.onSubmit}  />
      </div>
     </Layout>
    );
  }
}

