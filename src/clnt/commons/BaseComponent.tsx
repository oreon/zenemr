import {observable} from 'mobx';
import {observer} from 'mobx-react';

import * as React from 'react';
import * as ReactDOM from 'react-dom';

import Form from 'react-jsonschema-form';

import DataService from './httpService';

import DevTools from 'mobx-react-devtools';

import { Router, Route, hashHistory, Link, browserHistory } from 'react-router'
import IconButton from 'material-ui/IconButton';

import RaisedButton from 'material-ui/FlatButton';
import FontIcon from 'material-ui/FontIcon';
import ActionAndroid from 'material-ui/svg-icons/action/android';

import Divider from 'material-ui/Divider';

import {Card, CardActions, CardHeader, CardMedia, CardTitle, CardText} from 'material-ui/Card';

import * as _  from 'lodash';

import {customerOrderHeaders} from '../admin/CustomerOrder'
import {orderItemHeaders} from '../admin/OrderItem'

import {Table, TableBody, TableHeader, TableHeaderColumn, TableRow, TableRowColumn} from 'material-ui/Table';



export class SimpleView extends React.Component<any, any>{
  render() {

    let current = this.props.record;

    let vals = this.props.headers.map
      (x => { return <div key={x.property}> <b> {x.property} </b>: {current[x.property]}</div> });

    if (!current) {
      return <p> No Record Selected </p>
    } else {

      return (
      
         <Card>
          <CardHeader   title={current['displayName']}>  </CardHeader>
          <CardActions>
        <RaisedButton onClick={() => hashHistory.push('/admin/' + this.props.entityName + 'Edit/' + current.id) }>Edit</RaisedButton>
        <RaisedButton onClick={() => this.props.data.gotoList() }>Cancel</RaisedButton>
          </CardActions>
        <CardText>  
        {vals}
        </CardText>
        { this.props.renderExtra(current) }
      </Card>
      )
    }
    //return null;
  }
}


export class SimpleList extends React.Component<any, any>{

  baseLink: string;

  constructor(props) {
    super(props);
    
    this.baseLink = '/admin/' + this.props.editLink 
  }

  renderRow(record: any, headers) {

   let cells = headers.map(x =>
    { return <TableRowColumn  key={x.property}> {record[x.property]} </TableRowColumn> });
    let prnt = (this.props.parent) ?   "/" + this.props.parent :  ""
    let editLink = this.baseLink + "Edit/" + record.id + prnt;
    let viewLink = this.baseLink + "View/" + record.id 
    

    return (
      <TableRow  key={record.id}>
        {cells}
         {(!this.props.uneditable) && 
        <TableRowColumn key='edit'> 
        <Link to={{pathname: editLink, query: { prev: this.props.prev }}}>Edit</Link>
        <Link to={{pathname: viewLink, query: { prev: this.props.prev }}}>View</Link>
         </TableRowColumn>
         }
      </TableRow>
    )
  }

  renderExtra(record: any) {
    return this.props.renderExtra(record)
  } 

  render() {

    let styles = this.getStyles();

     let headers = this.props.headers
    .filter( x => { return x.property != this.props.container } )
    
     let ths = headers.map(x => { return <TableHeaderColumn key={x.property}>{x.title} </TableHeaderColumn> });

    let mainrows = this.props.records.map(customer => this.renderRow(customer, headers));

    let extras = this.props.records.map(customer => this.renderExtra(customer));

    let rows = _.zip(mainrows, extras)

    let addLink = this.baseLink;

    if(this.props.containerId){
      addLink = "#" + this.baseLink + "Edit/0/" + this.props.containerId
    }

    return (

      <div>
        
        {this.props.renderExtra({}) }

        {(!this.props.uneditable) && 
        <RaisedButton href={addLink} label="Add New"  linkButton={true} />
        }
      
        <br/>

         {(this.props.records.length > 0 ) &&
        <Table>
           <TableHeader displaySelectAll={false}  style={styles.header}>
              <TableRow key="this.props.headers"   >
              {ths}
            </TableRow>
           </TableHeader>
          <TableBody showRowHover={true}  displayRowCheckbox={false} stripedRows={this.props.nested} >
            {rows}
          </TableBody>
        </Table>
        }
        {(this.props.records.length == 0 ) &&  <p> No records </p> }
                  
      </div>
    )
  }

  getStyles () {
    return {
      root: {
       // paddingTop: Spacing.desktopKeylineIncrement
      },
      header: {
        fontWeight: 'normal',
        fontSize: 13,
        background: this.props.nested ? 'lightblue': 'lightgreen'
      },
      headerRight: {
        fontWeight: 'normal',
        fontSize: 13,
       // paddingLeft: scrollBarVisible ? 24 - (window.scrollbarWidth / 2) : 24
      },
      row: {
        borderBottom: '0px'
      }
    }
  }
}


export class EditViewBase extends React.Component<any, any> {

  entityName:string
    
    async componentDidMount() {
        let id = this.props.params.id
        if ( id && id > 0 ) {
          console.log(id)
          try {
            this.setState({
              record: await DataService.loadById(this.entityName,id)
            })
          } catch (error) {
            console.log(error);
            this.setState({ error: error })
          }
        }
  }
}


//@observer
export class SimpleForm extends React.Component<any, any>{

  constructor(props) { super(props); }

  render() {

    return (

      <div className="panel panel-default">

        <p>   </p>
        <Form schema={this.props.formSchema}
          formData={this.props.formData }
          uiSchema  = {this.props.uiSchema }
          onSubmit={({formData}) => this.props.onSubmit(formData) }
          >
          <div>
            <button type="submit" className="button">Submit</button>
            <button className="button" onClick={() => console.log('cancel') }>Cancel</button>
          </div>
        </Form>

      </div>
    );
  }
}

export class Nested extends React.Component<any, any>{

  constructor(props) { super(props); }

  render() {

    return (
      <p> {this.props.name}  </p>
    )
  }
}