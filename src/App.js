import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [data, setData] = useState(null);
  const [key, setKey] = useState('example-key');  // Set default key here

  useEffect(() => {
    axios.get(`http://localhost:5000/get-data/${key}`)
      .then(response => setData(response.data))
      .catch(error => console.error('Error fetching data:', error));
  }, [key]);

  return (
    <div className="App">
      <h1>Data from Firebase:</h1>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </div>
  );
}

export default App;
