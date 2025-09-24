# 🌆 City Weather Report

**Author**: Joshua C. Stroud  
**Version**: 3.0  
**License**: GNU GPL v3.0  
**Interpreter**: Python 3.12.10

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

## 📦 Installation

```bash
git clone https://github.com/yourusername/city-weather-report.git
cd city-weather-report
pip install -r requirements.txt

## ▶️ Usage

```bash
python main.py

 The Excel file city_weather_report_updated.xlsx will be created in the project directory.

## 📁 Project Structure

city-weather-report/
├── config.py
├── data_fetcher.py
├── data_merger.py
├── excel_writer.py
├── main.py
├── CHANGELOG.md
├── README.md
└── requirements.txt

## 🧪 Testing
Unit tests coming soon!

## 📜 License
This project is licensed under the GNU GPL v3.0.