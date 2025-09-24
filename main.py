# main.py

"""
MODULE NAME: main.py
PART OF: City Weather Report
AUTHOR: Joshua C. Stroud
VERSION: 3.0
INTERPRETER: Python 3.12.10
PURPOSE: Orchestrates data fetching, merging, and report generation
DEPENDENCIES: config, data_fetcher, data_merger, report_writer, logging
LICENSE: GNU GPL v3.0

MODULE CHANGE LOG:

Module Version  |   Date        |   Description
---------------------------------------------------------------------------------------------------------
1.0             |   2025-09-24  |   Initial Release
---------------------------------------------------------------------------------------------------------
"""

import logging
from config import cities_url, weather_url, excel_filename
from data_fetcher import fetch_json_data
from data_merger import merge_data
from report_writer import create_excel_report

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

def main():
    try:
        cities = fetch_json_data(cities_url)
        weather = fetch_json_data(weather_url)
        combined_data = merge_data(cities, weather)
        create_excel_report(combined_data, excel_filename)
    except Exception as e:
        logging.critical(f"Program failed: {e}")

if __name__ == "__main__":
    main()