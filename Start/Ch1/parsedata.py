# Example file for Advanced Python: Hands On by Joe Marini
# Load and parse a JSON data file and determine some information about it
import json
import pprint

# TODO: open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", 'r') as weatherfile:
    weatherdata = json.load(weatherfile)
    

# TODO: make sure the data loaded correctly by printing the length of the dataset
print(len(weatherdata))

# TODO: let's also take a look at the first item in the data
pprint.pp(weatherdata[0])

# TODO: How many days of data do we have for each year?
years = {}
years1 = {}
for i in weatherdata:
    key = i['date'][0:4]
    key1 = i['date'][0:4]
    
    years1[key1] = years1.get(key1, 0) + 1
    if key in years:
        years[key] += 1
    else:
        years[key] = 1

print(years)
pprint.pp(years1)

