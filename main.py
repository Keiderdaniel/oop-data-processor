from processors import TxtProcessor, CsvProcessor, ExcelProcessor, JsonProcessor

import pandas as pd

if __name__ == "__main__" :
    """
    processor = TxtProcessor("Dirty.txt", "clean.tx")
        processor.read_data()
        processor.process_data()
        processor.save_data()
        print("txt processing complete") 
    
        processor = CsvProcessor("sales_report.csv", "final_report.txt")
        processor.read_data()
        processor.process_data()
        processor.save_data()
        print("Csv processing complete")

        processor = JsonProcessor("data.json", "clean.json")
        processor.read_data()
        processor.process_data()
        processor.save_data()
        print("Json processing complete")
    
    """
    
    random_data = {
        "id": [1,2,3],
        "category": ["electronics", "books", "clothing"],
        "value": [1500, 50, 120]
    }
    
    df =pd.DataFrame(random_data)
    df.to_excel("input_data.xlsx", index=False)
    print("Excel file created")
    
    
    processor = ExcelProcessor("input_data.xlsx", "output_file.xlsx")
    processor.read_data()
    processor.process_data()
    processor.save_data()
    print("Excel processing complete")
    