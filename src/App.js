import React, { useState } from 'react';
import { ref, get, child } from 'firebase/database';  
import { database } from './firebase'; 

function App() {
  const [data, setData] = useState(null);  // store the data fetched from firebase
  const [email, setEmail] = useState('');  // store the user's input
  const [error, setError] = useState('');  // store any error messages

  // function to convert the email into firebase format
  // for example, "albertz@bu.edu" -> "albertz-at-bu-dot-edu"
  const formatEmailForFirebase = (email) => {
    return email.replace(/@/g, '-at-').replace(/\./g, '-dot-');
  };

  // function to fetch data when the form is submitted
  const fetchData = async (e) => {
    e.preventDefault();  
    setError('');  

    try {
      const formattedEmail = formatEmailForFirebase(email);  // convert email to firebase format
      const dbRef = ref(database);
      const snapshot = await get(child(dbRef, `/${formattedEmail}`));  // query the database

      if (snapshot.exists()) {
        const firebaseData = snapshot.val();
        setData(Object.keys(firebaseData).map(key => ({
          id: key,
          ...firebaseData[key]
        })));
      } else {
        setData(null);  
        setError('User does not exist'); // if the user is not found, so not in the database, error message
      }
    } catch (error) {
      console.error('Error fetching data:', error);
      setError('Something went wrong');  // other generic error message
    }
  };

  return ( // so below i just made some html and css to make the webpage look more friendly
    <div className="App" style={{ fontFamily: 'Arial, sans-serif', padding: '20px' }}>
      <h1 style={{ color: '#333' }}>Check User Data</h1>

      {/* form for inputting email */}
      <form onSubmit={fetchData} style={{ marginBottom: '20px' }}>
        <label style={{ marginRight: '10px' }}>
          Enter email:
          <input
            type="text"
            value={email}
            onChange={(e) => setEmail(e.target.value)}  // update the email state on input change
            placeholder="Enter email address"
            required
            style={{
              padding: '5px',
              fontSize: '16px',
              marginLeft: '10px',
              borderRadius: '4px',
              border: '1px solid #ccc',
            }}
          />
        </label>
        <button type="submit" style={{
          padding: '5px 10px',
          fontSize: '16px',
          borderRadius: '4px',
          border: 'none',
          backgroundColor: '#007BFF',
          color: 'white',
          cursor: 'pointer'
        }}>
          Fetch Data
        </button>
      </form>

      {/* display error if user doesn't exist */}
      {error && <p style={{ color: 'red' }}>{error}</p>} {/* set it to color red */}

      {/* display the fetched data from firebase as a table */}
      {data && (
        <div>
          <h2>Data for {email}:</h2>
          <table style={{
            width: '100%',
            borderCollapse: 'collapse',
            marginTop: '10px'
          }}>
            <thead>
              <tr>
                <th style={tableHeaderStyle}>ID</th>
                <th style={tableHeaderStyle}>Avg Response Time</th>
                <th style={tableHeaderStyle}>Max Response Time</th>
                <th style={tableHeaderStyle}>Min Response Time</th>
                <th style={tableHeaderStyle}>Misses</th>
                <th style={tableHeaderStyle}>Score</th>
              </tr>
            </thead>
            <tbody>
              {data.map((entry) => (
                <tr key={entry.id}>
                  <td style={tableCellStyle}>{entry.id}</td>
                  <td style={tableCellStyle}>{entry.avg_response_time}</td>
                  <td style={tableCellStyle}>{entry.max_response_time}</td>
                  <td style={tableCellStyle}>{entry.min_response_time}</td>
                  <td style={tableCellStyle}>{entry.misses}</td>
                  <td style={tableCellStyle}>{entry.score}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}

// so im creating some styles for table headers and cells
const tableHeaderStyle = {
  padding: '10px',
  borderBottom: '2px solid #ddd',
  backgroundColor: '#f4f4f4',
  textAlign: 'left',
};

const tableCellStyle = {
  padding: '10px',
  borderBottom: '1px solid #ddd',
};

export default App;