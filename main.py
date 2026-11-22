
from processors import TxtProcessor, CsvProcessor, ExcelProcessor, JsonProcessor
import pandas as pd
import argparse
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='processor.log'
)

def main():
    parser = argparse.ArgumentParser(description="File Processor CLI")
    
    parser.add_argument(
        "--type",
        choices=["txt", "csv", "excel", "json"],
        required=True,
        help="Type of file to process"
    )
    parser.add_argument("--input", required=True, help="Path to the input file")
    parser.add_argument("--output", required=True, help='Path to the output file')
    
    args = parser.parse_args()
    
    processors = {
        "txt": TxtProcessor,
        "csv": CsvProcessor,
        "excel": ExcelProcessor,
        "json": JsonProcessor
    }
    
    ProcessorClass = processors[args.type]
    
    try:
        processor = ProcessorClass(input_file=args.input, output_file=args.output)
        processor.read_data()
        processor.process_data()
        processor.save_data()
        logging.info(f'{args.type.upper()} processing complete')
        
        print(f'Successfully processed! {args.input} -> {args.output}')
    except Exception as e:
        logging.error(f'Failed to process {args.type.upper()} file: {e}')
        
        print(f'Error: {e}')

if __name__ == "__main__":
    main()