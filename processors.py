from abc import ABC, abstractmethod

import csv

import pandas as pd

class BaseProcessor(ABC):
    def __init__ (self, input_file: str, output_file: str):
        self.input_file = input_file
        self.output_file = output_file
        self.data = []
        pass

    @abstractmethod 
    def read_data(self):
        pass

    @abstractmethod
    def process_data(self):
        pass
    @abstractmethod
    def save_data(self):
        pass

class TxtProcessor(BaseProcessor):
    def __init__(self, input_file: str, output_file: str):
        super().__init__(input_file, output_file)

    def read_data(self):
        try:
            with open(self.input_file, "r", encoding="utf-8") as f:
                for l in f:
                    self.data.append(l)
        except FileNotFoundError:
            print(f'The file {self.input_file} was not found.')
            return []
                
    def process_data(self):
            pass

    def save_data(self):
            pass

class CsvProcessor(BaseProcessor):
    def __init__(self, input_file: str, output_file: str):
        super().__init__(input_file, output_file)

    def read_data(self):
        try:
            with open(self.input_file, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for l in reader:
                    self.data.append(l)
        except FileNotFoundError:
            print(f'The file {self.input_file} was not found.')
            return []
            
        
    def process_data(self):
        pass
        
    def save_data(self):
        pass

class ExcelProcessor(BaseProcessor):
    def __init__(self, input_file: str, output_file: str):
        super().__init__(input_file, output_file)
    
    def read_data(self):
        try:
            self.data = pd.read_excel(self.input_file)
        except FileNotFoundError:
                print(f'The file {self.input_file} was not found.')
                return []
            
    def process_data(self):
        pass
            
    def save_data(self):
        pass
        