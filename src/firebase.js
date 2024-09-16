import { initializeApp } from "firebase/app";
import { getDatabase } from 'firebase/database'

const firebaseConfig = {
  apiKey: "AIzaSyCvUsgQn12D_CUp8rYXYGNV5QdgYlwd5nQ",
  authDomain: "bu-ec463.firebaseapp.com",
  databaseURL: "https://bu-ec463-default-rtdb.firebaseio.com",
  projectId: "bu-ec463",
  storageBucket: "bu-ec463.appspot.com",
  messagingSenderId: "449756616509",
  appId: "1:449756616509:web:269a7e69fcfb7236b85754"
};

const app = initializeApp(firebaseConfig);
const database = getDatabase(app);

export { database };