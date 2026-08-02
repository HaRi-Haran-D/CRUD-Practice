// import { useEffect, useState } from "react";
// import axios from "axios";

// function App() {
//   const [date, setData] = useState("");
//   const [startTime, setStartTime] = useState("");
//   const [endTime, setEndTime] = useState("");
//   const [getData, setGetData] = useState([])

//   async function handleSubmit(e) {
//     e.preventDefault();

//     console.log(`data${date} starttime ${startTime} endtime ${endTime}`);
//     try {
//       const res = await axios({
//         method: "POST",
//         url: "http://localhost:8000/book/",
//         data: {
//           booking_date: date,
//           start_time: startTime,
//           end_time: endTime,
//         },
//       });
//       console.log(res);
//     } catch (error) {
//       console.log(error);
//     }
//   }

//   async function handlegetData() {
//     try {
//       const res = await axios({
//         method: "GET",
//         url: "http://localhost:8000/book/",
//       });
//       console.log(res);
//       setGetData(res.data)

//     } catch (error) {
//       console.log(error);
//     }
//   }

//   useEffect(() => {
//     handlegetData();
//   }, []);

//   return (
//     <>
//       <div>
//         <form onSubmit={(e) => handleSubmit(e)}>
//           <input
//             type="date"
//             value={date}
//             onChange={(e) => setData(e.target.value)}
//             placeholder="Enter Booking Date"
//           />
//           <input
//             type="time"
//             value={startTime}
//             onChange={(e) => setStartTime(e.target.value)}
//             placeholder="Enter Start Time"
//           />
//           <input
//             type="time"
//             value={endTime}
//             onChange={(e) => setEndTime(e.target.value)}
//             placeholder="Enter End Time"
//           />
//           <input type="submit" />
//         </form>
//       </div>
//       <div>
//     <div style={{display: "grid", gridTemplateColumns: "repeat(3, 1fr)", gap: "10px", width: "100%"}}>
//   {getData.map((e, i) => (
//     <div key={i} style={{border: "1px solid black", padding: "10px"}}
//     >
//       <h1>room number: {e.room_no}</h1>
//       <h1>booking date: {e.booking_date}</h1>
//       <h1>starting time: {e.start_time}</h1>
//       <h1>end time: {e.end_time}</h1>
//     </div>
//   ))}
// </div>
//       </div>
//     </>
//   );
// }

// export default App;

import React from 'react'
import Button from './components/Button'

const App = () => {
  return (
    <>
    <Button />
    </>
  )
}

export default App