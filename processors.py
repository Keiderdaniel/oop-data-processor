from abc import ABC, abstractmethod

import csv

import pandas as pd

class BaseProcessor(ABC):
    def __init__ (self, input_file: str, output_file: str):
        self.input_file = input_file
        self.output_file = output_file
        self.data = []
        self.processed_data = {}
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
        clean_data = []
        for l in self.data:
            clean_line = l.strip().upper()
            if clean_line:
                clean_data.append(clean_line)
        self.data = clean_data
            

    def save_data(self):
        with open(self.output_file, "w", encoding="utf8") as f:
            for item in self.data:
                f.write(item + "\n")

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
        totals = {}
        for item in self.data:
            category = item["category"]
            try:
                value = float(item["value"])
                if category in totals:
                    totals[category] = totals[category] + value
                else:
                    totals[category] = value
            except ValueError:
                print(f'Invalid error for {item}')
        self.processed_data = totals
        
    def save_data(self):
        try:
            with open(self.output_file, "w", encoding="utf8") as f:    
                f.write("--------------\n")
                f.write(" Sales Report \n")
                f.write("--------------\n")
                for category, value in self.processed_data.items():
                    f.write(f'{category.title()}: R$ {value:.2f}\n')
        except PermissionError:
                print("Permission Error")

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
        