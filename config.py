# config.py

"""
MODULE NAME: config.py
PART OF: City Weather Report
AUTHOR: Joshua C. Stroud
VERSION: 3.0
INTERPRETER: Python 3.12.10
PURPOSE: Stores constants and configuration values used across modules
DEPENDENCIES: None
LICENSE: GNU GPL v3.0

MODULE CHANGE LOG:

Module Version  |   Date        |   Description
---------------------------------------------------------------------------------------------------------
1.0             |   2025-09-24  |   Initial Release
---------------------------------------------------------------------------------------------------------
"""

cities_url = "https://cityweatherclass.free.beeceptor.com/cities"
weather_url = "https://cityweatherclass.free.beeceptor.com/weather"
headers = ["city", "population", "region", "temperature", "humidity"]
excel_filename = "city_weather_report_updated.xlsx"