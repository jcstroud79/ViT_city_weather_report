# data_fetcher.py

"""
MODULE NAME: data_fetcher.py
PART OF: City Weather Report
AUTHOR: Joshua C. Stroud
VERSION: 3.0
INTERPRETER: Python 3.12.10
PURPOSE: Fetches and parses JSON data from external APIs
DEPENDENCIES: requests, json, logging
LICENSE: GNU GPL v3.0

MODULE CHANGE LOG:

Module Version  |   Date        |   Description
---------------------------------------------------------------------------------------------------------
1.0             |   2025-09-24  |   Initial Release
---------------------------------------------------------------------------------------------------------
"""

import requests
import json
import logging

def fetch_json_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return json.loads(response.text)
    except (requests.RequestException, json.JSONDecodeError) as e:
        logging.error(f"Error fetching data from {url}: {e}")
        raise