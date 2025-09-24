# 🌆 City Weather Report

**Author**: Joshua C. Stroud  
**Version**: 3.0  
**Interpreter**: Python 3.12.10  
**License**: GNU GPL v3.0  

## 📌 Overview

City Weather Report is a Python application that retrieves JSON data from two public APIs — one for city demographics and one for weather conditions — merges the data, and generates a formatted Excel report with two worksheets:
- **City Weather Report**: Full dataset
- **Cities by Region**: Grouped and sorted by region

## 🚀 Features

- Modular design with clean separation of concerns
- Robust error handling and logging
- Excel report with auto-formatting and column resizing
- Region-based grouping for enhanced readability

## 🧰 Technologies Used

- Python 3.12
- `requests` for API calls
- `json` for data parsing
- `openpyxl` for Excel generation
- `logging` for diagnostics

## ▶️ Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/city-weather-report.git
   cd city-weather-report
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
3. Run the program
    ```bash
    python main.py
4. Output:
    - An Excel file named city_weather_report_updated.xlsx will be created in the project directory.
    - This file contains two worksheets: one with all combined demographic and weather data sorted alphabetically, and one sorted by region.

## 📁 Project Structure
    
    city-weather-report/
    ├── config.py               # Stores constants and configuration
    ├── data_fetcher.py         # Fetches JSON data from APIs
    ├── data_merger.py          # Merges city and weather data
    ├── excel_writer.py         # Creates and formats Excel workbook
    ├── main.py                 # Orchestrates the workflow
    ├── CHANGELOG.md            # Version history and updates
    ├── README.md               # Project documentation
    ├── requirements.txt        # Python dependencies
    └── .gitignore              # Files to exclude from Git tracking

## 🧪 Testing

Unit tests are planned for future versions. Suggested test coverage includes:
- Validating API response structure
- Ensuring correct merging of city and weather data
- Verifying Excel file creation and formatting
Test framework recommendation: unittest or pytest.

## 📜 License
This project is licensed under the GNU General Public License v3.0. You are free to use, modify, and distribute this software under the terms of the license.

For full license details, see GNU GPL v3.0. https://www.gnu.org/licenses/gpl-3.0.en.html