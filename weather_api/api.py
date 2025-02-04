from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, jsonify, current_app
)
from werkzeug.exceptions import abort

import json
import logging

from data_models.weather_data_schema import WeatherDataSchema
from weather_data_repository import Repository

logger = logging.getLogger(__name__)
logging.basicConfig(filename="", level=logging.INFO, format='%(asctime)s %(message)s')

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

	json_data = json.loads(json_data)

	data = prepare_data_for_db(json_data)

	if sql._connection_status:
		sql.insert_data(data)
		return jsonify("Result: Success")
	else:
		# handle error.
		return jsonify("Result: Absolute Failure")
	
def prepare_data_for_db(json_data):
	ordered_field_list = [
		"Timestamp",
		"Outdoor Temperature",
		"Outdoor Humidity",
		"Dew Point",
		"Heat Index",
		"Wind Chill",
		"Barometric Pressure",
		"Rain",
		"Wind Speed",
		"Wind Average",
		"Peak Wind",
		"Wind Direction",
		"Indoor Temperature",
		"Indoor Humidity",
		"TimestampDateOnly"
		]
	
	output = []

	for item in json_data:
		row = []
		for field in ordered_field_list:
			row.append(item[field])
		output.append(row)

	return output
		