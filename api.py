from flask import Flask, jsonify
from flask_cors import CORS
import requests
url = 'https://umdearborn.campuslabs.com/engage/api/discovery/event/search?endsAfter=2024-10-22T18%3A04%3A48-04%3A00&orderByField=endsOn&orderByDirection=ascending&status=Approved&take=15&benefitNames%5B0%5D=FreeFood&query='

app = Flask(__name__)
CORS(app)

@app.route('/api/hello', methods=['GET'])
def hello():
    try:
    # Send GET request to the URL
        response = requests.get(url)
    
    # Check if the request was successful (status code 200)
        if response.status_code == 200:
        # Parse the response as JSON
            data = response.json()
            print(data)
            resp = jsonify({
                'status': 'success',
                'data': data.get('value')
            })
            resp.headers.add('Access-Control-Allow-Origin', '*')
            return jsonify({
                'status': 'success',
                'data': data.get('value')
            })
            
            # Display the data
        else:
            return jsonify({
                'status': 'error',
                'message': f'Failed to fetch data. Status code: {response.status_code}'
            }), response.status_code

    except requests.exceptions.RequestException as e:
    # Handle any exceptions that occur during the request
        return jsonify({
            'status': 'error',
            'message': f'An error occurred: {e}'
        }), 500

if __name__ == '__main__':
    app.run(debug=True)