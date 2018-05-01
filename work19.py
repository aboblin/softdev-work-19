from flask import Flask
import requests
import json

response = requests.get("http://api.population.io/1.0/population/1990/United%20States/?format=json")

print response.json()
