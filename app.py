
   
import firebase_admin
from firebase_admin import credentials, db
from flask import Flask, jsonify

# Initialize Firebase app
cred = credentials.Certificate('bu-ec463-firebase-adminsdk-7c9mc-0618439ee9.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://bu-ec463-default-rtdb.firebaseio.com/'
})

app = Flask(__name__)

@app.route('/data', methods=['GET'])
def get_data():
    ref = db.reference('/path/to/data')
    data = ref.get()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
