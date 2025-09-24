# data_merger.py

"""
MODULE NAME: data_merger.py
PART OF: City Weather Report
AUTHOR: Joshua C. Stroud
VERSION: 3.0
INTERPRETER: Python 3.12.10
PURPOSE: Merges city and weather data into a unified dictionary
DEPENDENCIES: None
LICENSE: GNU GPL v3.0

MODULE CHANGE LOG:

Module Version  |   Date        |   Description
---------------------------------------------------------------------------------------------------------
1.0             |   2025-09-24  |   Initial Release
---------------------------------------------------------------------------------------------------------
"""

def merge_data(cities, weather):
    merged = []
    for city in cities:
        match = next((w for w in weather if w["city"] == city["city"]), {})
        merged.append({**city, **match})
    return {item["city"]: item for item in merged}