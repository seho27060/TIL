import { useSelector, useDispatch } from 'react-redux'

import { counterActions } from '../store/counter';
import classes from './Counter.module.css';

const Counter = () => {
  const dispatch = useDispatch()
  const counter = useSelector(state => state.counter.counter)
  const show = useSelector(state => state.counter.showCounter)

  const InclementHandler = () => {
    dispatch(counterActions.increment())
  }
  const IncreaseHandler = () => {
    dispatch(counterActions.increase(10))
  }
  const declementHandler = () => {
    dispatch(counterActions.decrement())
  }
  const toggleCounterHandler = () => {
    dispatch(counterActions.toggleCounter())
  };

  return (
    <main className={classes.counter}>
      <h1>Redux Counter</h1>
      {show && <div className={classes.value}>{counter}</div>}
     <div>
     <button onClick={InclementHandler}>Inclement</button>
     <button onClick={IncreaseHandler}>Inclement by 5</button>
     <button onClick={declementHandler}>Declement</button>
      </div> 
      <button onClick={toggleCounterHandler}>Toggle Counter</button>
    </main>
  );
};
export default Counter 


//////// 함수형 컴포넌트 참조
// import { Component } from 'react';
// import { connect } from 'react-redux'

// class Counter extends Component{
//   InclementHandler() {
//     this.props.inclement()
//   }
  
//   declementHandler() {
//     this.props.declement()
//   }
  
//   toggleCounterHandler() {}

//   render() {
//     return (
//       <main className={classes.counter}>
//         <h1>Redux Counter</h1>
//         <div className={classes.value}>{this.props.counter}</div>
//        <div>
//        <button onClick={this.InclementHandler.bind(this)}>Inclement</button>
//        <button onClick={this.declementHandler.bind(this)}>Declement</button>
//         </div> 
//         <button onClick={this.toggleCounterHandler}>Toggle Counter</button>
//       </main>
//     );
//   }
// }

// const mapStateToProps = state => {
//   return {
//     counter : state.counter,
//   }
// }

// const mapDispatchToProps = dispatch => {
//   return {
//     inclement : () => dispatch({type:'inclement'}),
//     declement : () => dispatch({type:'declement'}),
//   }
// }
// export default connect(mapStateToProps,mapDispatchToProps)(Counter);
