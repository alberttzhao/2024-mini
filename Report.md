**Exercise 1:**

The max_bright value was 55,000 and the min_bright was 37,000.

**Exercise 2:**

Updated exercise_sound.py to play twinkle twinkle little star

**Exercise 3:**

Some of the changes we made to exercise_game.py include adding a scoring function, connecting the Pi Pico to the internet, and finally posting the json file to a firestone data base. Focusing in on the aspect that uploads the json to the cloud server, we first needed to connect the Pi Pico to the internet. We did this by using the network library and conncet8ing to BU Guest. From there we uploaded the json to teh firestone realtime database by http. We took the users email that they entered on the Thonny terminal and stored it in a folder. From there they could acess this folder using a web app we developed.

Below is a detailed description of how our mini-project works:
We set up a simple web application that allows users to enter an email address, checks whether data related to that email exists in a Firebase Real-time database, and if found, displays the associated information in a table format. If the email doesn’t exist, an appropriate error message is displayed. The project is built using React (for the front-end) and Firebase Realtime Database (for the back-end).

Front-End Setup(React):
- Email Input Form:
  • The user interface includes an input field where users can enter an email address in a normal format (e.g., user@domain.com).
	•	The form submission triggers a function that converts the email into a format compatible with the Firebase database (e.g., user-at-domain-dot-com) and fetches data for that email from the Firebase Realtime Database.
- Data Display Table:
  • If data exists for the given email, it is formatted and displayed in a clean table with specific columns: ID, Avg Response Time, Max Response Time, Min Response Time, Misses, and Score.
  •	If no data exists, a message is displayed to inform the user that no information is available for the given email.

React Components and Hooks:
  •	useState: Used to manage the component’s state, specifically to store the user’s input email, the fetched data, and any error messages.
  •	useEffect: Although not extensively used in this particular setup, useEffect can be used when side effects (such as data fetching or other asynchronous operations) need to be triggered on component render.

We also used HTML and CSS for website and data table styling 

React Components and Hooks:
- Firebase Project Configuration
	•	A Firebase project is set up through the Firebase Console, where the database is configured to store and retrieve data.
	•	The Firebase SDK is added to the React project via the firebase NPM package. The necessary Firebase libraries, such as firebase/app and firebase/database, are imported to handle database connections.
- Firebase Configuration in firebase.js:
	•	A firebase.js file is created in the React project to handle Firebase configuration and initialization.
	•	This file imports the Firebase app and database, initializes the Firebase app with configuration details (like apiKey, authDomain, and databaseURL), and exports a database object that allows interaction with the Realtime Database.

Steps:
- User enter email address
- Email conversation
- Firebase Query
- Data display
