## Exercise 1

- The `max_bright` value was **55,000**, and the `min_bright` value was **37,000**.

## Exercise 2

- Updated `exercise_sound.py` to play *Twinkle Twinkle Little Star*.

# Exercise 3

## Mini-Project Overview

This mini-project demonstrates how to set up and use a simple web application that allows users to enter an email address, check whether data associated with that email exists in a Firebase Realtime Database, and display the information in a formatted table. If no data is found, an appropriate error message is displayed. The project uses **React** for the front-end and **Firebase Realtime Database** for the back-end.

### Changes to `exercise_game.py`:

- **Scoring Function**: Added a scoring mechanism.
- **Internet Connectivity**: Connected the Pi Pico to the internet using the `network` library and connected to the **BU Guest** network.
- **Cloud Upload**: We posted a JSON file to a Firestore Realtime Database using HTTP.

### Uploading JSON to the Cloud:

- The user enters their email via the Thonny terminal, which is then stored in a designated folder.
- This folder is accessible through a web app we developed, allowing users to view their data.

---

## Detailed Description of the Mini-Project

We set up a simple web application that allows users to enter an email address, checks whether data related to that email exists in a Firebase Realtime Database, and if found, displays the associated information in a table format. If the email doesn’t exist, an appropriate error message is displayed.

The project consists of the following main components:

### Front-End Setup (React)

#### Email Input Form:

- The user interface includes an input field where users can enter an email address in a normal format (e.g., `user@domain.com`).
- When the form is submitted, a function converts the email into a format compatible with Firebase (e.g., `user-at-domain-dot-com`) and fetches the data associated with that email from the Firebase Realtime Database.


#### Data Display Table:

- If data exists for the given email, it is formatted and displayed in a clean table with specific columns: **ID**, **Avg Response Time**, **Max Response Time**, **Min Response Time**, **Misses**, and **Score**.
- If no data exists, a message is displayed to inform the user that no information is available for the given email.
<img width="1511" alt="IMG_4254" src="https://github.com/user-attachments/assets/29de5c5e-e82c-40cd-91c5-e8b2e3c88837">


### React Components and Hooks

- **useState**: Manages the component’s state, specifically to store the user’s input email, the fetched data, and any error messages.
- **useEffect**: Can be used for side effects like fetching data when the component renders, though it isn't heavily used in this setup.

We also used **HTML** and **CSS** for basic website and data table styling.

---

### Firebase Configuration

#### Firebase Project Configuration:

- A Firebase project is set up through the **Firebase Console**, where the database is configured to store and retrieve data.
- The Firebase SDK is added to the React project via the `firebase` NPM package. Firebase libraries such as `firebase/app` and `firebase/database` are imported to handle database connections.

#### Firebase Configuration in `firebase.js`:

- A `firebase.js` file is created in the React project to handle Firebase configuration and initialization.
- This file imports the Firebase app and database, initializes Firebase with configuration details like `apiKey`, `authDomain`, and `databaseURL`, and exports a `database` object that allows interaction with the Realtime Database.

---

## Application Workflow

1. **User Enters Email Address**:
2. **Email Conversion**:
3. **Firebase Query**:
4. **Data Display**:
---

## Video Demonstration: 
