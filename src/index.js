// import React from 'react';
// import ReactDOM from 'react-dom';
// import App from './App';
// 
// ReactDOM.render(
//   <React.StrictMode>
//     <App />
//   </React.StrictMode>,
//   document.getElementById('root')
// );


// below I have to create a new way to use without reactDOM becuase it was throwing errors on the console
// and using react 18+ gets rid of it
import React from 'react';
import { createRoot } from 'react-dom/client';
import App from './App';

const container = document.getElementById('root');
const root = createRoot(container);  // create root for React 18+
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);