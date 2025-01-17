from marshmallow import Schema, fields

class WeatherDataSchema(Schema):
    id = fields.Int()
    timestamp = fields.DateTime(format="%m/%d/%Y %I:%M:%S %p")
    outdoortemperature = fields.Float()
    outdoorhumidity = fields.Int()
    dewpoint = fields.Int()
    heatindex = fields.Int()
    windchill = fields.Int()
    barometricpressure = fields.Float()
    rain = fields.Float()
    windspeed = fields.Float()
    windaverage = fields.Float()
    peakwind = fields.Float()
    winddirection = fields.Float()
    indoortemperature = fields.Float()
    indoorhumidity = fields.Int()
    timestampdateonly = fields.DateTime(format="%m-%d-%Y")