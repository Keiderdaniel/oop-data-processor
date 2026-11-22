# File Processor

A Python Command Line Interface (CLI) tool that reads, cleans, and consolidates data from TXT, CSV, Excel and JSON files to automate file organization.

## Features

- **Multi-format Support:** Handles `.txt`, `.csv`, `.xlsx`, and `.json` files.
- **Object-Oriented Architecture:** Built using Abstract Base Classes (ABC).
- **Command Line Interface:** Powered by `argparse` for easier file processing without changing the code.
- **Error Handling:** Implements "fail-fast" principles to prevent silent failures.
- **Automated Testing:** Comprehensive test suite using `pytest`.
- **Containerized:** Fully dockerized for consistent execution across any environment.

## Technologies Used

- **Language:** Python 3.14
- **Data Manipulation:** Pandas, OpenPyXL (for Excel/CSV handling)
- **CLI:** Argparse
- **Testing:** Pytest
- **DevOps:** Docker, GitHub Actions (CI)

## How to Run

1. **Clone this repository:**
   ```bash
   git clone https://github.com/Keiderdaniel/oop-data-processor
   cd oop-data-processor
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the CLI:**
   ```bash
   # Example: Process a TXT file
   python main.py --type txt --input samples/dirty.txt --output output_data/clean.txt

   # Example: Process a CSV file
   python main.py --type csv --input samples/sales_report.csv --output output_data/report.txt
   ```

4. **Check the help menu:**
   ```bash
   python main.py --help
   ```

## Running Tests

This project uses `pytest` to ensure reliability:
```bash
pytest -v
```

## Docker Support

You can build and run this project using Docker (no local Python installation required):

1. **Build the image:**
   ```bash
   docker build -t file-processor .
   ```

2. **Run the container:**
   ```bash
   docker run --rm file-processor --type txt --input samples/dirty.txt --output output_data/docker_clean.txt
   ```

## Project Structure

```text
OOP_DATA_PROCESSOR/
├── .github/workflows/   # CI/CD pipeline (GitHub Actions)
├── logs/                # Generated logs
├── output_data/         # Processed output files
├── samples/             # Example input files
├── tests/               # Pytest automated tests
├── .gitignore
├── Dockerfile
├── main.py              # CLI entry point
├── processors.py        # Core OOP logic
├── README.md
└── requirements.txt
```

## CI/CD Status

[![Python CI](https://github.com/Keiderdaniel/oop-data-processor/actions/workflows/ci.yml/badge.svg)](https://github.com/Keiderdaniel/oop-data-processor/actions/workflows/ci.yml)