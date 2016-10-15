//@observer
//export default class BaseCrudComponent extends React.Component<any, any> {
//
//  //customerStore: AppState
//
//  constructor(props) {
//    console.log("rcvd schema " + props.data.formSchema)
//    super(props);
//  }
//
//  componentDidMount() { }
//
//  render() {
//    return (
//      <div className="panel">
//        <DevTools />
//        {this.props.data.mode}
//
//        { (this.props.data.mode == 'L') &&
//          <CustomerList data={this.props.data} nestedRecords={this.props.nestedRecords}/>
//        }
//
//        {(this.props.data.mode == 'V') &&
//          <CustomerView data={this.props.data}/>
//        }
//
//        {(this.props.data.mode == 'E') &&
//          <CustomerForm  data={this.props.data}/>
//        }
//      </div>
//    )
//  }
//}
//
//// export class TableHeader extends React.Component<any, any>{
////   render() {
////     return <TableHeaderColumn> {this.props.name} </TableHeaderColumn>
////   }
//// }
//
//@observer
//export class CustomerList extends React.Component<any, any>{
//
//  constructor(props) { super(props); }
//
//  renderRow(record: any) {
//    let cells = this.props.data.headers.map(x =>
//    { return <TableRowColumn  key={x.property}> {record[x.property]} </TableRowColumn> });
//
//    return (
//      <TableRow>
//        {cells}
//        <TableRowColumn> <button onClick={() => this.props.data.selectPost(record) }
//          >Edit Me</button></TableRowColumn>
//        <TableRowColumn> <button onClick={() => this.props.data.selectPostView(record) }
//          >View</button></TableRowColumn>
//      </TableRow>
//    )
//  }
//
//  renderExtra(record: any) {
//    return (<TableRow key={record.id + "C"}>
//      <TableRowColumn> hi there </TableRowColumn>  <TableRowColumn> {record.displayName} </TableRowColumn>
//    </TableRow>)
//  }
//
//  render() {
//
//    let headers = this.props.data.headers.map(x => { return <TableHeaderColumn key={x.property}>{x.title} </TableHeaderColumn> });
//
//    let arr = this.props.nestedRecords ? this.props.nestedRecords : this.props.data.posts
//    let rows = arr.map(customer => {
//      return this.renderRow(customer)
//    });
//
//    let extras = arr.map(customer => {
//      return this.renderExtra(customer)
//    });
//
//    let rowsWithDet = _.zip(rows, extras)
//
//    return (
//      <div>
//        <button onClick={() => this.props.data.selectPost({}) } >
//          Add
//        </button>
//
//        <Table  className="table-striped" >
//          <TableHeader
//            displaySelectAll={false}>
//            <TableRow>
//              {headers}
//            </TableRow>
//          </TableHeader>
//          <TableBody displayRowCheckbox={false}>
//            {rows}
//          </TableBody>
//        </Table>
//
//        {  (this.props.data.next != null) &&
//          <a  onClick={this.props.data.goNext }> Next </a>  }
//        { (this.props.data.prev != null) &&
//          <a onClick={this.props.data.goPrev}> Prev </a> }
//      </div>
//    )
//  }
//}
//
//
//export const oi = [
//
//  { property: "customerOrder", title: "Customer Order" }
//  ,
//  { property: "qty", title: "Qty" }
//  ,
//  { property: "product", title: "Product" }
//
//]
//
//
//@observer
//export class CustomerView extends React.Component<any, any>{
//
//  constructor(props) { super(props); }
//
//  render() {
//
//    let current = this.props.data.selectedPost;
//
//    let vals = this.props.data.headers.map
//      (x => { return <div key={x.property}> <b> {x.property} </b>: {current[x.property]}</div> });
//
//    if (!current) {
//      return <p> No Record Selected </p>
//    }
//
//    if (current.customerOrders) {
//      //this.orders.posts = this.props.data.selectedPost.customerOrders
//      return (
//        <div>
//          {vals}
//
//          <SimpleList headers={customerOrderHeaders}  parent={this.props.data.selectedPost.id}
//            records={this.props.data.selectedPost.customerOrders}/>
//
//          <RaisedButton onClick={() => this.props.data.gotoEdit() }>Edit</RaisedButton>
//          <RaisedButton onClick={() => this.props.data.gotoList() }>Cancel</RaisedButton>
//
//        </div>
//
//      );
//    }
//    return null;
//  }
//
//}
//
////var History = Router.History;
//
//@observer
//export class CustomerForm extends React.Component<any, any>{
//
//  constructor(props) { super(props); }
//
//
//  render() {
//
//    return (
//
//      <div className="panel panel-default">
//
//        <p> {this.props.data.currentError}  </p>
//        <Form schema={this.props.data.formSchema}
//          formData={this.props.data.selectedPostJS() }
//          uiSchema  = {this.props.data.uiSchemaJS() }
//          onSubmit={({formData}) => this.props.data.onSubmit(formData) }
//          >
//          <div>
//            <button type="submit" className="button">Submit</button>
//            <button className="button" onClick={() => { hashHistory.goBack } }> Cancel</button>
//          </div>
//        </Form>
//
//      </div>
//    );
//  }
//}
