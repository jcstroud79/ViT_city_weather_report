# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),  
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [3.0] - 2025-09-24
### Added
- Modularized the project into separate Python files: `config.py`, `data_fetcher.py`, `data_merger.py`, `report_writer.py`, and `main.py`
- Created second worksheet in Excel report grouped by region
- Added `format_worksheet()` helper function to reduce code duplication
- Implemented logging for debugging and error tracking
- Added type checking for Excel data rows

---

## [2.0] - 2025-09-24
### Added
- Defined functions for data fetching, merging, and Excel writing
- Added type checking for dictionary validation
- Created grouped worksheet by region based on client request
- Changed output filename to `city_weather_report_updated.xlsx`

---

## [1.1] - 2025-09-24
### Changed
- Refactored monolithic script into modular functions
- Improved readability and maintainability

---

## [1.0] - 2025-09-23
### Initial Release
- Fetches JSON data from two APIs
- Merges city and weather data
- Outputs combined data to Excel spreadsheet
