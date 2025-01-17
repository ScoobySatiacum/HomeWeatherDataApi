# Using flask to make an api 
# import necessary libraries and functions 
from flask import Flask, jsonify, request 

from weather_data_repository import Repository

# creating a Flask app 
app = Flask(__name__) 

# on the terminal type: curl http://127.0.0.1:5000/ 
# returns weather data api when we use GET. 
# returns the data that we send when we use POST. 
@app.route('/', methods = ['GET', 'POST']) 
def home(): 
	if(request.method == 'GET'): 

		data = "weather data API."
		return jsonify({'data': data}) 

@app.route('/weather/current', methods = ['GET']) 
def current(): 
    
	sql = Repository("/srv/weather_data_api/weather_data.sqlite")
	success, data = sql.current_weather()
	if success:
		return jsonify(data)

# driver function 
if __name__ == '__main__': 

	app.run(debug = True) 
