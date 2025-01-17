from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, jsonify, current_app
)
from werkzeug.exceptions import abort
from pprint import pprint

import json

from data_models.weather_data_schema import WeatherDataSchema
from weather_data_repository import Repository

bp = Blueprint('api', __name__)

sql = Repository(current_app.config['DATABASE'])

@bp.route('/', methods = ['GET']) 
def home(): 
	if(request.method == 'GET'): 

		data = "weather data API."
		return jsonify({'data': data}) 

@bp.route('/weather/current', methods = ['GET']) 
def current(): 
	success, data = sql.current_weather()
	if success:
		return jsonify(data)
	
@bp.route('/weather/add', methods= ['POST'])
def add():

	json_data = request.json

	data = prepare_data_for_db(json_data)

	# for item in json_data:
	# 	schema = WeatherDataSchema()
	# 	result = schema.load(item)

	# 	data.append(result)

	print(data)

	if sql._connection_status:
		sql.insert_data(data)
	else:
		# handle error.
		return jsonify("Result: Absolute Failure")
	
def prepare_data_for_db(json_data):
	ordered_field_list = [
		"timestamp",
		"outdoortemperature",
		"outdoorhumidity",
		"dewpoint",
		"heatindex",
		"windchill",
		"barometricpressure",
		"rain",
		"windspeed",
		"windaverage",
		"peakwind",
		"winddirection",
		"indoortemperature",
		"indoorhumidity",
		"timestampdateonly"
		]
	
	output = []

	for item in json_data:
		row = []
		for field in ordered_field_list:
			row.append(item[field])
		output.append(row)

	return output
		