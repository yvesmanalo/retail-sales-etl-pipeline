from etl.extract import extract

file_location = "data/raw"
file_name = "sales_data.csv"

extract(file_location=file_location,file_name=file_name)