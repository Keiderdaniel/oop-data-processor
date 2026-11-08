from processors import TxtProcessor, CsvProcessor

if __name__ == "__main__" :
    
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