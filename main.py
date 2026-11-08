
from processors import TxtProcessor, CsvProcessor, ExcelProcessor, JsonProcessor

import pandas as pd

import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='processor.log'
)

if __name__ == "__main__" :
    
    #TXT
        
    processor = TxtProcessor("Dirty.txt", "clean.txt")
    processor.read_data()
    processor.process_data()
    processor.save_data()
    logging.info("txt processing complete") 
        
    #CSV
        
    processor = CsvProcessor("sales_report.csv", "final_report.txt")
    processor.read_data()
    processor.process_data()
    processor.save_data()
    logging.info("Csv processing complete")
    
    #EXCEL
            
    random_data = {
        "id": [1,2,3],
        "category": ["electronics", "books", "clothing"],
        "value": [1500, 50, 120]
        }
            
    df =pd.DataFrame(random_data)
    df.to_excel("input_data.xlsx", index=False)
    logging.info("Starting the processing")
            
            
    processor = ExcelProcessor("input_data.xlsx", "output_file.xlsx")
    processor.read_data()
    processor.process_data()
    processor.save_data()
    logging.info("Excel processing complete")
            
    #JSON
           
    processor = JsonProcessor("data.json", "clean.json")
    processor.read_data()
    processor.process_data()
    processor.save_data()
    logging.info("Json processing complete")
    
    try:
        bad_processor = TxtProcessor("dirty.txt", "dirty.txt")
    except ValueError as e:
        logging.error(f'Successfully caught error {e}')
        
    