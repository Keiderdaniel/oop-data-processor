import sys
import pytest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from processors import TxtProcessor, CsvProcessor

def test_txt_processor_cleans_data(tmp_path: Path) -> None:
    """Test that TXT processor strips whitespaces, removes empty lines and 
    converts to uppercase."""
    
    output_file = tmp_path / "output.txt"
    
    processor = TxtProcessor(
        input_file = "tests/fixtures/sample.txt",
        output_file = str(output_file)
    )
    
    processor.read_data()
    processor.process_data()
    processor.save_data()
    
    with open(output_file, 'r', encoding='utf-8') as f:
        saved_lines = f.readlines()
        
    clean_lines = [line.strip() for line in saved_lines]
    
    assert clean_lines == ['HELLO WORLD', 'PYTHON IS GREAT']
    
def test_txt_processor_missing_file() -> None:
    """Test that TXT processor raises FileNotFoundError when the input file
    does not exist."""
    processor = TxtProcessor('non_existent_file.txt', 'output.txt')
    with pytest.raises(FileNotFoundError):
        processor.read_data()
    
def test_input_equals_output_raises_error() -> None:
    """Test that BaseProcessors raises ValueError if input and output paths
    are identical."""
    
    with pytest.raises(ValueError, match="Input and output files cannot be the same"):
        TxtProcessor('same.txt', 'same.txt')
        
def test_csv_processor_cleans_data(tmp_path: Path) -> None:
    """Test that CSV processor correctly groups categories and calculates
    totals"""
    
    output_file = tmp_path / "output.csv"
    processor = CsvProcessor(
        input_file = "tests/fixtures/sample.csv",
        output_file = str(output_file)
    )
    
    processor.read_data()
    processor.process_data()
    processor.save_data()
    
    with open(output_file, 'r', encoding='utf-8') as f:
        saved_lines = f.readlines()
        
    clean_lines = [line.strip() for line in saved_lines]
    assert clean_lines == [
        'category,total_value',
        'Electronics,150.50',
        'Books,20.00'
        ]
