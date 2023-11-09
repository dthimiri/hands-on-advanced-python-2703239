# Example file for Advanced Python: Hands On by Joe Marini
# Introspect the data to make some determinations

import json
import pprint

# open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)

# TODO: What was the warmest day in the data set?
warmday = max(weatherdata, key=lambda x: x['tmax'])
print(warmday)
print(f"The warmest day was {warmday['date']} at {warmday['tmax']}")

# TODO: What was the coldest day in the data set?
coldestday = min(weatherdata, key=lambda x: x['tmin'])
print(coldestday)
print(f"The coldest day was {warmday['date']} at {warmday['tmin']}")

# TODO: How many days had snowfall?
snowday = [x for x in weatherdata if x['snow'] > 0]
print(f"Snow fell on {len(snowday)} days")

