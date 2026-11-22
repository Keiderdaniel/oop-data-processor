from abc import ABC, abstractmethod

import csv

import pandas as pd

import json

import logging

from pathlib import Path

class BaseProcessor(ABC):
    """
    Abstract base class for data processors.
    """
    def __init__ (self, input_file: str, output_file: str):
        """
        Initializes the processor.
        """
        self.input_file = Path(input_file)
        self.output_file = Path(output_file)
        
        if self.input_file.resolve() == self.output_file.resolve():
            raise ValueError("Input and output files cannot be the same")
        
        self.data = []
        self.processed_data = {}

    @abstractmethod 
    def read_data(self):
        """
        Reads data from the input file.
        """
        pass

    @abstractmethod
    def process_data(self):
        """
        Processes the data from the input file.
        """
        pass
    
    @abstractmethod
    def save_data(self):
        """
        Saves the processed data to the output file.
        """
        pass

class TxtProcessor(BaseProcessor):
    """
    Processor for TXT files.
    """
    def __init__(self, input_file: str, output_file: str):
        """
        Initializes the TXT processor.
        """
        super().__init__(input_file, output_file)

    def read_data(self) -> None:
        """
        Reads data from the TXT file and stores it in self.data.
        
        Raises:
            FileNotFound: If the input file does not exist.
        """
        try:
            with open(self.input_file, "r", encoding="utf-8") as f:
                for l in f:
                    self.data.append(l)
        except FileNotFoundError:
            logging.error(f'The file {self.input_file} was not found.')
            raise FileNotFoundError(f'The input file was not found: {self.input_file}')
                
    def process_data(self) -> None:
        """
        Processes the TXT data by removing whitespaces and empty lines.
        """
        clean_data = []
        for l in self.data:
            clean_line = l.strip().upper()
            if clean_line:
                clean_data.append(clean_line)
        self.data = clean_data
            

    def save_data(self) -> None:
        """
        Saves the processed data to the output TXT file.
        """
        try:
            with open(self.output_file, "w", encoding="utf8") as f:
                for item in self.data:
                    f.write(item + "\n")
        except PermissionError as e:
            logging.error('Permission Error')
            raise PermissionError('Permission denied when saving to {self.output_file}') from e

class CsvProcessor(BaseProcessor):
    """
    Processor for CSV files.
    """
    def __init__(self, input_file: str, output_file: str):
        """
        Initializes the CSV processor.
        """
        super().__init__(input_file, output_file)

    def read_data(self) -> None:
        """
        Reads data from the input file and stores it in self.data.
        
        Raises:
            FileNotFound: If the file does not exist.
        """
        try:
            with open(self.input_file, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for l in reader:
                    self.data.append(l)
        except FileNotFoundError:
            logging.error(f'The file {self.input_file} was not found.')
            raise FileNotFoundError(f'The input file was not found: {self.input_file}')
            
        
    def process_data(self) -> None:
        """
        Processes the CSV data by grouping items by categories
        and calculating the total value of each category.
        Invalid values are skipped.
        
        Raises:
            ValueError: If the value of an item is invalid.
        """
        totals = {}
        for item in self.data:
            try:
                category = item["category"]
                value = float(item["value"])
                if category in totals:
                    totals[category] = totals[category] + value
                else:
                    totals[category] = value
            except KeyError as e:
                logging.warning(f'Missing required column in CSV: {e}')
                raise KeyError(f'Invalid error for {e}')
            except ValueError:
                logging.warning(f'Invalid value found for item {item}')
                continue
        self.processed_data = totals
        
    def save_data(self) -> None:
        """
        Saves the processed data to the output CSV file.
        """
        try:
            with open(self.output_file, "w", encoding="utf8") as f:    
                f.write("--------------\n")
                f.write(" Sales Report \n")
                f.write("--------------\n")
                for category, value in self.processed_data.items():
                    f.write(f'{category.title()}: R$ {value:.2f}\n')
        except PermissionError:
                logging.error("Permission Error")

class ExcelProcessor(BaseProcessor):
    """
    Processor for Excel files.
    """
    def __init__(self, input_file: str, output_file: str):
        """
        Initializes the EXCEL processor. 
        """
        super().__init__(input_file, output_file)
    
    def read_data(self) -> None:
        """
        Reads data from the input EXCEL file and stores it in self.data
        """
        try:
            self.data = pd.read_excel(self.input_file)
        except FileNotFoundError:
            logging.error(f'The file {self.input_file} was not found.')
            raise FileNotFoundError(f'The input file was not found: {self.input_file}')
        except ValueError as e:
            logging.error(f'Invalid Excel format: {e}')
            raise ValueError(f'The file is not a valid xlsx file: {self.input_file}')
 
    def process_data(self) -> None:
        """
        Processes The EXCEL data by ...
        """
        self.processed_data = self.data
            
    def save_data(self) -> None:
        """
        Saves the processed data to the output EXCEL file.
        """
        self.processed_data.to_excel(self.output_file, index=False)
        
class JsonProcessor(BaseProcessor):
    """
    Processor for JSON files.
    """
    
    def __init__(self, input_file: str, output_file: str) -> None:
        """
        Initializes the JSON processor.
        """
        super().__init__(input_file, output_file)
        
    def read_data(self) -> None:
        """
        Reads data form the input JSON file and stores it in self.data
        
        Raises: 
            FileNotFoundError: if the input file does not exist.
            json.JSONDecodeError: if the file content is not valid JSON.
        """
        try:
            with open(self.input_file, "r", encoding="utf8") as f:
                self.data = json.load(f)
        except FileNotFoundError:
            logging.error(f'The file {self.input_file} was not found')
            raise FileNotFoundError(f'The file was not found: {self.input_file}')
        except json.JSONDecodeError:
            logging.error(f'The file {self.input_file} is not a valid JSON file.')
            raise ValueError(f'Invalid JSON format in file: {self.input_file}')
            
    def process_data(self) -> None:
        """
        Processes the JSON data by adding a "status" key to each dictionary.
        """
        try:
            for item in self.data:
                item['status'] = "processed"
            self.processed_data = self.data 
        except TypeError:
            raise ValueError('The JSON file is not a list of dictionaries')
            
    def save_data(self) -> None:
        """
        Saves the processed data to the output JSON file.
        """
        with open(self.output_file, "w", encoding="utf-8") as f:
            json.dump(self.processed_data, f, indent=4)
            