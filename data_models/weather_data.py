from dataclasses import dataclass, field
import datetime as dt

@dataclass
class WeatherData:
    timestamp: dt.datetime = field(default_factory=dt.datetime.now)
    outdoortemperature: float
    outdoorhumidity: int
    dewpoint: int
    heatindex: int
    windchill: int
    barometricpressure: float
    rain: float
    windspeed: float
    windaverage: float
    peakwind: float
    winddirection: float
    indoortemperature: float
    indoorhumidity: int